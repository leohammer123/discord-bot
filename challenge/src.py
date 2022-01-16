import requests
import requests.exceptions
import os

def ch6(url:str)->str:
    try:
        res = requests.get(url)

        if res.status_code==200:
            if res.text.find("<h1>Hello world</h1>")!=-1:
                requests.get(url,params={"flag":os.getenv('CH7')})
                return False
            return True
        else:
            return True
        
        
    except ConnectionError:
        return "Connection error"
    except requests.exceptions.MissingSchema:
        return "Not a valid url"
    except requests.exceptions.ConnectTimeout:
        return "Time out error"
    except Exception as e:
        return str(e)
    
def ch8(url:str)->str:

    cookie_dict = {"token":os.getenv('CH8'),"site":"https://challenge1002.000webhostapp.com/c8/"}
    res = requests.get(url,cookies=cookie_dict)
    
    if res.status_code==200:
        return "Server is online"
    else:
        return "sth are wrong"
