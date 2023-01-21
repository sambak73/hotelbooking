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
    #invoice = filename.split("-")[0]
    #dt = filename.split("-")[1]
    invoice, dt = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice #: {invoice}", border=0, ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=30, h=8, txt=f"Invoice date: {dt}", border=0, ln=1)

    pdf.set_font(family="Times", size=12, style="B")

    #pdf.cell(w=30, h=14, txt="Product ID", border=1, align="C")
    #pdf.cell(w=30, h=14, txt="Product", border=1, align="C")
    #pdf.cell(w=30, h=14, txt="Quantity", border=1, align="C")
    #pdf.cell(w=30, h=14, txt="Price", border=1, align="C")
    #pdf.cell(w=30, h=14, txt="Total Price", border=1, align="C")

    columns = df.columns
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.cell(w=30, h=14, txt=columns[0], border=1, align="C")
    pdf.cell(w=70, h=14, txt=columns[1], border=1, align="C")
    pdf.cell(w=40, h=14, txt=columns[2], border=1, align="C")
    pdf.cell(w=30, h=14, txt=columns[3], border=1, align="C")
    pdf.cell(w=20, h=14, txt=columns[4], border=1, align="C", ln=1)

    #pdf.ln(14)
    total = 0
    for index, row in df.iterrows():
        total = total + row["total_price"]
        pdf.cell(w=30, h=14, txt=str(row["product_id"]), border=1, align="C")
        pdf.cell(w=70, h=14, txt=str(row["product_name"]), border=1, align="C")
        pdf.cell(w=40, h=14, txt=str(row["amount_purchased"]), border=1, align="C")
        pdf.cell(w=30, h=14, txt=str(row["price_per_unit"]), border=1, align="C")
        pdf.cell(w=20, h=14, txt=str(row["total_price"]), border=1, align="C", ln=1)
        #for i in range(row.count()):
        #    if i == 4:
        #        total = total + row[i]
        #    pdf.cell(w=len(str(row[i-1]))+len(str(row[i]))+20, h=10, txt=str(row[i]), border=1, align="L")
        #pdf.ln(10)
    pdf.cell(w=185, h=16, txt=str(total), border=0, align="R")
    pdf.output(f"PDFs/{filename}.pdf")