import numpy as np
import pandas as pd


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))


def generate_dataset(n: int = 500, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    # Employment status (categorical)
    employment_status = rng.choice(
        ["employed", "self-employed", "unemployed"],
        size=n,
        p=[0.65, 0.25, 0.10],
    )

    # Income: log-normal (positive + right-skewed)
    income = rng.lognormal(mean=np.log(25000), sigma=0.5, size=n)
    income = np.clip(income, 5000, 200000)

    # Credit score: truncated normal (300-850)
    credit_score = rng.normal(loc=650, scale=80, size=n)
    credit_score = np.clip(credit_score, 300, 850)

    # Loan term (months): discrete distribution
    loan_term = rng.choice([12, 24, 36, 60], size=n, p=[0.15, 0.25, 0.45, 0.15])

    # Loan amount: correlated with income + term
    # (higher income & longer term → higher expected loan amount)
    base_loan = 0.22 * income + 2000 * (loan_term / 12)
    noise = rng.normal(loc=0, scale=5000, size=n)
    loan_amount = np.clip(base_loan + noise, 1000, 80000)

    # Employment stability score
    emp_score = np.select(
        [employment_status == "employed", employment_status == "self-employed", employment_status == "unemployed"],
        [0.6, 0.2, -0.8],
    )

    # Build approval probability (probabilistic decision)
    # Normalize key variables roughly to comparable scales
    income_z = (income - income.mean()) / income.std()
    credit_z = (credit_score - credit_score.mean()) / credit_score.std()
    loan_z = (loan_amount - loan_amount.mean()) / loan_amount.std()

    # Latent score: higher income/credit help, larger loan hurts, employment helps
    latent_score = (
        1.0 * credit_z
        + 0.6 * income_z
        - 0.7 * loan_z
        + emp_score
        + rng.normal(0, 0.4, size=n)  # noise (real-world uncertainty)
    )

    approval_prob = sigmoid(latent_score)
    loan_approved = rng.binomial(n=1, p=approval_prob, size=n)

    df = pd.DataFrame(
        {
            "income": income.round(0).astype(int),
            "credit_score": credit_score.round(0).astype(int),
            "loan_amount": loan_amount.round(0).astype(int),
            "loan_term": loan_term.astype(int),
            "employment_status": employment_status,
            "loan_approved": loan_approved.astype(int),
        }
    )

    return df


if __name__ == "__main__":
    df = generate_dataset(n=500, seed=42)
    df.to_csv("part2_ml/data/raw/loan_data.csv", index=False)
    print("Saved: part2_ml/data/raw/loan_data.csv")
    print(df.head())
