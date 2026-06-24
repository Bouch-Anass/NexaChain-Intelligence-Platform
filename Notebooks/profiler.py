import pandas as pd
import os
import glob

data_dir = r"C:\Users\Anaess Bouch\Technocolabs Software Internship\Data"
csv_files = glob.glob(os.path.join(data_dir, "*.csv"))

for file in csv_files:
    print(f"\n--- Profiling {os.path.basename(file)} ---")
    try:
        df = pd.read_csv(file)
        print(f"Total Rows: {len(df)}")
        print(f"Total Columns: {len(df.columns)}")
        
        # Duplicates
        duplicates = df.duplicated().sum()
        print(f"Duplicate Rows: {duplicates}")
        
        # Missing values
        missing = df.isnull().sum()
        missing = missing[missing > 0]
        if not missing.empty:
            print("Missing Values:")
            for col, count in missing.items():
                print(f"  - {col}: {count} ({count/len(df)*100:.2f}%)")
        else:
            print("Missing Values: None")
            
        # Specific known issues based on PDF
        numerics = df.select_dtypes(include=['number']).columns
        negatives = (df[numerics] < 0).sum()
        negatives = negatives[negatives > 0]
        if not negatives.empty:
            print("Negative Values (Potential Invalids):")
            for col, count in negatives.items():
                print(f"  - {col}: {count} ({count/len(df)*100:.2f}%)")
                
    except Exception as e:
        print(f"Error reading {file}: {e}")
