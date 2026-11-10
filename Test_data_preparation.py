from pathlib import Path

import pandas as pd

from Data_preparation import prepare_features


ROOT = Path(__file__).resolve().parent
TEST_DATA_PATH = ROOT / "Test Data" / "test.csv"
PREPARED_TEST_PATH = ROOT / "Test Data" / "cleaned_test_modified.csv"
#PREPARED_TEST_PATH = ROOT / "Test Data" / "cleaned_test_nointeractfeature.csv"
#PREPARED_TEST_PATH = ROOT / "Test Data" / "uncleaned_test.csv"


def prepare_test_data(path=TEST_DATA_PATH, feature_columns=None):
    data = pd.read_csv(path)
    if "id" not in data.columns:
        raise ValueError("Test data must include an 'id' column.")
    ids = data["id"].copy()
    features = prepare_features(data, feature_columns=feature_columns)
    return ids, features


def main():
    ids, features = prepare_test_data()
    prepared = features.copy()
    prepared.insert(0, "id", ids.to_numpy())
    prepared.to_csv(PREPARED_TEST_PATH, index=False)
    print(f"Prepared test data saved to: {PREPARED_TEST_PATH}")


if __name__ == "__main__":
    main()
