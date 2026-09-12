import pandas as pd

# Read CSV file
df = pd.read_csv("students.csv")

print("Original Data:")
print(df)


# 1. Missing Values
print("\nMissing Values:")
print(df.isnull().sum())


# Fill Missing Values
df["Marks"] = df["Marks"].fillna(0)

print("\nAfter Filling Missing Values:")
print(df)


# 2. Duplicates
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove Duplicates
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)


# 3. Data Types
print("\nData Types:")
print(df.dtypes)


# Change Data Type
df["Age"] = df["Age"].astype(int)

print("\nAfter Changing Data Type:")
print(df.dtypes)


# 4. Renaming Columns
df = df.rename(columns={
    "Name": "Student_Name",
    "Marks": "Student_Marks"
})

print("\nAfter Renaming Columns:")
print(df)


# Final Data
print("\nFinal Cleaned Data:")
print(df)
