import requests


def screenshot(url):
  url = """https://api.browshot.com/api/v1/screenshot/create?key=V2ZByU9a7YOqGbsaJ54rsa21IgrpG5l&instance_id=26&url="""+url+"""&size=page&hide_popups=0&dark=0"""
  r = requests.get(url)
  return(r.code)