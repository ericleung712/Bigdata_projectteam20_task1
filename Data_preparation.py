from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent
TRAIN_DATA_PATH = ROOT / "Training Data" / "train.csv"
#PREPARED_DATA_PATH = ROOT / "Training Data" / "train_uncleaned.csv"
PREPARED_DATA_PATH = ROOT / "Training Data" / "train_cleaned_modified.csv"
#PREPARED_DATA_PATH = ROOT / "Training Data" / "train_cleaned_modified_nointeractfeature.csv"


def prepare_features(data, feature_columns=None):
    """Apply the shared training/test feature transformations."""
    df = data.drop(columns=["id", "label"], errors="ignore").copy()
    required_columns = {
        "Temperature",
        "Humidity",
        "Wind Speed",
        "Precipitation (%)",
        "Cloud Cover",
        "Atmospheric Pressure",
        "UV Index",
        "Season",
        "Visibility (km)",
        "Location",
    }
    missing_columns = required_columns.difference(df.columns)
    if missing_columns:
        raise ValueError(f"Input data is missing required columns: {sorted(missing_columns)}")

    # Clip numerical features to reasonable ranges to handle outliers.
    df["Humidity"] = df["Humidity"].clip(lower=0, upper=100)
    df["Precipitation (%)"] = df["Precipitation (%)"].clip(lower=0, upper=100)
    df["Temperature"] = df["Temperature"].clip(lower=-25, upper=70)
    df["Atmospheric Pressure"] = df["Atmospheric Pressure"].clip(lower=870, upper=1085)

    # Map cloud cover to ordinal values for easier processing.
    cloud_map = {
        "clear": 0,
        "partly cloudy": 1,
        "cloudy": 2,
        "overcast": 3,
    }
    df["Cloud_Cover_Ordinal"] = df["Cloud Cover"].map(cloud_map).fillna(-1).astype(int)

# Create additional derived features
    df["Freezing_Flag"] = (df["Temperature"] <= 0).astype(int)
    df["Snow_Potential"] = df["Precipitation (%)"] * df["Freezing_Flag"]
    df["Rain_Potential"] = df["Precipitation (%)"] * (1 - df["Freezing_Flag"])
    df["Moisture_Saturation"] = df["Humidity"] * (100.0 - df["Precipitation (%)"])
    df["Low_Vis_High_Hum"] = (
        (df["Visibility (km)"] < 2.0) & (df["Humidity"] > 85.0)
     ).astype(int)
    df["UV_per_Cloud"] = (df["UV Index"] + 1.0) / (df["Cloud_Cover_Ordinal"] + 1.0)

    # Categorize wind speed and visibility into discrete bins for easier modeling.
    df["Wind_Scale"] = pd.cut(
        df["Wind Speed"],
        bins=[-np.inf, 1.0, 12.0, 29.0, np.inf],
        labels=["Calm", "Light", "Moderate", "Strong_Gale"],
    )
    df["Visibility_Category"] = pd.cut(
        df["Visibility (km)"],
        bins=[-np.inf, 1.0, 4.0, np.inf],
        labels=["Dense_Fog", "Moderate_Fog", "Clear"],
    )

# One-hot encode categorical features and drop the original columns.
    df = pd.get_dummies(
        df,
        columns=["Season", "Location", "Wind_Scale", "Visibility_Category"],
        #columns=["Season", "Location", "Cloud Cover"],
        drop_first=False,
        dtype=float,
    )

    df = df.drop(columns=["Cloud Cover"])
    if feature_columns is not None:
        df = df.reindex(columns=feature_columns, fill_value=0)
    return df.astype(float)

def prepare_training_data(data):
    if "label" not in data.columns:
        raise ValueError("Training data must include a 'label' column.")
    features = prepare_features(data)
    labels = data["label"].to_numpy()
    return features, labels


def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import seaborn as sns

    raw_data = pd.read_csv(TRAIN_DATA_PATH)
    graph_dir = ROOT / "Graph"
    graph_dir.mkdir(parents=True, exist_ok=True)

    print("=== Raw Dataset shape and missing values ===")
    print(f"Shape: {raw_data.shape}")
    print(raw_data.isnull().sum())

    numeric_columns = [
        "Temperature",
        "Humidity",
        "Wind Speed",
        "Precipitation (%)",
        "Atmospheric Pressure",
        "Visibility (km)",
    ]

    print("\n=== Raw Dataset Numerical summary statistics (selected columns) ===")
    print(raw_data[numeric_columns].describe().T[["mean", "std", "min", "50%", "max"]])
    
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(14, 10))
    for index, column in enumerate(numeric_columns, 1):
        plt.subplot(2, 3, index)
        sns.boxplot(y=raw_data[column], color="skyblue")
        plt.title(f"Boxplot: {column}", fontsize=12)
    plt.tight_layout()
    plt.savefig(graph_dir / "eda_boxplots.png")
    plt.close()

    plt.figure(figsize=(14, 10))
    for index, column in enumerate(numeric_columns, 1):
        plt.subplot(2, 3, index)
        sns.histplot(raw_data[column], kde=True, bins=30, color="salmon")
        plt.title(f"Distribution: {column}", fontsize=12)
    plt.tight_layout()
    plt.savefig(graph_dir / "eda_distributions.png")
    plt.close()

    features, labels = prepare_training_data(raw_data)
    prepared = features.copy()
    prepared["label"] = labels
    prepared.to_csv(PREPARED_DATA_PATH, index=False)
    print(f"Prepared training data saved to: {PREPARED_DATA_PATH}")


if __name__ == "__main__":
    main()
