import streamlit as st
from fpdf import FPDF
import pandas as pd
from openpyxl import Workbook

#wb = Workbook("10001-2023.1.18.xlsx")

#ws = wb.

pdf = FPDF(orientation="P", unit="mm", format="A4")


st.title("Test Page")

df = pd.read_excel("10001-2023.1.18.xlsx",sheet_name="Sheet 1")
columns = df.columns.size
st.write(columns)
pdf.add_page()

pdf.set_font(family="Times", size=12)
pdf.set_text_color(0, 0, 254)
for index, row in df.iterrows():
    for i in range(columns):

        st.write(row[i])

pdf.output("output.pdf")
st.write(df)