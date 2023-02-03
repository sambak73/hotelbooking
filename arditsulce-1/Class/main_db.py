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

class Event():

    def scrap(self, url):
        r = requests.get(url)
        data = r.text
        return data

    def extract(self, data):

        extractor = Extractor.from_yaml_file('1.yaml')
        value = extractor.extract(data)['tours']
        return value

class Db():

    def __init__(self, DBPath):
        self.connection = sqlite3.connect(DBPath)
        self.cursor = self.connection.cursor()

    def writedata(self, value):
        rows = value.split(',')
        row = [item.strip() for item in rows]
        self.cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
        self.connection.commit()

    def readdata(self, value):
        rows = value.split(',')
        row = [item.strip() for item in rows]
        name, city, date = row
        self.cursor.execute("SELECT * FROM events WHERE name Like ?", (name,))
        result = self.cursor.fetchall()
        return result

class Email():
    def send(self, message):
        #message = self.message
        with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, message)

if __name__ == '__main__':

    while True:
        event = Event()
        data = event.scrap(url)
        returned_data = event.extract(data)
        print(returned_data)
        if returned_data != 'No upcoming tours':
            db = Db('webscrapping.db')
            existing_data = db.readdata(returned_data)
            if not existing_data:
                db.writedata(returned_data)
                email = Email()
                email.send(message='New Event added')
        time.sleep(2)
