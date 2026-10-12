# Student Performance Analytics System

## 1. Project Title
* **Project Name:** Student Performance Analytics System[cite: 1]
* **Course:** Python with AI (EWB Courses)[cite: 1]
* **Submission Date:** October 15, 2026[cite: 1, 5]

---

## 2. Objective
The primary objective of this project is to build an automated, Python-based data analysis system that reads student performance data, calculates total and average marks, determines grades and pass/fail status, generates subject-wise statistics, and identifies top performers using NumPy and Pandas[cite: 1].

---

## 3. Technologies Used
* **Python 3.x**
* **NumPy** (for array operations and numerical aggregation)
* **Pandas** (for data loading, DataFrame manipulation, and filtering)[cite: 1, 3, 4]

---

## 4. Dataset Description
The dataset (`students.csv`) consists of **20 student records** structured with the following fields[cite: 1, 2]:
* `StudentID`: Unique identification number for each student[cite: 1]
* `Name`: Full name of the student[cite: 1]
* `Department`: Academic department (AI & DS)[cite: 1]
* `Python`: Marks obtained in Python (out of 100)[cite: 1]
* `DataScience`: Marks obtained in Data Science (out of 100)[cite: 1]
* `AI`: Marks obtained in Artificial Intelligence (out of 100)[cite: 1]
* `Attendance`: Attendance percentage[cite: 1]

---

## 5. Implementation
1. **Data Loading:** CSV file is read into a Pandas DataFrame using `load_dataset()` with exception handling[cite: 1, 2].
2. **Data Processing:**
   * Row-wise scores are converted to NumPy arrays to compute total marks and average scores[cite: 1, 2].
   * A minimum threshold of 40 marks in each individual subject determines the `Pass`/`Fail` status[cite: 1].
   * Academic grades (`A+`, `A`, `B`, `C`, `D`, `F`) are assigned based on average scores[cite: 1].
3. **Statistical Analysis:** Aggregate metrics (class average, overall pass percentage, subject-wise min/max/average) are calculated[cite: 1, 2].

---

## 6. Key Features
* Dynamic CSV dataset loading with error handling[cite: 1, 2].
* NumPy-accelerated row-wise numerical processing[cite: 1].
* Automated evaluation of pass/fail status and letter grade assignments[cite: 1].
* Subject-wise performance summary breakdown[cite: 1].
* Clean and readable tabular terminal output[cite: 2].

---

## 7. Sample Output
```text
Initializing Student Performance Analytics System...

✅ Dataset successfully loaded!

--- PROCESSED STUDENT DATA ---
 StudentID      Name  TotalMarks  Average Status Grade
       101     Aarav         263    87.67   Pass     A
       102    Ananya         240    80.00   Pass     A
       103    Bhavya         123    41.00   Fail     F
       104       Dev         281    93.67   Pass    A+
       105      Diya         183    61.00   Pass     C
       106    Gautam         107    35.67   Fail     F
       107      Isha         263    87.67   Pass     A
       108     Karan         217    72.33   Pass     B
       109     Kavya         289    96.33   Pass    A+
       110     Meera         165    55.00   Pass     D
       111    Nikhil         246    82.00   Pass     A
       112     Pooja          83    27.67   Fail     F
       113     Rahul         203    67.67   Pass     C
       114      Riya         271    90.33   Pass    A+
       115     Rohan         133    44.33   Pass     F
       116     Sanya         236    78.67   Pass     B
       117 Siddharth         267    89.00   Pass     A
       118     Tanvi         189    63.00   Pass     C
       119    Vikram         272    90.67   Pass    A+
       120      Zara         157    52.33   Pass     D

==================================================
      STUDENT PERFORMANCE ANALYTICS SUMMARY
==================================================
Total Students      : 20
Passed Students     : 17
Failed Students     : 3
Pass Percentage     : 85.00%
Class Average       : 69.8

--------------------------------------------------
SUBJECT-WISE PERFORMANCE ANALYSIS
--------------------------------------------------
[Python] -> Avg: 68.7 | Max: 95 | Min: 25
[DataScience] -> Avg: 70.6 | Max: 98 | Min: 30
[AI] -> Avg: 70.1 | Max: 96 | Min: 28

--------------------------------------------------
TOP PERFORMER
--------------------------------------------------
Name     : Kavya (ID: 109)
Average  : 96.33 | Grade: A+
==================================================