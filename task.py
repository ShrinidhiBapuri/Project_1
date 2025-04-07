# --------------------------------------------
# Student Performance Data Analysis Project
# --------------------------------------------

# 1. Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# 2. Load the Dataset
df = pd.read_csv("student-mat.csv")
print("First 5 rows of the dataset:")
print(df.head())

# 3. Initial Data Exploration
print("\nMissing values:\n", df.isnull().sum())
print("\nData types:\n", df.dtypes)
print("\nDataset shape (rows, columns):", df.shape)

# 4. Data Cleaning
df = df.drop_duplicates()
print("Shape after removing duplicates:", df.shape)

# 5. Data Analysis

# Q1: Average final grade (G3)
avg_g3 = df["G3"].mean()
print(f"\nAverage final grade (G3): {avg_g3:.2f}")

# Q2: Number of students scoring above 15 in G3
high_scorers = df[df["G3"] > 15].shape[0]
print(f"Number of students with G3 > 15: {high_scorers}")

# Q3: Correlation between study time and G3
correlation = df["studytime"].corr(df["G3"])
print(f"Correlation between study time and final grade (G3): {correlation:.2f}")

# Q4: Average final grade by gender
avg_by_gender = df.groupby("sex")["G3"].mean()
print("\nAverage final grade (G3) by gender:")
print(avg_by_gender)

# 6. Data Visualizations

# Histogram of Final Grades
plt.figure(figsize=(8, 5))
plt.hist(df["G3"], bins=15, color='skyblue', edgecolor='black')
plt.title("Distribution of Final Grades (G3)")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.grid(True)
plt.show()

# Scatter Plot: Study Time vs Final Grade
plt.figure(figsize=(8, 5))
sns.scatterplot(x="studytime", y="G3", data=df)
plt.title("Study Time vs Final Grade (G3)")
plt.xlabel("Study Time (hours/week)")
plt.ylabel("Final Grade (G3)")
plt.grid(True)
plt.show()

# Bar Chart: Average G3 by Gender
plt.figure(figsize=(6, 5))
sns.barplot(x=avg_by_gender.index, y=avg_by_gender.values, palette="pastel")
plt.title("Average Final Grade (G3) by Gender")
plt.xlabel("Gender")
plt.ylabel("Average G3")
plt.grid(True)
plt.show()
