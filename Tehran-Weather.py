import requests
import json

city_id = "2251945"
url_api = "https://www.metaweather.com/api/location/"+ city_id +"/"
response = requests.get(url_api)
weather_info = response.json()

print("----------\nTimeZone : %s\nWeather : %s\n----------" %(weather_info['timezone'],weather_info['consolidated_weather'][0]['weather_state_name']))
