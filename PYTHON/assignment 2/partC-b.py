import pandas as pd
import numpy as np
from scipy.stats import zscore

# Sample Credit Card Withdrawal Dataset
data = {
    "Customer_ID": range(1, 15),
    "Withdrawal": [2000, 2500, 3000, 2800, 5000, 5200, 6000, 15000, 16000, 17000, 2600, 2550, 2400, 40000]
}

df = pd.DataFrame(data)

# ------------------ 1. Detect Outliers (Z-score) ------------------
df["Zscore"] = zscore(df["Withdrawal"])
z_outliers = df[df["Zscore"].abs() > 3]
print("\nZ-score Outliers:\n", z_outliers)


# ------------------ IQR Method ------------------
Q1 = df["Withdrawal"].quantile(0.25)
Q3 = df["Withdrawal"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

iqr_outliers = df[(df["Withdrawal"] < lower) | (df["Withdrawal"] > upper)]
print("\nIQR Outliers:\n", iqr_outliers)


# ------------------ 3. Correct Outliers (Capping Method) ------------------
df["Corrected"] = np.where(df["Withdrawal"] > upper, upper,
                           np.where(df["Withdrawal"] < lower, lower, df["Withdrawal"]))

print("\nCorrected Dataset:\n", df)
