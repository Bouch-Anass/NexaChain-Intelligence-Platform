import pandas as pd
import numpy as np
import logging
import os
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler('clean_financials.log')])

def clean_financials_dataset(input_path: str, output_path: str):
    try:
        logging.info(f"Loading financials data from {input_path}")
        df = pd.read_csv(input_path)
        
        # Deduplicate
        initial_len = len(df)
        df = df.drop_duplicates()
        logging.info(f"Removed {initial_len - len(df)} duplicate records.")
        
        # Missing values
        if 'working_capital_ratio' in df.columns:
            m = df['working_capital_ratio'].isnull().sum()
            df['working_capital_ratio'] = df['working_capital_ratio'].fillna(df['working_capital_ratio'].median())
            logging.info(f"Imputed {m} missing working_capital_ratio.")
            
        if 'financial_risk_score' in df.columns:
            m = df['financial_risk_score'].isnull().sum()
            df['financial_risk_score'] = df['financial_risk_score'].fillna(df['financial_risk_score'].median())
            logging.info(f"Imputed {m} missing financial_risk_score.")
            
        # Invalid / Negative Margins
        if 'gross_profit_usd' in df.columns:
            neg = (df['gross_profit_usd'] < 0).sum()
            df['is_loss_order'] = (df['gross_profit_usd'] < 0).astype(int)
            logging.info(f"Flagged {neg} negative gross_profit_usd records as loss orders.")
            
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        logging.info("Successfully exported cleaned financials data.")
    except Exception as e:
        logging.error(f"Error: {e}")
        raise

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    clean_financials_dataset(os.path.join(script_dir, r"..\Data\financials.csv"), os.path.join(script_dir, r"..\Data\cleaned\financials_cleaned.csv"))
