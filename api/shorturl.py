import json
import requests

def shorturl(url):
  re_url = 'https://api.shrtco.de/v2/shorten?url='+ url
  r = json.loads(requests.get(re_url).text)
  status = r['ok']
  link1=r['result']['full_short_link']
  link2 = r['result']['full_short_link2']
  link3 = r['result']['full_short_link3']
  org = r['result']['original_link']
  final = 'ok : '+str(status)+'\n'+'Original link : '+org +'\n'+'link1 : '+str(link1)+'\n'+'link2 : '+str(link2)+'\n'+'link3 : '+str(link3)+'\n'
  return final