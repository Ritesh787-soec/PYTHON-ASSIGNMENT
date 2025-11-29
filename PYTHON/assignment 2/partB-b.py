import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------- 1. Create User Health Dataset ----------
data = {
    "Age": [21, 25, 30, 35, 40, 45, 50, 29, 33, 38],
    "Gender": ["M","F","M","F","M","F","M","F","M","F"],
    "Steps_per_day": [5000, 8000, 6000, 9000, 7000, 4000, 3000, 7500, 8200, 6800],
    "Sleep_Hours": [6.5, 7.2, 5.8, 6.9, 7.0, 6.0, 5.5, 6.8, 7.5, 6.3],
    "BMI": [22.0, 24.5, 27.8, 26.3, 28.7, 29.1, 31.2, 25.4, 23.9, 27.1],
    "Workout_minutes": [40, 60, 30, 50, 45, 20, 15, 55, 65, 35]
}

df = pd.DataFrame(data)

# ---------- 2. Clean Missing Values ----------
df = df.fillna(df.mean(numeric_only=True))

# ---------- 3. Correlation ----------
print("\nCorrelation Matrix:")
print(df[["Workout_minutes", "BMI", "Sleep_Hours"]].corr())

sns.heatmap(df[["Workout_minutes", "BMI", "Sleep_Hours"]].corr(),
            annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# ---------- 4. Visualizations ----------
# Steps vs BMI
plt.figure()
sns.scatterplot(x="Steps_per_day", y="BMI", hue="Gender", data=df)
plt.title("Steps vs BMI")
plt.show()

# Sleep Hours Distribution
plt.figure()
plt.hist(df["Sleep_Hours"])
plt.title("Sleep Hours Distribution")
plt.xlabel("Hours")
plt.ylabel("Frequency")
plt.show()
