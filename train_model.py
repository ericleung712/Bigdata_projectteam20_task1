import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from Data_preparation import TRAIN_DATA_PATH, prepare_training_data

#def load_training_data(path=ROOT / "Training Data" / "train.csv"):
def load_training_data(path=TRAIN_DATA_PATH):
    data = pd.read_csv(path)
    return prepare_training_data(data)


def split_training_data(features, labels, test_size=0.2, random_state=0):
    return train_test_split(
        features,
        labels,
        test_size=test_size,
        stratify=labels,
        random_state=random_state,
    )


def main():
    from Decision_tree import Decision_Tree
    from Random_Forest import Random_Forest

    features, labels = load_training_data()
    X_train, X_test, y_train, y_test = split_training_data(features, labels)

    decision_tree = Decision_Tree(max_depth=10, min_samples_split=10)
    decision_tree.fit(X_train, y_train)
    tree_accuracy = np.mean(decision_tree.predict(X_test) == y_test) * 100
    print(f"Decision tree accuracy: {tree_accuracy:.3f}%")

    random_forest = Random_Forest(
        n_trees=20,
        max_depth=10,
        min_samples_split=10,
        min_samples_leaf=1,
        n_thresholds=25,
    )
    random_forest.fit(X_train, y_train)
    forest_accuracy = np.mean(random_forest.predict(X_test) == y_test) * 100
    print(f"Random forest accuracy: {forest_accuracy:.3f}%")


if __name__ == "__main__":
    main()
