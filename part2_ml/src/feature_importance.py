from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier


TRAIN_PATH = Path("part2_ml/data/processed/train.csv")
RESULTS_DIR = Path("part2_ml/results")
FEATURE_IMPORTANCE_PATH = RESULTS_DIR / "feature_importance.csv"

TARGET_COL = "loan_approved"
NUMERIC_FEATURES = ["income", "credit_score", "loan_amount", "loan_term"]
CATEGORICAL_FEATURES = ["employment_status"]


def main() -> None:
    train_df = pd.read_csv(TRAIN_PATH)

    X_train = train_df.drop(columns=[TARGET_COL])
    y_train = train_df[TARGET_COL].astype(int)

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), NUMERIC_FEATURES),
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
        ]
    )

    model = DecisionTreeClassifier(max_depth=5, random_state=42)

    pipeline = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("model", model),
        ]
    )

    pipeline.fit(X_train, y_train)

    # Extract feature names after preprocessing
    ohe = pipeline.named_steps["preprocess"].named_transformers_["cat"]
    cat_features = list(ohe.get_feature_names_out(CATEGORICAL_FEATURES))
    feature_names = NUMERIC_FEATURES + cat_features

    importances = pipeline.named_steps["model"].feature_importances_

    importance_df = (
        pd.DataFrame(
            {"feature": feature_names, "importance": importances}
        )
        .sort_values(by="importance", ascending=False)
        .reset_index(drop=True)
    )

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    importance_df.to_csv(FEATURE_IMPORTANCE_PATH, index=False)

    print("Feature importance (Decision Tree):")
    print(importance_df.to_string(index=False))
    print(f"\nSaved: {FEATURE_IMPORTANCE_PATH}")


if __name__ == "__main__":
    main()
