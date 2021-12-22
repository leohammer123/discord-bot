import requests
from cookies import cookie


url = input()
cookie_dict = {"token":cookie,"origin":"https://challenge1002.000webhostapp.com/c8"}



res = requests.get(url,cookies=cookie_dict)

if res.status_code==200:
    print("Sever is online")
else:
    print("sth are wrong")