import requests
from selectorlib import Extractor
import datetime
import smtplib, ssl

url = 'http://programmer100.pythonanywhere.com'

def scrap(url):
    r = requests.get(url)
    data = r.text
    return data

def extract(data):
    extract = Extractor.from_yaml_file('temp.yaml')
    extracted_value = extract.extract(data)['home']
    return extracted_value
returned_data = scrap(url)
print(extract(returned_data))