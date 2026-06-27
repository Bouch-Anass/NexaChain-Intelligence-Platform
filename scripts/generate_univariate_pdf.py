import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import os

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'NexaChain Intelligence Platform - Univariate Analysis', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
        
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, text):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 6, text)
        self.ln()
        
    def add_plot(self, image_path):
        self.image(image_path, w=170)
        self.ln()

def analyze_variable(df, col, title, pdf, output_dir):
    data = df[col].dropna()
    if len(data) == 0: return
    
    # Calculate stats
    stats = {
        'Count': len(data),
        'Mean': data.mean(),
        'Median': data.median(),
        'Min': data.min(),
        'Max': data.max(),
        'Std Dev': data.std(),
        'Skewness': data.skew(),
        'Kurtosis': data.kurt()
    }
    
    # Text
    pdf.chapter_title(title)
    stats_text = "\n".join([f"{k}: {v:,.2f}" if isinstance(v, float) else f"{k}: {v:,}" for k, v in stats.items()])
    pdf.chapter_body(stats_text)
    
    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    sns.histplot(data, kde=True, ax=axes[0], color='skyblue')
    axes[0].set_title(f'{col} - Histogram & Density')
    
    sns.boxplot(x=data, ax=axes[1], color='lightgreen')
    axes[1].set_title(f'{col} - Box Plot')
    
    plt.tight_layout()
    img_path = os.path.join(output_dir, f"{col}_plot.png")
    plt.savefig(img_path)
    plt.close()
    
    pdf.add_plot(img_path)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cleaned_dir = os.path.join(script_dir, r"..\Data\cleaned")
    reports_dir = os.path.join(script_dir, r"..\Reports\statistical_analysis")
    img_dir = os.path.join(reports_dir, "images")
    os.makedirs(img_dir, exist_ok=True)
    
    pdf = PDFReport()
    pdf.add_page()
    
    # Orders
    orders = pd.read_csv(os.path.join(cleaned_dir, 'orders_cleaned.csv'))
    analyze_variable(orders, 'order_value_usd', 'Orders: Order Value (USD)', pdf, img_dir)
    
    # Logistics
    logistics = pd.read_csv(os.path.join(cleaned_dir, 'logistics_cleaned.csv'))
    analyze_variable(logistics, 'delivery_delay_days', 'Logistics: Delivery Delay Days', pdf, img_dir)
    
    # Inventory
    inventory = pd.read_csv(os.path.join(cleaned_dir, 'inventory_cleaned.csv'))
    analyze_variable(inventory, 'stock_on_hand', 'Inventory: Stock on Hand', pdf, img_dir)
    
    # Vendors
    vendors = pd.read_csv(os.path.join(cleaned_dir, 'vendors_cleaned.csv'))
    analyze_variable(vendors, 'vris_score', 'Vendors: Vendor Risk Intelligence Score (VRIS)', pdf, img_dir)
    
    # Financials
    financials = pd.read_csv(os.path.join(cleaned_dir, 'financials_cleaned.csv'))
    analyze_variable(financials, 'working_capital_ratio', 'Financials: Working Capital Ratio', pdf, img_dir)
    analyze_variable(financials, 'gross_profit_usd', 'Financials: Gross Profit (USD)', pdf, img_dir)
    
    # Save PDF
    pdf.output(os.path.join(reports_dir, 'univariate_analysis.pdf'))
    print("Univariate PDF generated successfully.")

if __name__ == "__main__":
    main()
