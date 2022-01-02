import random
from ctftool.decode import *
from challenge.show import *
from api.basic_api import *
from challenge.start import *
from challenge.user_action import *

def api_cmd(fc_name:str,*arg):
    """api_cmd : Handle all api command

    Args:
        fc_name (str): Command name

    Returns:
        [str] or [bytes]: Command output might return picture or text ,depends on the function
    """
    if fc_name == "screenshot":
            text = screenshot(str(arg[0]))
            return text
    if fc_name == "weather":
            text = get_weather(arg[0])
            return text
    if fc_name == "shorturl":
        text = shorturl(arg[0])
        return text
    if fc_name == "release":
        text = release_challenge()
        return text
    if fc_name == "random":
        rand = random.randint(1,5)
        if rand == 1:
            text = Catfact()
            return text
        if rand == 2:
            text,pic = RandomUser()
            return text,pic
        if rand == 3:
            text = my_ip()
            return text
        if rand == 4:
            text = get_quote()
            return text
        if rand == 5:
            text = Dogpic()

def tool_cmd(fc_name,*arg):
    """tool_cmd : Handle all ctf tool command

    Args:
        fc_name [str]: Command name

    Returns:
        [str] : Command output
    """
    if fc_name == "base64":
        text = bass64(arg[0])
        return text
    
    if fc_name == "dec2ascii":
        text = dec2ascii(int(arg[0]))
        return text
    
    if fc_name == "rsapq":
            text = str(rsapq(int(arg[0]),int(arg[1]),int(arg[2]),int(arg[3]),int(arg[4])))
            return text
        
    if fc_name == "factordb":
        text = factordb(int(arg[0]))
        return text
    
    if fc_name == "hex2ascii":
        text = hex2ascii(arg[0])
        return str(text)
    
    if fc_name == "base32":
        text = bass32(arg[0])
        return text
    
    if fc_name == "xor":
        text = xor(arg[0],arg[1])
        return text
    
    if fc_name == "long_byte":
        text = long_byte(int(arg[0]))
        return str(text)
    
    if fc_name == "byte_long":
        text= byte_long(arg[0].encode())
        return str(text)
    
    if fc_name == "dec2ascii":
        text = dec2ascii(int(arg[0]))
        return text
      
def challenge_cmd(fc_name,*arg):
    
    if fc_name == "show":
        embed = show(int(arg[0])) # typeof(embed) = Discord.Embed
        return embed
    
    if fc_name == "score":
        text = score(int(arg[0]))
        return text
    
    if fc_name == "start":
        text = start(int(arg[0]),arg[1])
        return text
    
    if fc_name == "submit":
        
        text = flag_validate(arg[1],int(arg[0]))
        return text
    
    if fc_name == "create":
        
        text = creat_user(int(arg[0]))
        return text    
       
def usage(cmd):
    pass