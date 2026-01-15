import os
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


RAW_PATH = Path("part2_ml/data/raw/loan_data.csv")
PROCESSED_DIR = Path("part2_ml/data/processed")
PROCESSED_DATASET_PATH = PROCESSED_DIR / "loan_data_processed.csv"
TRAIN_PATH = PROCESSED_DIR / "train.csv"
TEST_PATH = PROCESSED_DIR / "test.csv"


def main() -> None:
    df = pd.read_csv(RAW_PATH)

    target_col = "loan_approved"
    X = df.drop(columns=[target_col])
    y = df[target_col].astype(int)

    numeric_features = ["income", "credit_score", "loan_amount", "loan_term"]
    categorical_features = ["employment_status"]

    # Preprocessing:
    # - One-hot encode employment_status
    # - Standardize numeric features (important for KNN)
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ],
        remainder="drop",
    )

    # Fit on full dataset ONLY for the purpose of exporting a processed dataset CSV
    # (Train/Test split is done separately below for modeling.)
    X_processed = preprocessor.fit_transform(X)

    # Build feature names for the processed matrix
    ohe = preprocessor.named_transformers_["cat"]
    cat_feature_names = list(ohe.get_feature_names_out(categorical_features))
    feature_names = numeric_features + cat_feature_names

    processed_df = pd.DataFrame(X_processed.toarray() if hasattr(X_processed, "toarray") else X_processed,
                                columns=feature_names)
    processed_df[target_col] = y.values

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    processed_df.to_csv(PROCESSED_DATASET_PATH, index=False)

    # Train/test split for modeling (reproducible)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Save raw-split (unprocessed) so downstream scripts can reuse the same split
    train_df = X_train.copy()
    train_df[target_col] = y_train.values
    test_df = X_test.copy()
    test_df[target_col] = y_test.values

    train_df.to_csv(TRAIN_PATH, index=False)
    test_df.to_csv(TEST_PATH, index=False)

    print(f"Saved processed dataset: {PROCESSED_DATASET_PATH}")
    print(f"Saved train split: {TRAIN_PATH}")
    print(f"Saved test split: {TEST_PATH}")


if __name__ == "__main__":
    main()
