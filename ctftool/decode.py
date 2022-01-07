from Crypto.Util.number import *
import requests
import json
import codecs
import base64

def rsapq(p:int , q:int , e:int , ct:int) -> int:
  p = int(p)
  q = int(q)
  e = int(e)
  ct = int(ct)
  def egcd(a, b):
      if a == 0:
          return (b, 0, 1)
      else:
          g, y, x = egcd(b % a, a)
          return x - (b // a)
  n = p * q
  phi = (p - 1) * (q - 1)
  d = egcd(e, phi)
  pt = pow(ct, d, n)
  return pt

def factordb(n:int) -> str:
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

def hex2ascii(hex_string:str)-> bytes:
  return codecs.decode(hex_string,'hex')

def xor(plaintext:str,key:str)->bytes:
  cipher = ''
  q = len(plaintext)%len(key)
  for r in plaintext:
    cipher += chr(ord(r)^ord(key[q]))
  return cipher.encode()

def bass64(txt:str) ->str:
  return base64.b64decode(txt).decode()

def bass32(txt:str)->str:
  return base64.b32decode(txt).decode()

def long_byte(long:int)->bytes:
  return long_to_bytes(long)

def byte_long(txt:bytes)->int:
  return bytes_to_long(txt)

def dec2ascii(num:int)->str:
  ascii_text = chr(num)
  return ascii_text