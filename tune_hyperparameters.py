from pathlib import Path
from time import perf_counter

from Decision_tree_tuning import tune_decision_tree
from Random_forest_tuning import tune_random_forest
from timing_report import write_tuning_timing
from train_model import load_training_data, split_training_data


ROOT = Path(__file__).resolve().parent
OUTPUT_PATH = ROOT / "Result" / "best_hyperparameters.txt"


def main():
    features, labels = load_training_data()
    X_train, _, y_train, _ = split_training_data(
        features,
        labels,
        test_size=0.2,
        random_state=0,
    )

    start = perf_counter()
    tree_params, tree_results = tune_decision_tree(X_train, y_train)
    tree_seconds = perf_counter() - start

    start = perf_counter()
    forest_params, forest_results = tune_random_forest(X_train, y_train)
    forest_seconds = perf_counter() - start
    write_tuning_timing(tree_seconds, forest_seconds)
    tree_score = tree_results.loc[0, "mean_cv_macro_f1"]
    forest_score = forest_results.loc[0, "mean_cv_macro_f1"]

    report = (
        "Best hyperparameters from 5-fold stratified cross-validation\n"
        "These values are informational and are not automatically applied to task 1.py.\n\n"
        f"Decision tree (mean macro F1: {tree_score:.3f})\n"
        f"{tree_params}\n\n"
        f"Random forest (mean macro F1: {forest_score:.3f})\n"
        f"{forest_params}\n"
    )

    print(report)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")
    print(f"Saved best hyperparameters to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
