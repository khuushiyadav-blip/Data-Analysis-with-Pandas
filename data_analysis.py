import pandas as pd

# Create DataFrame directly
data = {
    "Name": ["Riya", "Rahul", "Priya", "Agrima", "Anushka",
             "Sanskriti", "Snehalata", "Lata", "Asha",
             "Rekha", "Babita", "Raman", "Ramesh"],

    "Age": [18, 16, 15, 19, 20, 21, 20, 17, 14, 18, 19, 20, 23],

    "Marks": [100, 57, 67, 89, 95, 90, 98, 45, 33, 100, 47, 59, 87]
}

df = pd.DataFrame(data)

print("Student Dataset:")
print(df)

print("\nStatistical Summary:")
print(df.describe())

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())

print("\nAverage Age:")
print(df["Age"].mean())

print("\nStudents Scoring Above 80:")
print(df[df["Marks"] > 80])

print("\nTop Performer(s):")
print(df[df["Marks"] == df["Marks"].max()])
