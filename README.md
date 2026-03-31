# Employee Data Cleaning & Preprocessing using Pandas

## Project Overview

This project focuses on **cleaning and preprocessing employee data** using Python libraries like **Pandas** and **NumPy**.
The goal is to transform raw, messy data into a clean and structured format suitable for analysis.

---

## Technologies Used

* Python 
* Pandas
* NumPy

---

## Dataset

The dataset contains employee-related information such as:

* Name
* Department
* Age
* Salary
* Performance Score
* Joining Date

---

## Features / Steps Performed

### Data Cleaning

* Removed duplicate records
* Handled missing values
* Replaced empty strings with `NaN`

### ✅ Data Transformation

* Standardized text (Name → Title Case, Department → Upper Case)
* Converted numeric columns (Age, Salary, Performance Score)
* Converted Joining Date to proper datetime format

### Missing Value Handling

* Filled **Age** with median
* Filled **Salary & Performance Score** with mean
* Filled missing **Name & Department** with default values

---

## Code Highlights

```python
df = pd.read_csv("employee_data.csv")

df = df.drop_duplicates()

df["Name"] = df["Name"].astype(str).str.strip().str.title()
df["Department"] = df["Department"].astype(str).str.strip().str.upper()

numeric_cols = ["Age", "Salary", "PerformanceScore"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
```

---

## Project Objective

To demonstrate **real-world data preprocessing techniques** which are essential in:

* Data Analysis
* Machine Learning
* Data Science projects

---

## Outcome

After cleaning:

* Data becomes consistent and usable
* Missing and incorrect values are handled
* Dataset is ready for analysis or modeling

---

## How to Run

1. Install required libraries:

   ```bash
   pip install pandas numpy
   ```
2. Run the script:

   ```bash
   python 1.py
   ```

---

## Use Case

This project is useful for:

* Beginners learning **Data Science**
* Understanding **data cleaning pipelines**
* Preparing datasets for **ML models**

---

## Author

**Priti Kumari**
BCA (AI/ML) Student

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
