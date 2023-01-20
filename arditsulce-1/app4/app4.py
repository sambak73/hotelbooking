from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")
#print(df["Topic"])

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, align="L", ln=1)
    pdf.line(10,20,200,20)



pdf.output("output.pdf")