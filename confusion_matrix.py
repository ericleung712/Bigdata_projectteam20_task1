from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix


CLASS_LABELS = [1, 2, 3, 4]
LABEL_NAMES = ["Sunny", "Cloudy", "Rainy", "Snowy"]


def save_confusion_matrices(y_true, predictions_by_model, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    confusion_matrices = {}

    for model_name, predictions in predictions_by_model.items():
        matrix = confusion_matrix(y_true, predictions, labels=CLASS_LABELS)
        confusion_matrices[model_name] = matrix
        print(f"\n{model_name} classification report:")
        print(
            classification_report(
                y_true,
                predictions,
                labels=CLASS_LABELS,
                target_names=LABEL_NAMES,
                zero_division=0,
            )
        )

        matrix_frame = pd.DataFrame(
            matrix,
            index=LABEL_NAMES,
            columns=LABEL_NAMES,
        )
        matrix_frame.to_csv(output_dir / f"confusion_matrix_{model_name}.csv")

        plt.figure(figsize=(6, 4))
        sns.heatmap(
            matrix,
            xticklabels=LABEL_NAMES,
            yticklabels=LABEL_NAMES,
            annot=True,
            fmt="d",
            cmap="Blues",
        )
        plt.title(f"{model_name.replace('_', ' ').title()} Confusion Matrix")
        plt.xlabel("Predicted label")
        plt.ylabel("True label")
        plt.tight_layout()
        plt.savefig(output_dir / f"confusion_matrix_{model_name}.png")
        plt.close()

    return confusion_matrices
