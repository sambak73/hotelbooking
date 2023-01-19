import streamlit as st

st.set_page_config(layout="wide")

st.title("My Portfolio")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")
with col2:
    content = """
    This is the profile page of myself.
    I'm trying python programming using to create web application using streamlit framework.
    The page is introduction of myself and my interests in the field of Information Technology
    This is just a start to the complete profile page
    """
    st.info(content)
    content2 = """
    Following are list of applications created using python. There is also link to source code.
    """
st.write(content2)