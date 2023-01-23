import smtplib
import requests

api = 'db53b7c8aacc4b89a4dd7934f08e9158'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-12-23&sortBy=publishedAt&apiKey=db53b7c8aacc4b89a4dd7934f08e9158'

r = requests.request('GET',url)
data = r.json()
for article in data['articles']:
