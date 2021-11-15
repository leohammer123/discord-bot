import os
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


def screenshot(url:str)->str:
  try:
    url = """https://api.browshot.com/api/v1/screenshot/create?key=V2ZByU9a7YOqGbsaJ54rsa21IgrpG5l&instance_id=26&url="""+url+"""&size=page&hide_popups=0&dark=0"""
    r = requests.get(url)
    return(r.code)
  except Exception as e:
    return("error : "+ str(e))

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