import discord
from discord import embeds

from ctftool.decode import *
from challenge.show import *
from api.basic_api import *

def api_cmd(fc_name,*arg):
    if fc_name=="quote":
        try:
            text = get_quote()
        except Exception as e:
            return str(e)
        return text
    if fc_name == "screenshot":
        try:
            text = screenshot(str(arg[0]))
        except Exception as e:
            return e
        return text
    if fc_name == "weather":
        try:
            text = get_weather(arg[0])
        except Exception as e:
            return e
        return text
    if fc_name == "shorturl":
        try:
            text = shorturl(arg[0])
        except Exception as e:
            return e
        return text
    if fc_name == "release":
        try:
            text = release_challenge()
        except Exception as e:
            return e
        return text



def tool_cmd(fc_name,*arg):
    if fc_name == "base64":
        try:
            text = bass64(arg[0])
        except Exception as e:
            return e
        return text
    if fc_name == "dec2ascii":
        try:
            text = dec2ascii(int(arg[0]))
        except Exception as e:
            return e
        return text
    if fc_name == "rsapq":
        try:
            text = rsapq(int(arg[0]),int(arg[1]),int(arg[2]),int(arg[3]),int(arg[4]))
        except Exception as e:
            return e
        return str(text)
    if fc_name == "factordb":
        try:
            text = factordb(int(arg[0]))
        except Exception as e:
            return e
        return text
    if fc_name == "hex2ascii":
        try:
            text = hex2ascii(arg[0])
        except Exception as e:
            return e
        return str(text)
    if fc_name == "base32":
        try:
            text = bass32(arg[0])
        except Exception as e:
            return e
        return text
    if fc_name == "xor":
        try:
            text = xor(arg[0],arg[1])
        except Exception as e:
            return e
        return text
    if fc_name == "long_byte":
        try:
            text = long_byte(int(arg[0]))
        except Exception as e:
            return e
        return str(text)
    if fc_name == "byte_long":
        try:
            text = byte_long(arg[0].encode())
        except Exception as e:
            return e
        return str(text)
    if fc_name == "dec2ascii":
        try:
            text = dec2ascii(int(arg[0]))
        except Exception as e:
            return e
        return text   
def challenge_cmd(fc_name,*arg):
    if fc_name == "show":
        try:
            embed = show(int(arg[0]))
        except Exception as e:
            return e
        return embed
    if fc_name == "score":
        pass
def usage(cmd):
    return