import requests
import json

# url_api = "https://www.metaweather.com/api/location/search/?lattlong=35.6892,51.3890"
# response = requests.get(url_api)

# city_info = response.json()

# f = open("C:/Users/markazi/Desktop/city_info.json", "w+")
# json.dump(city_info, f)

city_id = "2251945"
url_api = "https://www.metaweather.com/api/location/"+ city_id +"/"
response = requests.get(url_api)
weather_info = response.json()

# f = open("C:/Users/markazi/Desktop/weather_info.json", "a+")
# json.dump(weather_info, f)

print("----------\nTimeZone : %s\nWeather : %s\n----------" %(weather_info['timezone'],weather_info['consolidated_weather'][0]['weather_state_name']))