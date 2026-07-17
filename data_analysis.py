import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

print("Dataset:")
print(df)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())

print("\nStudents Scoring Above 80:")
print(df[df["Marks"] > 80])
