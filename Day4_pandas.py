import pandas as pd

# Series
marks = pd.Series([85, 90, 78, 88])
print("Series:")
print(marks)

# DataFrame
data = {
    "Name": ["Sayali", "Sakshi", "Priya", "Amit"],
    "Age": [22, 21, 23, 24],
    "Marks": [85, 90, 78, 88],
    "City": ["Pune", "Mumbai", "Nashik", "Pune"]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

# Reading CSV file
df = pd.read_csv("students.csv")

print("\nCSV Data:")
print(df)

# First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Shape
print("\nShape:")
print(df.shape)

# Columns
print("\nColumns:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes)
