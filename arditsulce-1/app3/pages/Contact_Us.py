import streamlit as st
import smtplib,ssl
host = "smtp.gmail.com"
port = 465
sender = "sambasivam.k@gmail.com"
password = "xgbswpanmtgyevjf"
receiver = "smbkrishnamurthy@gmail.com"

context = ssl.create_default_context()
st.title("Contact Us")
def send_email(email,message):
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(sender,password)
        server.sendmail(email,receiver,message)

with st.form(key="contact_form"):
    email = st.text_input("Your Email","", key="email")
    message = st.text_area("Your Message","", key="query")
    messages = f"""\
    Subject: New email from {email}
    {message}
    """
    submit = st.form_submit_button("Submit")
    if submit:
        send_email(email,messages)
        st.info("Your email was sent successfully")