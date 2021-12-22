import requests
import requests.exceptions
import os

def ch6(url:str)->str:
    try:
        res = requests.get(url)
        
        if res.status_code==200:
            if res.text.find("<h1>Hello world</h1>")!=-1:
                requests.get(url,params={"flag":os.getenv('ch7-flag')})
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
        return e
    