import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath,"Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice = filename.split("-")[0]
    dt = filename.split("-")[1]

    pdf.set_font(family="Times", size=12, style="B")

    pdf.cell(w=50, h=18, txt=invoice, border=0, ln=1)
    pdf.cell(w=30, h=16, txt=dt, border=0, ln=1)

    pdf.set_font(family="Times", size=12, style="B")

    pdf.cell(w=30, h=14, txt="Product ID", border=1, align="C")
    pdf.cell(w=30, h=14, txt="Product", border=1, align="C")
    pdf.cell(w=30, h=14, txt="Quantity", border=1, align="C")
    pdf.cell(w=30, h=14, txt="Price", border=1, align="C")
    pdf.cell(w=30, h=14, txt="Total Price", border=1, align="C")

    pdf.ln(14)
    total = 0
    for index, row in df.iterrows():
        for i in range(row.count()):
            if i == 4:
                total = total + row[i]
            pdf.cell(w=30, h=10, txt=str(row[i]), border=1, align="L")
        pdf.ln(10)
    pdf.cell(w=150, h=16, txt=str(total), border=0, align="R")
    pdf.output(f"PDFs/{filename}.pdf")