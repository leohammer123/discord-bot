import os
import requests
import json


def get_weather(city):
  url ="""http://api.weatherstack.com/current?access_key="""+os.getenv('weather token').replace('\n','')+"""&query="""+city
  r = requests.get(url.replace('\n',''))
  r = json.loads(r.text)
  try:
    temp =r['current']['temperature']
    humid = r['current']['humidity']
    des = r['current']['weather_descriptions']
    wind_speed = r['current']['wind_speed']
  except KeyError as err:
    return 'error occured : '+ str(err)
  output = 'city : '+str(city)+'\n'+'tempature : '+str(temp)+'\n'+'weather_descriptions : '+str(des)[2:-2]+'\n'+'wind speed : '+str(wind_speed)+'\n'+'humidity : '+str(humid)+'\n'
  return output