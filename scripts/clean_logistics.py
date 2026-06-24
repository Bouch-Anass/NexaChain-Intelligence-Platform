import pandas as pd
import numpy as np
import logging
import os
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler('clean_logistics.log')])

def clean_logistics_dataset(input_path: str, output_path: str):
    try:
        logging.info(f"Loading logistics data from {input_path}")
        df = pd.read_csv(input_path)
        
        if 'fuel_cost_usd' in df.columns:
            cap = df['fuel_cost_usd'].quantile(0.99)
            outliers = df['fuel_cost_usd'] > cap
            df.loc[outliers, 'fuel_cost_usd'] = cap
            logging.info(f"Capped {outliers.sum()} fuel_cost_usd outliers to {cap:.2f}.")
            
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        logging.info("Successfully exported cleaned logistics data.")
    except Exception as e:
        logging.error(f"Error: {e}")
        raise

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    clean_logistics_dataset(os.path.join(script_dir, r"..\Data\logistics.csv"), os.path.join(script_dir, r"..\Data\cleaned\logistics_cleaned.csv"))
