import pandas as pd
import numpy as np
import os

def calculate_stats(df, col):
    series = df[col].dropna()
    if len(series) == 0: return None
    stats = {
        'Count': len(series),
        'Mean': series.mean(),
        'Median': series.median(),
        'Min': series.min(),
        'Max': series.max(),
        'Range': series.max() - series.min(),
        'Variance': series.var(),
        'Std Dev': series.std(),
        'Skewness': series.skew(),
        'Kurtosis': series.kurt()
    }
    return stats

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cleaned_dir = os.path.join(script_dir, r"..\Data\cleaned")
    report_dir = os.path.join(script_dir, r"..\Reports\statistical_analysis")
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, 'univariate_analysis.md')
    
    csv_files = [f for f in os.listdir(cleaned_dir) if f.endswith('.csv')]
    
    with open(report_path, 'w') as f:
        f.write("# Univariate Analysis Report\n")
        f.write("**Project:** NexaChain Intelligence Platform\n")
        f.write("**Phase:** Week 2 - Statistical Analysis\n\n")
        f.write("This report provides a comprehensive statistical breakdown of all numerical variables across the cleaned enterprise datasets. It includes the calculation of central tendency, dispersion, and shape (skewness/kurtosis) for future predictive modeling.\n\n")
        
        for file in csv_files:
            file_path = os.path.join(cleaned_dir, file)
            df = pd.read_csv(file_path)
            numerics = df.select_dtypes(include=[np.number]).columns
            
            f.write(f"## Dataset: `{file}`\n")
            
            for col in numerics:
                # Skip IDs and flags
                if col.endswith('_id') or col.endswith('_flag'):
                    continue
                    
                stats = calculate_stats(df, col)
                if not stats: continue
                
                f.write(f"### Variable: `{col}`\n")
                f.write("| Metric | Value |\n| :--- | :--- |\n")
                for k, v in stats.items():
                    if isinstance(v, float):
                        f.write(f"| **{k}** | {v:,.4f} |\n")
                    else:
                        f.write(f"| **{k}** | {v:,} |\n")
                f.write("\n")
                
                # Business Interpretation based on Skewness
                if stats['Skewness'] > 1:
                    f.write("> **Observation:** This distribution is highly right-skewed (long tail on the right). Consider a log-transformation for Machine Learning models.\n\n")
                elif stats['Skewness'] < -1:
                    f.write("> **Observation:** This distribution is highly left-skewed. Watch for potential ceiling effects.\n\n")
                else:
                    f.write("> **Observation:** This variable has a relatively symmetrical distribution.\n\n")

if __name__ == "__main__":
    main()
    print("Univariate Analysis Complete!")
