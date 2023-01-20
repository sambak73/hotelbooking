import smtplib
import ssl

host = "smtp.gmail.com"
port = 465
username = "sambasivam.k@gmail.com"
password = "xgbswpanmtgyevjf"
receiver = "smbkrishnamurthy@gmail.com"
message = "Hello"
context = ssl.create_default_context()

with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)