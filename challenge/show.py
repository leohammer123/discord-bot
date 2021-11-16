import json
import discord
from discord import embeds


def show(index:int)->embeds:
    try:    
        n = json.loads(open("C:\\Users\\j0704\\OneDrive\\文件\\GitHub\\discord-bot\\challenge\\data\\challenge_info.json",'r',encoding="utf-8").read())[index-1]
        embed=discord.Embed(title=n["title"], description=n["description"], color=0x781717)
        embed.set_author(name=n["author"])
        embed.add_field(name="Difficulty", value=n["difficulty"], inline=True)
        embed.add_field(name="Category ", value=n["category"], inline=True)
        embed.set_footer(text=n["link"])
        return embed
    except Exception as e:
        return str(e)
