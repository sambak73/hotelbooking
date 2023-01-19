import streamlit as st
import pandas as pd

#st.set_page_config(layout="wide")

st.title("My Portfolio")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Nature-PNG-Image.png")
with col2:
    content = """
    This is the profile page of myself.
    I'm trying python programming using to create web application using streamlit framework.
    The page is introduction of myself and my interests in the field of Information Technology
    This is just a start to the complete profile page
    """
    st.title("Samba Krishnamurthy")
    st.info(content)
    content2 = """
    Following are list of applications created using python. There is also link to source code.
    """
st.write(content2)
data = pd.read_csv('data.csv',sep=";")
col3, col4 = st.columns(2)
for index, row in data[:10].iterrows():
    #st.write(row["title"])
    with col3:
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write(row["url"])

for index, row in data[10:].iterrows():
    with col4:
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write(row["url"])