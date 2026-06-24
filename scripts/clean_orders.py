import pandas as pd
import numpy as np
import logging
import os
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('clean_orders.log')
    ]
)

def load_data(file_path: str) -> pd.DataFrame:
    """Loads the dataset and prints basic dimensions."""
    try:
        logging.info(f"Loading data from {file_path}")
        df = pd.read_csv(file_path)
        logging.info(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        raise

def handle_duplicates(df: pd.DataFrame, subset: str, sort_col: str = None) -> pd.DataFrame:
    """Removes duplicate records keeping the latest if sort_col is provided."""
    initial_len = len(df)
    if sort_col and sort_col in df.columns:
        df = df.sort_values(by=sort_col, ascending=False)
    
    df = df.drop_duplicates(subset=[subset], keep='first')
    logging.info(f"Removed {initial_len - len(df)} duplicate records based on {subset}.")
    return df

def validate_dates(df: pd.DataFrame, date_col: str, max_date: str) -> pd.DataFrame:
    """Caps future dates to a maximum valid date."""
    if date_col in df.columns:
        df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
        max_dt = pd.to_datetime(max_date)
        
        future_mask = df[date_col] > max_dt
        future_count = future_mask.sum()
        
        df.loc[future_mask, date_col] = max_dt
        logging.info(f"Capped {future_count} future dates in {date_col} to {max_date}.")
    return df

def standardize_text(df: pd.DataFrame, text_col: str) -> pd.DataFrame:
    """Standardizes text categories (title case, strip whitespace)."""
    if text_col in df.columns:
        df[text_col] = df[text_col].astype(str).str.strip().str.title()
        df[text_col] = df[text_col].replace({'Ship.': 'Shipped'}) # Custom fix for known issue
        logging.info(f"Standardized text in {text_col}.")
    return df

def validate_numeric(df: pd.DataFrame, num_col: str) -> pd.DataFrame:
    """Handles negative order values based on business logic."""
    if num_col in df.columns:
        # If 'is_credit_note' exists, leave negative values alone where it's True
        negative_mask = df[num_col] < 0
        if 'is_credit_note' in df.columns:
            invalid_mask = negative_mask & (df['is_credit_note'] != 1)
        else:
            invalid_mask = negative_mask
            
        invalid_count = invalid_mask.sum()
        df.loc[invalid_mask, num_col] = np.nan
        df['data_entry_error'] = invalid_mask.astype(int)
        logging.info(f"Set {invalid_count} negative {num_col} values to NULL and flagged as errors.")
    return df

def clean_orders_dataset(input_path: str, output_path: str):
    """Main pipeline to clean the Orders dataset."""
    df = load_data(input_path)
    
    # 1. Deduplicate
    df = handle_duplicates(df, subset='order_id', sort_col='last_modified_date')
    
    # 2. Date Validation (Cap at 2024-12-31 per metadata)
    df = validate_dates(df, date_col='order_date', max_date='2024-12-31')
    
    # 3. Text Standardization
    df = standardize_text(df, text_col='order_status')
    
    # 4. Numeric Validation (Negative order_value_usd)
    df = validate_numeric(df, num_col='order_value_usd')
    
    # Export
    try:
        df.to_csv(output_path, index=False)
        logging.info(f"Successfully exported cleaned data to {output_path}")
    except Exception as e:
        logging.error(f"Failed to export data: {e}")
        raise

if __name__ == "__main__":
    input_file = r"..\Data\orders.csv"
    output_file = r"..\Data\cleaned\orders_cleaned.csv"
    
    # Resolve absolute paths based on script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    abs_input = os.path.join(script_dir, input_file)
    abs_output = os.path.join(script_dir, output_file)
    
    logging.info("Starting Orders Data Cleaning Pipeline...")
    clean_orders_dataset(abs_input, abs_output)
    logging.info("Pipeline Execution Complete.")
