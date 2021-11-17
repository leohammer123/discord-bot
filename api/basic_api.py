import io
import os
from types import resolve_bases
from typing import Tuple
import requests
import json


def get_quote()->str:
  try:
    r = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(r.text)
    quote = json_data[0]['q']+'-'+json_data[0]['a']
    return quote
  except Exception as e:
    return "error : "+str(e)


def screenshot(url:str)->bytes:
  try:
    url_1 = f'http://api.screenshotlayer.com/api/capture?access_key=4be0203452a15afba12ba1224744dee8&url={url}&viewport=1440x900&width=250'
    res = requests.get(url_1,stream=True)
    data = io.BytesIO(res.content) # Transfer bytes to fp
  except Exception as e:
    return str(e)
  return data
  
def shorturl(url:str)->str:
  re_url = 'https://api.shrtco.de/v2/shorten?url='+ url
  r = json.loads(requests.get(re_url).text)
  status = r['ok']
  link1=r['result']['full_short_link']
  link2 = r['result']['full_short_link2']
  link3 = r['result']['full_short_link3']
  org = r['result']['original_link']
  final = 'ok : '+str(status)+'\n'+'Original link : '+org +'\n'+'link1 : '+str(link1)+'\n'+'link2 : '+str(link2)+'\n'+'link3 : '+str(link3)+'\n'
  return final


def get_weather(city :str)->str:
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

def release_challenge()->str:
    r = requests.get('https://imaginaryctf.org/api/challenges/released')
    r = json.loads(r.text)
    text = "   title     category      points\n"
    index = 1
    for a in r:
        text += f'{index}  {a["title"]}  {a["category"]}  {a["points"]}\n'
        index += 1
    return text
  
def RandomUser()->Tuple:
  res = requests.get('https://randomuser.me/api/')
  a = json.loads(res.text)
  text = f'Hi my name is {a["results"][0]["name"]["first"]} {a["results"][0]["name"]["last"]}'
  text += f'. I am a {a["results"][0]["gender"]},and I live in {a["results"][0]["location"]["country"]} {a["results"][0]["location"]["state"]} {a["results"][0]["location"]["city"]}.'
  text += f'\nThis is my photo uwu'
  print(text)
  url = a["results"][0]['picture']['large']
  pic = requests.get(url)
  n = io.BytesIO(pic.content) 
  return text,n
    
def Catfact()->str:
  r = requests.get('https://catfact.ninja/fact')
  js = json.loads(r.text)
  return "Cat fact : "+js['fact']

def Dogpic()->bytes:
  r = requests.get('https://dog.ceo/api/breeds/image/random',stream=True)
  pic = io.BytesIO(r.content)
  return pic

def my_ip()->str:
  res = requests.get('https://api.ipify.org/?format=json')
  res = json.loads(res.text)
  return "My id address is "+res["ip"] + " Please hack me"

def rand_activity()->str:
  res = requests.get('https://www.boredapi.com/api/activity')
  res = json.loads(res.text)
  return res["activity"]