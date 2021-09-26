from crypto.Util.number import * 
import requests
import json
import codecs
import base64

def rsapq(p,q,e,ct):
  p = int(p)
  q = int(q)
  e = int(e)
  ct = int(ct)
  def egcd(a, b):
      if a == 0:
          return (b, 0, 1)
      else:
          g, y, x = egcd(b % a, a)
          return (g, x - (b // a) * y, y)

  def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
  n = p * q
  phi = (p - 1) * (q - 1)
  gcd, a, b = egcd(e, phi)
  d = a
  pt = pow(ct, d, n)
  return str(pt)



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

def hex2ascii(hex):
  return codecs.decode(hex,'hex')

def xor(plaintext,key):
  n = 0
  cipher = ''
  q = len(plaintext)%len(key)
  for r in plaintext:
    cipher += chr(ord(r)^ord(key[q]))
    if not(chr(ord(r)^ord(key[q])).isprintable()):
        n = 1
  if n:
        cipher = str(cipher.encode())
  return cipher

def bass64(txt):
  return base64.b64decode(txt).decode()

def bass32(txt):
  return base64.b32decode(txt).decode()

def long_byte(long):
  return long_to_bytes(long)

def byte_long(txt):
  return bytes_to_long(txt)

def dec2ascii(num):
  ascii_text = ''
  for n in num:
    ascii_text+=chr(int(n))
  return ascii_text

