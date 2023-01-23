import streamlit as st
import requests
from datetime import datetime

date = datetime.now().date()
#print(date)
api = 'AcUFpMgUIcd6cSZZHlsAIcDOeE0fuilrYHfasI04'
url = 'https://api.nasa.gov/planetary/apod?api_key=AcUFpMgUIcd6cSZZHlsAIcDOeE0fuilrYHfasI04'\
      f'&date={date}'
#print(url)
request = requests.request('GET',url)
data = request.json()
img_url = data['url']
#print(img_url)
#print(data['explanation'])
img_req = requests.request('GET',img_url)
img_data = img_req.content
with open('galaxy.jpg', 'wb') as file:
    file.write(img_data)

st.set_page_config("Daily Galaxy Pic from NASA")

st.image('galaxy.jpg')
st.write(data['explanation'])
