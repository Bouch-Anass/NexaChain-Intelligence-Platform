import pandas as pd
import numpy as np
import logging
import os
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler('clean_vendors.log')])

def clean_vendors_dataset(input_path: str, output_path: str):
    try:
        logging.info(f"Loading vendors data from {input_path}")
        df = pd.read_csv(input_path)
        
        if 'financial_stability_score' in df.columns:
            m = df['financial_stability_score'].isnull().sum()
            df['financial_stability_score'] = df['financial_stability_score'].fillna(df['financial_stability_score'].median())
            logging.info(f"Imputed {m} missing financial_stability_score.")
            
        if 'quality_acceptance_rate' in df.columns:
            m = df['quality_acceptance_rate'].isnull().sum()
            df['quality_acceptance_rate'] = df['quality_acceptance_rate'].fillna(df['quality_acceptance_rate'].median())
            logging.info(f"Imputed {m} missing quality_acceptance_rate.")
            
        if 'vris_score' in df.columns:
            m = df['vris_score'].isnull().sum()
            df['vris_score'] = df['vris_score'].fillna(df['vris_score'].median())
            logging.info(f"Imputed {m} missing vris_score.")
            
        if 'days_payable_outstanding' in df.columns:
            invalid_mask = df['days_payable_outstanding'] < 0
            df.loc[invalid_mask, 'days_payable_outstanding'] = 0
            logging.info(f"Set {invalid_mask.sum()} negative days_payable_outstanding to 0.")
            
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        logging.info("Successfully exported cleaned vendors data.")
    except Exception as e:
        logging.error(f"Error: {e}")
        raise

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    clean_vendors_dataset(os.path.join(script_dir, r"..\Data\vendors.csv"), os.path.join(script_dir, r"..\Data\cleaned\vendors_cleaned.csv"))
