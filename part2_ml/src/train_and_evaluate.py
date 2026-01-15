from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


TRAIN_PATH = Path("part2_ml/data/processed/train.csv")
TEST_PATH = Path("part2_ml/data/processed/test.csv")
RESULTS_DIR = Path("part2_ml/results")
METRICS_PATH = RESULTS_DIR / "metrics.csv"

TARGET_COL = "loan_approved"
NUMERIC_FEATURES = ["income", "credit_score", "loan_amount", "loan_term"]
CATEGORICAL_FEATURES = ["employment_status"]


def build_preprocessor() -> ColumnTransformer:
    return ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), NUMERIC_FEATURES),
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
        ],
        remainder="drop",
    )


def evaluate_model(name: str, pipeline: Pipeline, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
    preds = pipeline.predict(X_test)

    return {
        "model": name,
        "accuracy": accuracy_score(y_test, preds),
        "precision": precision_score(y_test, preds, zero_division=0),
        "recall": recall_score(y_test, preds, zero_division=0),
        "f1": f1_score(y_test, preds, zero_division=0),
    }


def main() -> None:
    train_df = pd.read_csv(TRAIN_PATH)
    test_df = pd.read_csv(TEST_PATH)

    X_train = train_df.drop(columns=[TARGET_COL])
    y_train = train_df[TARGET_COL].astype(int)

    X_test = test_df.drop(columns=[TARGET_COL])
    y_test = test_df[TARGET_COL].astype(int)

    preprocessor = build_preprocessor()

    # Model 1: KNN (scaling is important)
    knn_pipeline = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("model", KNeighborsClassifier(n_neighbors=7)),
        ]
    )

    # Model 2: Decision Tree (interpretable baseline)
    tree_pipeline = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("model", DecisionTreeClassifier(max_depth=5, random_state=42)),
        ]
    )

    # Fit
    knn_pipeline.fit(X_train, y_train)
    tree_pipeline.fit(X_train, y_train)

    # Evaluate
    results = [
        evaluate_model("KNN (k=7)", knn_pipeline, X_test, y_test),
        evaluate_model("Decision Tree (max_depth=5)", tree_pipeline, X_test, y_test),
    ]

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    metrics_df = pd.DataFrame(results).sort_values(by="f1", ascending=False)
    metrics_df.to_csv(METRICS_PATH, index=False)

    print("\nModel comparison (sorted by F1):")
    print(metrics_df.to_string(index=False))
    print(f"\nSaved metrics: {METRICS_PATH}")


if __name__ == "__main__":
    main()
