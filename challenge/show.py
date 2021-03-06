import json
import discord
from discord import embeds


def show(index:int)->embeds:
    """show function

    Args:
        index (int): The index of the challenge

    Returns:
        embeds: A discord embed with challenge info
    """
    try:   
         
        n = json.loads(open("./challenge/data/challenge_info.json",'r',encoding="utf-8").read())[index-1]
    
        embed=discord.Embed(title=n["title"], description=n["description"],url=n["link"],color=0x781717)
        embed.set_author(name=n["author"],url=n["author-url"],icon_url=n["icon-url"])
        embed.add_field(name="Difficulty", value=n["difficulty"], inline=True)
        embed.add_field(name="Category ", value=n["category"], inline=True)
        return embed
    
    except IndexError as e:
        return "This challenge havn't been released yet."
    except Exception as e:
        return str(e)
