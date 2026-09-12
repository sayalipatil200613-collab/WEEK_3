import pandas as pd
import numpy as np

# ==========================================
# MINI PROJECT - EXPLORATORY DATA ANALYSIS
#===========================================

# 1. Load Dataset
df = pd.read_csv("students.csv")

print("===== STUDENT DATASET =====")
print(df)


# ==========================================
# 2. DATA EXPLORATION
# ==========================================

print("\n===== DATA EXPLORATION =====")

print("\nFirst 5 Rows:")
print(df.head())

print("\nShape of Dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)


# ==========================================
# 3. DATA CLEANING
# ==========================================

print("\n===== DATA CLEANING =====")

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing marks
df["Marks"] = df["Marks"].fillna(0)

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

print("\nCleaned Data:")
print(df)


# ==========================================
# 4. FILTERING
# ==========================================

print("\n===== FILTERING =====")

print("\nStudents with Marks greater than 80:")
print(df[df["Marks"] > 80])

print("\nStudents from Pune:")
print(df[df["City"] == "Pune"])


# ==========================================
# 5. SORTING
# ==========================================

print("\n===== SORTING =====")

print("\nStudents sorted by Marks:")
print(df.sort_values("Marks", ascending=False))


# ==========================================
# 6. GROUPBY
# ==========================================

print("\n===== GROUPBY =====")

print("\nAverage Marks by City:")
print(df.groupby("City")["Marks"].mean())

print("\nNumber of Students by City:")
print(df.groupby("City")["Name"].count())


# ==========================================
# 7. SUMMARY STATISTICS
# ==========================================

print("\n===== SUMMARY STATISTICS =====")

print("\nMean Marks:")
print(df["Marks"].mean())

print("\nMedian Marks:")
print(df["Marks"].median())

print("\nMaximum Marks:")
print(df["Marks"].max())

print("\nMinimum Marks:")
print(df["Marks"].min())


# ==========================================
# 8. NUMPY OPERATION
# ==========================================

print("\n===== NUMPY OPERATION =====")

marks_array = np.array(df["Marks"])

print("Marks Array:")
print(marks_array)

print("Total Marks using NumPy:")
print(np.sum(marks_array))

print("Average Marks using NumPy:")
print(np.mean(marks_array))


# ==========================================
# 9. BUSINESS / DATA INSIGHTS
# ==========================================

print("\n===== KEY INSIGHTS =====")

print("1. The highest marks are:", df["Marks"].max())

print("2. The lowest marks are:", df["Marks"].min())

print("3. The average marks are:", df["Marks"].mean())

print("4. The total number of students is:", len(df))

print("5. Pune students:")
print(df[df["City"] == "Pune"])
