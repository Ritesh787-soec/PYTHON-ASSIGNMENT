import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------ Create Sample Dataset ------------------
np.random.seed(42)
data = {
    "Age": np.random.randint(20, 60, 50),
    "BMI": np.random.normal(26, 4, 50),
    "Steps": np.random.randint(3000, 12000, 50),
    "Sleep_Hours": np.random.normal(6.5, 1.2, 50),
    "Workout_Min": np.random.randint(10, 90, 50)
}

df = pd.DataFrame(data)

# Introduce missing values
df.loc[5, "BMI"] = np.nan
df.loc[12, "Sleep_Hours"] = np.nan


# ------------------ 1. Missing Value Detection & Cleaning ------------------
print("\nMissing Values:\n", df.isnull().sum())

df["BMI"].fillna(df["BMI"].mean(), inplace=True)
df["Sleep_Hours"].fillna(df["Sleep_Hours"].median(), inplace=True)


# ------------------ 2. Outlier Detection (IQR) ------------------
Q1 = df["BMI"].quantile(0.25)
Q3 = df["BMI"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Treat outliers using capping
df["BMI"] = np.where(df["BMI"] > upper, upper,
                     np.where(df["BMI"] < lower, lower, df["BMI"]))


# ------------------ 3. Descriptive Statistics ------------------
print("\nDescriptive Statistics:\n", df.describe())


# ------------------ 4. Visualizations ------------------

# 4A Histogram
plt.figure()
plt.hist(df["BMI"])
plt.title("Histogram - BMI")
plt.xlabel("BMI")
plt.ylabel("Frequency")
plt.show()

# 4B Boxplot
plt.figure()
sns.boxplot(x=df["Sleep_Hours"])
plt.title("Boxplot - Sleep Hours")
plt.show()

# 4C Heatmap
plt.figure()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
