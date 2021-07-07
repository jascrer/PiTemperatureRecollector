import requests
from requests import api

CACHI_LOCATION= {
    "lat":9.8293,
    "lon":-83.7941,
    "zip":"30204,cr"
}

def get_current_weather():
    '''
    Retrieves and displays an object with the complete weather object
    '''
    api = OpenWeatherApi()
    response = requests.get(api.api_url)
    if response.status_code != 200:
        raise Exception(f'Error {response.status_code}')
    print(f'{response.json()}')
    return response.json()

class OpenWeatherApi:
    def __init__(self):
        self.app_id=''
        self.api_url = (f'https://api.openweathermap.org/data/2.5/weather?zip={CACHI_LOCATION["zip"]}&appid={self.app_id}')
        self.weather_dict = dict()

    def request_to_api(self):
        '''
        Creates the request to the API to retrieve the weather information
        '''
        response_weather = requests.get(self.api_url)
        if response_weather.status_code != 200:
            raise Exception(f'Error - Error Code:{response_weather.status_code} - Message: {response_weather.text}')
        return response_weather.json()
    
    def refresh_weather(self):
        '''
        Refreshes the weather dictionary with the api
        '''
        self.weather_dict = self.request_to_api()

    def get_temperatures(self):
        '''
        Returns the temperatures recorded in the weather dictionary
        '''
        temperature = round(self.weather_dict['main']['temp']-273.5,2)
        feels_like = round(self.weather_dict['main']['feels_like']-273.5,2)
        return (temperature, feels_like)
    
    def get_humidity(self):
        '''
        Returns the humidity recorded in the weather dictionary
        '''
        return self.weather_dict['main']['humidity']

# Example of how to use the class to get temperatures
api_object = OpenWeatherApi()
api_object.refresh_weather()
(temperature, feels_like) = api_object.get_temperatures()
print(f'Temperature = {temperature}|Feels Like = {feels_like}')
humidity = api_object.get_humidity()
print(f'Humidity= {humidity}')
# Gets all the weather object
#get_current_weather()