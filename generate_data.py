from pathlib import Path
import numpy as np
import pandas as pd

np.random.seed(42)
ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)

n=7043
tenure=np.random.randint(1,73,n)
contract=np.random.choice(["Month-to-month","One year","Two year"],n,p=[.55,.25,.20])
internet=np.random.choice(["Fiber optic","DSL","No"],n,p=[.46,.39,.15])
support=np.random.choice(["Yes","No","No internet service"],n,p=[.31,.54,.15])
payment=np.random.choice(["Electronic check","Mailed check","Bank transfer","Credit card"],n,p=[.33,.20,.24,.23])
senior=np.random.choice([0,1],n,p=[.84,.16])
partner=np.random.choice(["Yes","No"],n)
dependents=np.random.choice(["Yes","No"],n,p=[.30,.70])
monthly=np.round(np.random.normal(72,28,n).clip(18,125),2)
paperless=np.random.choice(["Yes","No"],n,p=[.59,.41])

logit=(-1.8
       +1.25*(contract=="Month-to-month")
       -0.65*(contract=="One year")
       -1.05*(contract=="Two year")
       +0.55*(internet=="Fiber optic")
       +0.55*(payment=="Electronic check")
       +0.35*(support=="No")
       +0.45*senior
       -0.018*tenure
       +0.008*(monthly-70))
prob=1/(1+np.exp(-logit))
churn=np.where(np.random.rand(n)<prob,"Yes","No")
total=np.round(monthly*tenure + np.random.normal(0,100,n),2).clip(20,None)

df=pd.DataFrame({
    "customer_id":[f"CUST-{i:05d}" for i in range(1,n+1)],
    "tenure_months":tenure,
    "contract":contract,
    "internet_service":internet,
    "tech_support":support,
    "payment_method":payment,
    "senior_citizen":senior,
    "partner":partner,
    "dependents":dependents,
    "paperless_billing":paperless,
    "monthly_charges":monthly,
    "total_charges":total,
    "churn":churn
})
df.to_csv(DATA/"customer_churn.csv",index=False)
print(f"Created {len(df):,} synthetic customer records.")