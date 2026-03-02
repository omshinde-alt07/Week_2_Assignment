# Python Utilities Project

## Overview

This project contains three Python programs designed to demonstrate core Python skills, clean coding practices, and environment management. The programs focus on financial analysis, data type inspection, and basic user input processing. All scripts follow PEP 8 conventions and achieve a high Pylint score.

---

## Project Files

### 1. `finance_calculator.py`

A personal finance tool that collects employee salary details and generates a structured financial summary.

**Features**

* Input validation for:

  * Annual salary (> 0)
  * Tax percentage (0–50%)
  * Monthly rent (> 0)
  * Savings percentage (0–100%)
* Calculates:

  * Monthly gross salary
  * Tax deduction
  * Net salary
  * Rent ratio
  * Savings amount
  * Disposable income
* Provides annual projections
* Professional formatted report using f-strings

**Sample Output**

```
════════════════════════════════════════════
EMPLOYEE FINANCIAL SUMMARY
════════════════════════════════════════════
Employee : Om Shinde
Annual Salary : ₹800,000.00
────────────────────────────────────────────
Monthly Breakdown:
Gross Salary : ₹ 66,666.67
Tax (12.0%) : ₹ 8,000.00
Net Salary : ₹ 58,666.67
Rent : ₹ 5,000.00 (8.5% of net)
Savings (50.0%) : ₹ 29,333.33
Disposable : ₹ 24,333.33
────────────────────────────────────────────
Annual Projection:
Total Tax : ₹ 96,000.00
Total Savings : ₹ 352,000.00
Total Rent : ₹ 60,000.00
════════════════════════════════════════════
```

**Code Quality**

* Pylint Score: **9.80/10**
* Black formatted
* PEP 8 compliant

---

### 2. `data_type_analyzer.py`

A utility that analyzes any Python value and reports its properties.

**Features**

* Displays:

  * Value
  * Data type
  * Truthiness
  * Length (if applicable)

**Example Output**

```
Value: 42 | Type: int | Truthy: True | Length: N/A
Value:  | Type: str | Truthy: False | Length: 0
Value: [1, 2, 3] | Type: list | Truthy: True | Length: 3
Value: None | Type: NoneType | Truthy: False | Length: N/A
```

---

### 3. Basic User Info Script

A simple program that collects user name and age and determines adulthood.

**Example Output**

```
Name: Om
Age: 23
Om is 23 years old and is an Adult
In 5 years: 28
```

---

## Environment Setup

Activate virtual environment:

```
source onboarding_en/bin/activate
```

Run scripts:

```
python finance_calculator.py
python data_type_analyzer.py
```

Run Pylint:

```
pylint finance_calculator.py
```

---

## Notes

* Ensure a final newline at the end of files to avoid Pylint warnings.
* If using a `.pylintrc`, use fully qualified exception names (e.g., `builtins.Exception`).

---

## Skills Demonstrated

* Python fundamentals (input, functions, conditionals)
* Data validation
* String formatting with f-strings
* Code quality tools (Pylint, Black)
* Virtual environment usage
* Clean and modular programming

---

## Author

Om Shinde
