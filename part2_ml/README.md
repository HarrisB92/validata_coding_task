# Part 2 — Loan Approval Prediction (Machine Learning)

This task focuses on predicting loan approval using two machine learning models:
- K-Nearest Neighbors (KNN)
- Decision Tree

The objective is to compare model performance and extract business-relevant insights.

---

## Dataset

A synthetic dataset of 500 loan applications was generated to simulate a realistic
retail banking scenario.

Features:
- income
- credit_score
- loan_amount
- loan_term
- employment_status (categorical)
- loan_approved (target)

The dataset was generated using realistic statistical distributions and correlated
features. Loan approval was modeled probabilistically to reflect real-world uncertainty.

Raw dataset:
- `data/raw/loan_data.csv`

---

## Preprocessing

Preprocessing includes:
- Standardization of numerical features
- One-hot encoding of categorical features
- Stratified train/test split (80/20)

Preprocessing is applied inside the modeling pipeline to avoid data leakage.

Processed artifacts:
- `data/processed/loan_data_processed.csv`
- `data/processed/train.csv`
- `data/processed/test.csv`

---

## Models

Two models were trained and evaluated:

1. K-Nearest Neighbors (KNN)
2. Decision Tree (depth-limited for interpretability)

Evaluation metrics:
- Accuracy
- Precision
- Recall
- F1-score

---

## Results

Model performance metrics are stored in:
- `results/metrics.csv`

Feature importance (Decision Tree):
- `results/feature_importance.csv`

---

## Running the Pipeline

From the repository root:

1. Generate dataset:
   python part2_ml/src/generate_dataset.py

2. Preprocess data:
   python part2_ml/src/data_preprocessing.py

3. Train and evaluate models:
   python part2_ml/src/train_and_evaluate.py

4. Extract feature importance:
   python part2_ml/src/feature_importance.py

---

## Report

A detailed summary of findings and business insights is available in:
- `report.md`
