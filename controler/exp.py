import discord
import json


def api_cmd(cmd):
    return
def tool_cmd(cmd):
    return
def challenge_cmd(cmd):
    if(cmd.startswith('show')):
        n = json.loads(open('controler\\data\\challenge_info.json','rb'))
        cmd = cmd.replace('')
        embed=discord.Embed(title=n["title"], url="https://challenge222324.w3spaces.com/", description="First web challenge ：）", color=0x781717)
        embed.set_author(name="e04qqq", icon_url="https://avatars.githubusercontent.com/u/66953227?s=40&v=4")
        embed.add_field(name="Difficulty", value="eazy", inline=True)
        embed.add_field(name="Category ", value="web", inline=True)
        embed.set_footer(text="https://challenge222324.w3spaces.com/")
        
        # await message.channel.send(embed=embed)
        
    
def usage(cmd):
    return