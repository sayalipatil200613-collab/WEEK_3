import pandas as pd

# Read CSV file
df = pd.read_csv("students.csv")

# -----------------------------
# 1. DATA EXPLORATION
# -----------------------------

print("Original Data:")
print(df)

print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nNumber of Rows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)


# -----------------------------
# 2. FILTERING
# -----------------------------

print("\nStudents with Marks greater than 80:")
print(df[df["Marks"] > 80])

print("\nStudents from Pune:")
print(df[df["City"] == "Pune"])


# -----------------------------
# 3. SORTING
# -----------------------------

print("\nMarks in Descending Order:")
print(df.sort_values("Marks", ascending=False))

print("\nMarks in Ascending Order:")
print(df.sort_values("Marks", ascending=True))


# -----------------------------
# 4. GROUPBY
# -----------------------------

print("\nAverage Marks by City:")
print(df.groupby("City")["Marks"].mean())

print("\nNumber of Students by City:")
print(df.groupby("City")["Name"].count())


# -----------------------------
# 5. SUMMARY STATISTICS
# -----------------------------

print("\nSummary Statistics:")
print(df["Marks"].describe())

print("\nTotal Marks:")
print(df["Marks"].sum())

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nMaximum Marks:")
print(df["Marks"].max())

print("\nMinimum Marks:")
print(df["Marks"].min())

print("\nNumber of Students:")
print(df["Name"].count())
