from itertools import product

import numpy as np
import pandas as pd
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold

from Random_Forest import Random_Forest


PARAMETER_GRID = {
    "n_trees": [5, 10, 20],
    "max_depth": [4, 10, 20],
    "min_samples_split": [2, 10, 20],
    "min_samples_leaf": [1, 5, 10],
    "n_thresholds": [10, 25],
}


def tune_random_forest(X_train, y_train):
    X_array = np.asarray(X_train)
    y_array = np.asarray(y_train)
    class_labels = np.unique(y_array)
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
    folds = list(cv.split(X_array, y_array))
    combinations = list(product(*PARAMETER_GRID.values()))
    results = []

    for combination_index, values in enumerate(combinations, start=1):
        params = dict(zip(PARAMETER_GRID, values))
        fold_scores = []
        for fold_index, (train_indices, validation_indices) in enumerate(folds):
            forest = Random_Forest(**params, random_state=42 + fold_index)
            forest.fit(X_array[train_indices], y_array[train_indices])
            predictions = forest.predict(X_array[validation_indices])
            fold_scores.append(
                f1_score(
                    y_array[validation_indices],
                    predictions,
                    labels=class_labels,
                    average="macro",
                    zero_division=0,
                )
            )
        mean_score = np.mean(fold_scores)
        results.append({**params, "mean_cv_macro_f1": mean_score})
        print(
            f"Completed {combination_index}/{len(combinations)}: "
            f"{params}, mean CV macro F1={mean_score:.3f}",
            flush=True,
        )

    result_frame = pd.DataFrame(results).sort_values(
        "mean_cv_macro_f1", ascending=False, kind="stable"
    ).reset_index(drop=True)
    best_params = {
        name: int(result_frame.loc[0, name])
        for name in PARAMETER_GRID
    }
    print("Best random-forest parameters:", best_params)
    print(f"Best mean 5-fold CV macro F1: {result_frame.loc[0, 'mean_cv_macro_f1']:.3f}")
    return best_params, result_frame
