import requests
import json


def factordb(n):
  result = []
  status = 'Fail'
  n  = requests.get('http://factordb.com/api?query='+str(n))
  r = json.loads(n.text)
  if r['status'] == 'FF':
    result.append('Success')
    result.append(r['factors'])
  else:
    result.append(status)
  

  return result

  