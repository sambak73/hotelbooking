from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")
#print(df["Topic"])

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0, 0, 254)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, align="L", ln=1)
    pdf.line(10,20,200,20)

    pdf.ln(246)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(w=0, h=8, txt=row["Topic"], border=0, align="R")

    for i in range(row["Pages"]-1):
        pdf.add_page()
pdf.output("output.pdf")