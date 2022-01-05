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
    if fc_name is None:
        return "Missing function name"
        
    if fc_name == "screenshot":
        if arg[0] is None:
            return "**Missing one argument**"
        text = screenshot(str(arg[0]))
        return text
    if fc_name == "weather":
        if arg[0] is None:
            return "**Missing one argument**"
        text = get_weather(arg[0])
        return text
    if fc_name == "shorturl":
        if arg[0] is None:
            return "**Missing one argument**"
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
    
    return f"**api command doesn't contain {fc_name}**"
def tool_cmd(fc_name,*arg):
    """tool_cmd : Handle all ctf tool command

    Args:
        fc_name [str]: Command name

    Returns:
        [str] : Command output
    """
    if fc_name is None:
        return "**Missing function name**"
        
    if fc_name == "base64":
        if arg[0] is None:
            return "**Missing one argument**"
        text = bass64(arg[0])
        return text
    
    if fc_name == "dec2ascii":
        if arg[0] is None:
            return "**Missing one argument**"
        text = dec2ascii(int(arg[0]))
        return text
    
    if fc_name == "rsapq":
        if arg[0] is None or arg[1] is None or arg[2] is None or arg[3] is None or arg[4] is None:
            return "**Missing argument (require 5 arguements)**"
        text = str(rsapq(int(arg[0]),int(arg[1]),int(arg[2]),int(arg[3]),int(arg[4])))
        return text
        
    if fc_name == "factordb":
        if arg[0] is None:
            return "**Missing one argument**"
        text = factordb(int(arg[0]))
        return text
    
    if fc_name == "hex2ascii":
        if arg[0] is None:
            return "**Missing one argument**"
        text = hex2ascii(arg[0])
        return str(text)
    
    if fc_name == "base32":
        if arg[0] is None:
            return "**Missing one argument**"
        text = bass32(arg[0])
        return text
    
    if fc_name == "xor":
        if arg[0] is None or arg[1] is None:
            return "**Missing argument(require 2 arguments)**"
        text = xor(arg[0],arg[1])
        return text
    
    if fc_name == "long_byte":
        if arg[0] is None:
            return "**Missing one argument**"
        text = long_byte(int(arg[0]))
        return str(text)
    
    if fc_name == "byte_long":
        if arg[0] is None:
            return "**Missing one argument**"
        text= byte_long(arg[0].encode())
        return str(text)
    
    if fc_name == "dec2ascii":
        if arg[0] is None:
            return "**Missing one argument**"
        text = dec2ascii(int(arg[0]))
        return text
      
    return f"**ctftool command doesn't contain {fc_name}**"

def challenge_cmd(fc_name,*arg):
    if fc_name is None:
        return "**Missing function name**"
    
    if fc_name == "show":
        try:
            if arg[0] is None:
                return "**Missing one arguement**"
            embed = show(int(arg[0])) # typeof(embed) = Discord.Embed

        except ValueError:
            return "**Invalid index**"
        
        return embed
    
    if fc_name == "score":
        text = score(int(arg[0]))
        return text
    
    if fc_name == "start":
        if arg[0] is None:
            return "**Missing two argument**"
        elif arg[1] is None:
            return "**Missing one argument**" 
        
        try:
            text = start(int(arg[0]),arg[1])
            return text
        except ValueError:
            return "**Invalid index**"
    
    if fc_name == "submit":
        if arg[1] == "":
            return "**Missing your flag**"
        text = flag_validate(arg[1],int(arg[0]))
        return text
    
    if fc_name == "create":
        
        text = creat_user(int(arg[0]))
        return text    
    
    return f"**challenge command doesn't contain {fc_name}**"

def usage(cmd):
    pass