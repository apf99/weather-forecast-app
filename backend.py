import requests

API_KEY = '88e439962180641942adf1e76064a02d'

def get_data(place, forecast_days=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url)
    content = response.json()
    filtered_content = content['list']
    no_values = 8*forecast_days
    filtered_content = filtered_content[:no_values]
    return filtered_content


if __name__ == '__main__':
    data = get_data('London', 2)
    print(data)
