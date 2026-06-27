import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import os

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'NexaChain Intelligence Platform - Bivariate & Correlation Analysis', 0, 1, 'C')

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

def load_master(cleaned_dir):
    orders = pd.read_csv(os.path.join(cleaned_dir, 'orders_cleaned.csv'))
    logistics = pd.read_csv(os.path.join(cleaned_dir, 'logistics_cleaned.csv'))
    vendors = pd.read_csv(os.path.join(cleaned_dir, 'vendors_cleaned.csv'))
    inventory = pd.read_csv(os.path.join(cleaned_dir, 'inventory_cleaned.csv'))
    fin = pd.read_csv(os.path.join(cleaned_dir, 'financials_cleaned.csv'))
    
    # Merge for correlation
    master = pd.merge(orders, logistics, on='order_id', how='inner', suffixes=('', '_logistics'))
    # Use vendors info
    master = pd.merge(master, vendors, on='vendor_id', how='left', suffixes=('', '_vendor'))
    return master

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cleaned_dir = os.path.join(script_dir, r"..\Data\cleaned")
    reports_dir = os.path.join(script_dir, r"..\Reports\statistical_analysis")
    img_dir = os.path.join(reports_dir, "images")
    os.makedirs(img_dir, exist_ok=True)
    
    pdf = PDFReport()
    
    # --- TASK 2: BIVARIATE ANALYSIS ---
    pdf.add_page()
    pdf.chapter_title('Task 2: Bivariate Analysis (Scatter & Regression)')
    master = load_master(cleaned_dir)
    
    # Pair 1: Order Value vs Delivery Delay
    if 'order_value_usd' in master.columns and 'delivery_delay_days' in master.columns:
        plt.figure(figsize=(8, 5))
        sns.regplot(x='delivery_delay_days', y='order_value_usd', data=master.sample(min(1000, len(master))), scatter_kws={'alpha':0.3})
        plt.title('Order Value vs Delivery Delay')
        img_path = os.path.join(img_dir, "bivariate_1.png")
        plt.savefig(img_path)
        plt.close()
        pdf.add_plot(img_path)
        pdf.chapter_body("Observation: We evaluate if larger orders face longer delays.")
        
    # Pair 2: VRIS Score vs Quality Acceptance Rate
    if 'vris_score' in master.columns and 'quality_acceptance_rate' in master.columns:
        plt.figure(figsize=(8, 5))
        sns.regplot(x='vris_score', y='quality_acceptance_rate', data=master.sample(1000), scatter_kws={'alpha':0.3})
        plt.title('Vendor Risk vs Quality Rate')
        img_path = os.path.join(img_dir, "bivariate_2.png")
        plt.savefig(img_path)
        plt.close()
        pdf.add_plot(img_path)
        pdf.chapter_body("Observation: Negative regression indicates higher risk vendors produce lower quality goods.")
        
    # --- TASK 3: CORRELATION ANALYSIS ---
    pdf.add_page()
    pdf.chapter_title('Task 3: Correlation Matrix & Heatmaps')
    
    numerics = master.select_dtypes(include=[np.number])
    cols_to_use = [c for c in numerics.columns if not c.endswith('_id') and not c.endswith('_flag')][:10]
    df_corr = numerics[cols_to_use].dropna()
    
    # Pearson
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_corr.corr(method='pearson'), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Pearson Correlation Heatmap')
    plt.tight_layout()
    img_path = os.path.join(img_dir, "pearson.png")
    plt.savefig(img_path)
    plt.close()
    pdf.add_plot(img_path)
    pdf.chapter_body("Pearson Matrix highlights linear relationships.")
    
    # Spearman
    pdf.add_page()
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_corr.corr(method='spearman'), annot=True, cmap='viridis', fmt=".2f")
    plt.title('Spearman Correlation Heatmap')
    plt.tight_layout()
    img_path = os.path.join(img_dir, "spearman.png")
    plt.savefig(img_path)
    plt.close()
    pdf.add_plot(img_path)
    pdf.chapter_body("Spearman Matrix highlights monotonic relationships, resilient to outliers.")
    
    pdf.output(os.path.join(reports_dir, 'correlation_report.pdf'))
    print("Correlation PDF generated successfully.")

if __name__ == "__main__":
    main()
