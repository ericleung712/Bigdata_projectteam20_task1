from itertools import product

import numpy as np
import pandas as pd
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold

from Decision_tree import Decision_Tree


PARAMETER_GRID = {
    "max_depth": [2, 4, 6, 10],
    "min_samples_leaf": [1, 2, 5, 10],
    "n_thresholds": [10, 25, 50],
}


def tune_decision_tree(X_train, y_train):
    X_array = np.asarray(X_train)
    y_array = np.asarray(y_train)
    class_labels = np.unique(y_array)
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
    results = []

    for max_depth, min_samples_leaf, n_thresholds in product(
        PARAMETER_GRID["max_depth"],
        PARAMETER_GRID["min_samples_leaf"],
        PARAMETER_GRID["n_thresholds"],
    ):
        fold_scores = []
        for train_indices, validation_indices in cv.split(X_array, y_array):
            tree = Decision_Tree(
                max_depth=max_depth,
                min_samples_split=10,
                min_samples_leaf=min_samples_leaf,
                n_thresholds=n_thresholds,
            )
            tree.fit(X_array[train_indices], y_array[train_indices])
            predictions = tree.predict(X_array[validation_indices])
            fold_scores.append(
                f1_score(
                    y_array[validation_indices],
                    predictions,
                    labels=class_labels,
                    average="macro",
                    zero_division=0,
                )
            )
        results.append(
            {
                "max_depth": max_depth,
                "min_samples_leaf": min_samples_leaf,
                "n_thresholds": n_thresholds,
                "mean_cv_macro_f1": np.mean(fold_scores),
            }
        )

    result_frame = pd.DataFrame(results).sort_values(
        "mean_cv_macro_f1", ascending=False, kind="stable"
    ).reset_index(drop=True)
    best_params = {
        name: int(result_frame.loc[0, name])
        for name in PARAMETER_GRID
    }
    print("Best decision-tree parameters:", best_params)
    print(f"Best mean 5-fold CV macro F1: {result_frame.loc[0, 'mean_cv_macro_f1']:.3f}")
    return best_params, result_frame
