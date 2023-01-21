import pandas as pd
from fpdf import FPDF
from pathlib import Path
import glob

filenames = glob.glob("animals/*.txt")

for file in filenames:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
#    df = pd.read_csv(file)
#    print(df)
    f = Path(file).stem
    f = f.title()
    with open(file, "r") as fil:
        data = fil.read()
        #print(f"{file} data is {data}")
#    for index, row in df.iterrows():
        pdf.add_page()
        pdf.set_text_color(0, 0, 254)
        pdf.set_font(family="Times", size=18, style="B")
        pdf.cell(w=0, h=14, txt=f, align="L", ln=1)
        pdf.set_text_color(100, 100, 100)
        pdf.set_font(family="Times", size=14, style="I")
        pdf.multi_cell(w=0, h=12, txt=data, align="L")
        pdf.output(f"animals-PDFs/{f}.pdf")



