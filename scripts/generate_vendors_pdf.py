import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import os

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'NexaChain Intelligence Platform - Vendor Risk Segmentation', 0, 1, 'C')

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

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cleaned_dir = os.path.join(script_dir, r"..\Data\cleaned")
    reports_dir = os.path.join(script_dir, r"..\Reports\statistical_analysis")
    img_dir = os.path.join(reports_dir, "images")
    os.makedirs(img_dir, exist_ok=True)
    
    pdf = PDFReport()
    pdf.add_page()
    
    # Task 5: Vendor Risk Segmentation
    pdf.chapter_title('Task 5: Vendor Risk Segmentation')
    
    vendors = pd.read_csv(os.path.join(cleaned_dir, 'vendors_cleaned.csv'))
    
    # Tiering based on VRIS Score
    vendors['Risk_Tier'] = pd.cut(vendors['vris_score'], bins=[-1, 30, 70, 90, 100], labels=['Low', 'Medium', 'High', 'Critical'])
    summary = vendors['Risk_Tier'].value_counts().sort_index()
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x=summary.index, y=summary.values, palette='Reds')
    plt.title('Vendor Distribution by Risk Tier')
    plt.ylabel('Number of Vendors')
    plt.tight_layout()
    img_path = os.path.join(img_dir, "vendor_tiers.png")
    plt.savefig(img_path)
    plt.close()
    pdf.add_plot(img_path)
    
    pdf.chapter_body(f"Critical Risk Vendors detected: {summary.get('Critical', 0)}")
    pdf.chapter_body(f"High Risk Vendors detected: {summary.get('High', 0)}")
    pdf.chapter_body("Recommendation: Procurement should prepare backup suppliers immediately for Critical and High-Risk tiers.")
        
    pdf.output(os.path.join(reports_dir, 'vendor_risk_analysis.pdf'))
    print("Vendor Risk PDF generated successfully.")

if __name__ == "__main__":
    main()
