import pandas as pd
import numpy as np


df = pd.read_csv("employee_data.csv")
print("Original Data Shape:", df.shape)


df = df.drop_duplicates()


df["Name"] = df["Name"].astype(str).str.strip().str.title()
df["Department"] = df["Department"].astype(str).str.strip().str.upper()

df["Name"].replace("", np.nan, inplace=True)
df["Department"].replace("", np.nan, inplace=True)


numeric_cols = ["Age", "Salary", "PerformanceScore"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")  


df["JoiningDate"] = pd.to_datetime(df["JoiningDate"], errors="coerce")

df["Age"].fillna(df["Age"].median(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)
df["PerformanceScore"].fillna(df["PerformanceScore"].mean(), inplace=True)


df["Name"].fillna("Unknown", inplace=True)
df["Department"].fillna("UNKNOWN", inplace=True)


df.reset_index(drop=True, inplace=True)

print("Cleaned Data Shape:", df.shape)


df.to_csv("cleaned_employee_data.csv", index=False)
print("Cleaning Completed ")
print("New file created: cleaned_employee_data.csv")
