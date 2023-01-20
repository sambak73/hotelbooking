import pandas
import streamlit as st
import smtplib,ssl
import pandas as pd
host = "smtp.gmail.com"
port = 465
sender = "sambasivam.k@gmail.com"
password = "xgbswpanmtgyevjf"
receiver = "smbkrishnamurthy@gmail.com"
data = pd.read_csv("topics.csv")
context = ssl.create_default_context()
st.title("Contact Us")
def send_email(email,message):
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(sender,password)
        server.sendmail(email,receiver,message)

with st.form(key="contact_form"):
    topics = []
    email = st.text_input("Your Email","", key="email")
    for index, topic in data.iterrows():
        topics.append(topic["topic"])
    option = st.selectbox("Topic to discuss", topics)
    message = st.text_area("Your Message", "", key="query")
    messages = f"""\
Subject: {option} by {email}

From: {email}
{message}
"""
    submit = st.form_submit_button("Submit")
    if submit:
        send_email(email,messages)
        st.info("Your email was sent successfully")