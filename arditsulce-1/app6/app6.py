import smtplib, ssl
import requests
import os

api = 'db53b7c8aacc4b89a4dd7934f08e9158'

url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-12-23&sortBy=publishedAt&apiKey=db53b7c8aacc4b89a4dd7934f08e9158&language=en' #&pageSize=20'
r = requests.request('GET',url)
data = r.json()

host = 'smtp.gmail.com'
port = 465
sender = 'sambasivam.k@gmail.com'
password = os.environ['EPASSWORD']
receiver = 'smbkrishnamurthy@gmail.com'
context = ssl.create_default_context()
body = "Subject: Today's News" + "\n"
for article in data['articles'][0:20]:
    #body.append([article['title'],article['description'],article['url']])
    title = article['title'].title()
    if title is not None and article['description'] is not None:
        body = body + f"{title} \n {article['description']} \n {article['url']} \n \n"
    #print(type(body))
    print(body)
    #print(body[0][1])
with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
    server.login(sender, password)
    body = body.encode('utf-8')
    server.sendmail(sender, receiver, body)
