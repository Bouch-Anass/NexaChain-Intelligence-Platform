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
        logging.FileHandler('clean_inventory.log')
    ]
)

def load_data(file_path: str) -> pd.DataFrame:
    try:
        logging.info(f"Loading data from {file_path}")
        df = pd.read_csv(file_path)
        logging.info(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        raise

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    if 'reorder_point' in df.columns:
        missing_rp = df['reorder_point'].isnull().sum()
        df['reorder_point'] = df['reorder_point'].fillna(df['reorder_point'].median())
        logging.info(f"Imputed {missing_rp} missing reorder_point values with median.")
        
    if 'vendor_lead_time_days' in df.columns:
        missing_lt = df['vendor_lead_time_days'].isnull().sum()
        df['vendor_lead_time_days'] = df['vendor_lead_time_days'].fillna(df['vendor_lead_time_days'].median())
        logging.info(f"Imputed {missing_lt} missing vendor_lead_time_days values with median.")
    return df

def handle_invalid_stock(df: pd.DataFrame) -> pd.DataFrame:
    if 'stock_on_hand' in df.columns:
        negative_mask = df['stock_on_hand'] < 0
        invalid_count = negative_mask.sum()
        df['stock_error_flag'] = negative_mask.astype(int)
        df.loc[negative_mask, 'stock_on_hand'] = 0
        logging.info(f"Set {invalid_count} negative stock_on_hand values to 0 and flagged as errors.")
    return df

def clean_inventory_dataset(input_path: str, output_path: str):
    df = load_data(input_path)
    df = handle_missing_values(df)
    df = handle_invalid_stock(df)
    
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        logging.info(f"Successfully exported cleaned data to {output_path}")
    except Exception as e:
        logging.error(f"Failed to export data: {e}")
        raise

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    abs_input = os.path.join(script_dir, r"..\Data\inventory.csv")
    abs_output = os.path.join(script_dir, r"..\Data\cleaned\inventory_cleaned.csv")
    
    logging.info("Starting Inventory Data Cleaning Pipeline...")
    clean_inventory_dataset(abs_input, abs_output)
    logging.info("Pipeline Execution Complete.")
