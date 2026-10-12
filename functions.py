import pandas as pd
import numpy as np

def load_dataset(file_path):
    """CSV file-a Pandas DataFrame-a load panni return pannum."""
    try:
        df = pd.read_csv(file_path)
        print("✅ Dataset successfully loaded!")
        return df
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return None

def process_student_data(df):
    """Total marks, average, pass/fail status, and grades calculate pannum."""
    subject_cols = ['Python', 'DataScience', 'AI']
    
    # NumPy arrays use panni row-wise calculation
    marks_array = df[subject_cols].to_numpy()
    
    # Total and Average calculation using NumPy
    df['TotalMarks'] = np.sum(marks_array, axis=1)
    df['Average'] = np.round(np.mean(marks_array, axis=1), 2)
    
    # Pass/Fail logic: Individual subjects-la 40+ irukkanum
    def check_pass_fail(row):
        if row['Python'] >= 40 and row['DataScience'] >= 40 and row['AI'] >= 40:
            return 'Pass'
        return 'Fail'

    df['Status'] = df.apply(check_pass_fail, axis=1)
    
    # Grade assignment logic based on Average
    def assign_grade(avg):
        if avg >= 90:
            return 'A+'
        elif avg >= 80:
            return 'A'
        elif avg >= 70:
            return 'B'
        elif avg >= 60:
            return 'C'
        elif avg >= 50:
            return 'D'
        else:
            return 'F'

    df['Grade'] = df['Average'].apply(assign_grade)
    return df

def generate_summary(df):
    """Overall class statistics & Subject-wise performance summary print pannum."""
    print("\n" + "="*50)
    print("      STUDENT PERFORMANCE ANALYTICS SUMMARY")
    print("="*50)
    
    total_students = len(df)
    passed_students = len(df[df['Status'] == 'Pass'])
    failed_students = total_students - passed_students
    pass_percentage = (passed_students / total_students) * 100
    overall_avg = np.round(df['Average'].mean(), 2)

    print(f"Total Students      : {total_students}")
    print(f"Passed Students     : {passed_students}")
    print(f"Failed Students     : {failed_students}")
    print(f"Pass Percentage     : {pass_percentage:.2f}%")
    print(f"Class Average       : {overall_avg}")
    
    # Subject-wise Analysis
    print("\n" + "-"*50)
    print("SUBJECT-WISE PERFORMANCE ANALYSIS")
    print("-"*50)
    subjects = ['Python', 'DataScience', 'AI']
    for sub in subjects:
        sub_avg = np.round(df[sub].mean(), 2)
        sub_max = df[sub].max()
        sub_min = df[sub].min()
        print(f"[{sub}] -> Avg: {sub_avg} | Max: {sub_max} | Min: {sub_min}")
        
    # Top Performers
    top_performer = df.loc[df['Average'].idxmax()]
    print("\n" + "-"*50)
    print("TOP PERFORMER")
    print("-"*50)
    print(f"Name     : {top_performer['Name']} (ID: {top_performer['StudentID']})")
    print(f"Average  : {top_performer['Average']} | Grade: {top_performer['Grade']}")
    print("="*50 + "\n")