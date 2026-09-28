from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "customer_churn.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
df["churn_flag"] = (df["churn"] == "Yes").astype(int)

print("Rows:", len(df))
print("Overall churn rate:", round(df["churn_flag"].mean() * 100, 2), "%")
print("\nChurn by contract:")
print((df.groupby("contract")["churn_flag"].mean() * 100).sort_values(ascending=False).round(2))
print("\nChurn by payment method:")
print((df.groupby("payment_method")["churn_flag"].mean() * 100).sort_values(ascending=False).round(2))
print("\nChurn by tech support:")
print((df.groupby("tech_support")["churn_flag"].mean() * 100).sort_values(ascending=False).round(2))

for col, filename, title in [
    ("contract", "churn_by_contract.png", "Churn Rate by Contract Type"),
    ("payment_method", "churn_by_payment.png", "Churn Rate by Payment Method"),
    ("tech_support", "churn_by_support.png", "Churn Rate by Tech Support"),
]:
    rate=(df.groupby(col)["churn_flag"].mean()*100).sort_values(ascending=False)
    plt.figure(figsize=(8,5))
    rate.plot(kind="bar")
    plt.title(title)
    plt.ylabel("Churn rate (%)")
    plt.xlabel("")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(OUT/filename, dpi=160)
    plt.close()
