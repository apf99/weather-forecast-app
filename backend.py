import requests

API_KEY = '88e439962180641942adf1e76064a02d'

def get_data(place, forecast_days=None, kind=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url)
    content = response.json()
    filtered_content = content['list']
    no_values = 8*forecast_days
    filtered_content = filtered_content[:no_values]
    if kind == 'Temperature':
        filtered_content = [item['main']['temp'] for item in filtered_content]
    elif kind == 'Sky':
        filtered_content = [item['weather'][0]['main'] for item in filtered_content]
    return filtered_content


if __name__ == '__main__':
    data = get_data('London', 2, 'Sky')
    print(data)
