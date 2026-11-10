import pickle
from pathlib import Path
from time import perf_counter

from Decision_tree import Decision_Tree
from Random_Forest import Random_Forest
from confusion_matrix import save_confusion_matrices
from timing_report import fit_with_timing, write_training_timing
from train_model import load_training_data, split_training_data


ROOT = Path(__file__).resolve().parent
MODEL_WEIGHTS_DIR = ROOT / "model_weights"
GRAPH_DIR = ROOT / "Graph"

LABEL_MAPPING = {
    1: "Sunny",
    2: "Cloudy",
    3: "Rainy",
    4: "Snowy",
}

# Decision tree parameters before tuning
#TREE_PARAMETERS = {
#    "max_depth": 10,
#    "min_samples_split": 10,
#    "min_samples_leaf": 2,
#    "n_thresholds": 10,
#}

# Decision tree parameters After tuning
TREE_PARAMETERS = {
    "max_depth": 10,
    "min_samples_split": 10,
    "min_samples_leaf": 2,
    "n_thresholds": 50,
}

# Decision tree parameters before tuning
#FOREST_PARAMETERS = {
#    "n_trees": 10,
#    "max_depth": 10,
#    "min_samples_split": 10,
#    "min_samples_leaf": 2,
#    "n_thresholds": 10,
#    "random_state": 0,
#}

# Random forest parameters After tuning
FOREST_PARAMETERS = {
    "n_trees": 20,
    "max_depth": 10,
    "min_samples_split": 2,
    "min_samples_leaf": 1,
    "n_thresholds": 25,
    "random_state": 25,
}



def save_model(model_name, model, feature_columns, parameters):
    artifact = {
        "model": model,
        "feature_columns": list(feature_columns),
        "label_mapping": LABEL_MAPPING,
        "parameters": parameters,
    }
    output_path = MODEL_WEIGHTS_DIR / f"{model_name}.pkl"
    with output_path.open("wb") as model_file:
        pickle.dump(artifact, model_file)
    print(f"Saved {model_name} weights to: {output_path}")


def main():
    MODEL_WEIGHTS_DIR.mkdir(parents=True, exist_ok=True)
    GRAPH_DIR.mkdir(parents=True, exist_ok=True)

    preprocessing_start = perf_counter()
    features, labels = load_training_data()
    X_train, X_validation, y_train, y_validation = split_training_data(
        features,
        labels,
        test_size=0.2,
        random_state=0,
    )
    preprocessing_seconds = perf_counter() - preprocessing_start

    validation_tree = Decision_Tree(**TREE_PARAMETERS)
    tree_validation_seconds = fit_with_timing(validation_tree, X_train, y_train)
    tree_predictions = validation_tree.predict(X_validation)

    validation_forest = Random_Forest(**FOREST_PARAMETERS)
    forest_validation_seconds = fit_with_timing(validation_forest, X_train, y_train)
    forest_predictions = validation_forest.predict(X_validation)

    save_confusion_matrices(
        y_validation,
        {
            "decision_tree": tree_predictions,
            "random_forest": forest_predictions,
        },
        GRAPH_DIR,
    )

    final_tree = Decision_Tree(**TREE_PARAMETERS)
    tree_final_seconds = fit_with_timing(final_tree, features, labels)
    final_forest = Random_Forest(**FOREST_PARAMETERS)
    forest_final_seconds = fit_with_timing(final_forest, features, labels)

    save_model("decision_tree", final_tree, features.columns, TREE_PARAMETERS)
    save_model("random_forest", final_forest, features.columns, FOREST_PARAMETERS)
    write_training_timing(
        preprocessing_seconds,
        {
            "decision_tree_validation": tree_validation_seconds,
            "decision_tree_final": tree_final_seconds,
            "random_forest_validation": forest_validation_seconds,
            "random_forest_final": forest_final_seconds,
        },
    )
    print("Training and evaluation complete.")


if __name__ == "__main__":
    main()
