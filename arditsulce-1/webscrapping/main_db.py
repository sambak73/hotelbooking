import time
import sqlite3
import requests
from selectorlib import Extractor
import smtplib, ssl
import datetime

url = 'http://programmer100.pythonanywhere.com/tours/'
sender = 'sambasivam.k@gmail.com'
password = 'wqvvlrytjfcwyvto'
receiver = 'smbkrishnamurthy@gmail.com'
context = ssl.create_default_context()
host = 'smtp.gmail.com'
port = 465


def scrap(url):
    r = requests.get(url)
    data = r.text
    return data


def extract(data):

    extractor = Extractor.from_yaml_file('1.yaml')
    value = extractor.extract(data)['tours']
    return value


def writedata(value):
    rows = value.split(',')
    row = [item.strip() for item in rows]
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    connection.commit()
def readdata(value):
    rows = value.split(',')
    row = [item.strip() for item in rows]
    name, city, date = row
    cursor.execute("SELECT * FROM events WHERE name Like ?", (name,))
    result = cursor.fetchall()
    return str(result)
def send_email():
    message = 'Subject:Music event'\
'New Event added'
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)

if __name__ == '__main__':
    connection = sqlite3.connect('webscrapping.db')
    cursor = connection.cursor()

    while True:
        data = scrap(url)
        returned_data = extract(data)
        print(returned_data)
        if returned_data != 'No upcoming tours':
            existing_data = readdata(returned_data)
            if not existing_data:
                writedata(returned_data)
                send_email()
        time.sleep(2)
