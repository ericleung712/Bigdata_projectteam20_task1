import pickle
from pathlib import Path
from time import perf_counter

import numpy as np
import pandas as pd

from Print_tree import visualize_decision_tree
from Test_data_preparation import TEST_DATA_PATH, prepare_test_data
from timing_report import write_inference_timing


ROOT = Path(__file__).resolve().parent
MODEL_WEIGHTS_DIR = ROOT / "model_weights"
RESULT_DIR = ROOT / "Result"
SAMPLE_SUBMISSION_PATH = ROOT / "Test Data" / "sample_submission.csv"


def load_model(model_name):
    # load a previously saved model, or explain which step creates it.
    model_path = MODEL_WEIGHTS_DIR / f"{model_name}.pkl"
    if not model_path.is_file():
        raise FileNotFoundError(
            f"Trained model not found at {model_path}. Run 'task 1.py' first."
        )
    with model_path.open("rb") as model_file:
        return pickle.load(model_file)


def main():
    # load both models and make sure they expect features in the same order.
    tree_artifact = load_model("decision_tree")
    forest_artifact = load_model("random_forest")
    feature_columns = tree_artifact["feature_columns"]
    if feature_columns != forest_artifact["feature_columns"]:
        raise ValueError("Saved models do not use the same feature-column order.")

    # prepare test features using the exact column order recorded during training.
    ids, features = prepare_test_data(TEST_DATA_PATH, feature_columns=feature_columns)
    sample_submission = pd.read_csv(SAMPLE_SUBMISSION_PATH)
    if sample_submission.columns.tolist() != ["id", "label"]:
        raise ValueError("sample_submission.csv must have exactly the columns 'id,label'.")
    if not np.array_equal(ids.to_numpy(), sample_submission["id"].to_numpy()):
        raise ValueError("Test data IDs do not match sample_submission.csv IDs and order.")

    # create output folders so prediction files and tree diagrams can be written.
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    graph_dir = ROOT / "Graph"
    graph_dir.mkdir(parents=True, exist_ok=True)

    inference_times = {}
    for model_name, artifact in (
        ("decision_tree", tree_artifact),
        ("random_forest", forest_artifact),
    ):
        model = artifact["model"]
        label_mapping = artifact["label_mapping"]
        # time only the prediction call so model inference can be compared.
        inference_start = perf_counter()
        predictions = model.predict(features)
        inference_times[model_name] = perf_counter() - inference_start
        # submission_labels = pd.Series(predictions).map(label_mapping)
        invalid_predictions = predictions[~np.isin(predictions, [1, 2, 3, 4])]
        if invalid_predictions.size:
            invalid_labels = np.unique(invalid_predictions).tolist()
            raise ValueError(
                f"{model_name} predicted labels outside 1, 2, 3, 4: {invalid_labels}"
            )

        # pair each prediction with its original id and save the submission file.
        submission = pd.DataFrame(
            {
                "id": ids.to_numpy(),
                "label": predictions,
            }
        )
        output_path = RESULT_DIR / f"submission_{model_name}.csv"
        submission.to_csv(output_path, index=False)
        print(f"Saved {model_name} submission to: {output_path}")
        # draw the decision tree, or the first tree as a representative forest example.
        model_to_draw = model if model_name == "decision_tree" else model.trees[0]
        graph = visualize_decision_tree(
            model_to_draw,
            feature_names=feature_columns,
            label_mapping=label_mapping,
        )
        for output_format in ("png", "svg"):
            output_path = graph.render(
                filename=str(graph_dir / model_name),
                format=output_format,
                cleanup=True,
            )
            print(f"Saved {model_name} tree diagram to: {output_path}")

    # record elapsed prediction time and the number of test rows processed.
    write_inference_timing(inference_times, len(features))


if __name__ == "__main__":
    main()
