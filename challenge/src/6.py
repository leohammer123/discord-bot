import requests
import requests.exceptions
flag = "flag{this_is_a_fake_flag}"
url = input()

res = requests.get(url)
if res.status_code==200:
    if res.text.find("<h1>Hello world</h1>")!=-1:
        requests.get(url,params={"flag":flag})       