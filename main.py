import pandas as pd
from functions import load_dataset, process_student_data, generate_summary

def main():
    dataset_path = 'students.csv'
    
    print("Initializing Student Performance Analytics System...\n")
    
    # 1. Load Data
    df = load_dataset(dataset_path)
    if df is None:
        return
    
    # 2. Process Data (Calculations, Pass/Fail, Grades)
    df_processed = process_student_data(df)
    
    # 3. Display Processed DataFrame Table
    print("\n--- PROCESSED STUDENT DATA ---")
    print(df_processed[['StudentID', 'Name', 'TotalMarks', 'Average', 'Status', 'Grade']].to_string(index=False))
    
    # 4. Generate Summary Statistics & Subject Analysis
    generate_summary(df_processed)

if __name__ == "__main__":
    main()