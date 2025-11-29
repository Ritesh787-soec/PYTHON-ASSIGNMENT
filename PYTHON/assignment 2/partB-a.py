import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------ Create Sample Dataset --------------
data = {
    "Age": [22, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    "BMI": [18.5, 22.3, 27.8, 31.2, 29.5, 26.0, 24.5, 28.7, 32.1, 33.5],
    "Heart_Rate": [72, 75, 80, 88, 90, 85, 78, 76, 82, 95]
}

df = pd.DataFrame(data)
print(df)

# ------------ 1. Histogram --------------
plt.figure()
plt.hist(df["BMI"])
plt.xlabel("BMI")
plt.ylabel("Frequency")
plt.title("Histogram of BMI")
plt.show()

# ------------ 2. Boxplot for Outliers --------------
plt.figure()
sns.boxplot(x=df["Heart_Rate"])
plt.title("Boxplot of Heart Rate")
plt.show()

# ------------ 3. Correlation Heatmap --------------
plt.figure()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
