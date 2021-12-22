import requests
from cookies import cookie


url = input()
cookie_dict = {"token":cookie}



res = requests.get(url,cookies=cookie_dict)

if res.status_code==200:
    print("Sever is online")
else:
    print("sth are wrong")