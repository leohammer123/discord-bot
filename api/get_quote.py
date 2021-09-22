import requests
import json


def get_quote():
  r = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(r.text)
  quote = json_data[0]['q']+'-'+json_data[0]['a']
  return quote