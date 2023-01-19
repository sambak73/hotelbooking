import streamlit as st
from PIL import Image

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
#st.image("images/20.png")
with open("data.csv", "r") as file:
    data = file.readlines()
col3, col4 = st.columns(2)
for index, title in enumerate(data):
    listitem = title.split(";")
    #st.write(f"{index}.{listitem[1]}")
    #st.write(f"{index} . {title}")

    if index > 0:
        image = listitem[3].strip('\n')
        image = Image.open(f"images/{image}")
        if index % 2 > 0:
            with col3:
                st.title(listitem[0])
                st.write(listitem[1])
                st.image(image)
                st.info(listitem[2])
        if index % 2 == 0:
            with col4:
                st.title(listitem[0])
                st.write(listitem[1])
                st.image(image)
                st.info(listitem[2])