import requests

API_KEY = '9854f92d1f014ab47ac058cccb519e25'
place = 'Tokyo'

def get_value(place, days):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    req = requests.get(url)
    data = req.json()
    filtered_data = data['list']
    nr_of_days_values = 8 * days
    filtered_data = filtered_data[:nr_of_days_values]
    return filtered_data
if __name__ == '__main__':
    get_value('Tokyos', 3, 'Sky')