import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import os

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'NexaChain Intelligence Platform - Cash Flow Analysis', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
        
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)
        
    def add_plot(self, image_path):
        self.image(image_path, w=170)
        self.ln()

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cleaned_dir = os.path.join(script_dir, r"..\Data\cleaned")
    reports_dir = os.path.join(script_dir, r"..\Reports\financial_analysis")
    img_dir = os.path.join(reports_dir, "images")
    os.makedirs(img_dir, exist_ok=True)
    
    pdf = PDFReport()
    pdf.add_page()
    
    # Task 6: Cash Flow Pattern Analysis
    pdf.chapter_title('Task 6: Cash Flow Pattern Analysis')
    
    financials = pd.read_csv(os.path.join(cleaned_dir, 'financials_cleaned.csv'))
    orders = pd.read_csv(os.path.join(cleaned_dir, 'orders_cleaned.csv'))
    
    # Merge for dates
    if 'order_date' in orders.columns:
        orders['order_date'] = pd.to_datetime(orders['order_date'])
        fin = pd.merge(financials, orders[['order_id', 'order_date']], on='order_id', how='inner')
        fin = fin.sort_values(by='order_date')
        
        # Monthly Aggregation
        fin['Month'] = fin['order_date'].dt.to_period('M').astype(str)
        monthly_gp = fin.groupby('Month')['gross_profit_usd'].sum().reset_index()
        
        plt.figure(figsize=(10, 5))
        sns.lineplot(x='Month', y='gross_profit_usd', data=monthly_gp, marker='o', color='green')
        plt.title('Monthly Gross Profit (Cash Flow Trend)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        img_path = os.path.join(img_dir, "cash_flow_monthly.png")
        plt.savefig(img_path)
        plt.close()
        pdf.add_plot(img_path)
        
        # Working Capital Ratio over time (Rolling)
        fin['WC_Rolling'] = fin['working_capital_ratio'].rolling(window=30, min_periods=1).mean()
        plt.figure(figsize=(10, 5))
        sns.lineplot(x='order_date', y='WC_Rolling', data=fin, color='purple')
        plt.title('30-Day Rolling Working Capital Ratio')
        plt.tight_layout()
        img_path = os.path.join(img_dir, "wc_rolling.png")
        plt.savefig(img_path)
        plt.close()
        pdf.add_plot(img_path)
        
    pdf.output(os.path.join(reports_dir, 'cash_flow_analysis.pdf'))
    print("Cash Flow PDF generated successfully.")

if __name__ == "__main__":
    main()
