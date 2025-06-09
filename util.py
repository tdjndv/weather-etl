import requests

def get_lat_lon(postal_prefix, country_code, api_key, flag):
    url = f'http://api.openweathermap.org/geo/1.0/zip?zip={postal_prefix},{country_code}&appid={api_key}'
    data = requests.get(url).json()
    if flag:
        print(f"get_lat_lon: {url}")
    return data

def get_weather(info, api_key, flag, format):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={info['lat']}&lon={info['lon']}&appid={api_key}&units={format}"
    data = requests.get(url).json()
    if flag:
        print(f"get_weather: {url}")
    return data

def default_format(data):
    return {"city" : data['name'], "temp" : data['main']['temp'], "weather" : data['weather'][0]['description'], "humidity" : data['main']['humidity'], 'wind' : data['wind']['speed'], "feels like" : data['main']['feels_like']}