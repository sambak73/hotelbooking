import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.title("The Best Company")
content = """
This is simplified sample website for the Best Company.
We list the team below.
"""
st.write(content)
st.header("Our Team")
data = pd.read_csv("data .csv",sep=",")

col1,emptycol1,col2,emptycol2,col3 = st.columns([1,.5,1,.5,1])

for index, row in data[:4].iterrows():
    with col1:
        name = row["first name"].title() + "  " + row["last name"].title()
        st.subheader(name)
        st.write(row["role"])
        st.image("images/" + row['image'])

for index, row in data[4:8].iterrows():
    with col2:
        name = row["first name"].title() + "  " + row["last name"].title()
        st.subheader(name)
        st.write(row["role"])
        st.image(f"images/{row['image']}")

for index, row in data[8:].iterrows():
    with col3:
        name = row["first name"].title() + "  " + row["last name"].title()
        st.subheader(name)
        st.write(row["role"])
        st.image("images/" + row["image"])