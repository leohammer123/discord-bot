from discord import channel
from discord.flags import MessageFlags
from challenge.flag_validate import flag_check
import sys
sys.path.insert(1, './api/')
sys.path.insert(1, './ctftool/')
sys.path.insert(1, './challenge/')


import hashlib
import discord
import os
from get_quote import get_quote
from screenshot import screenshot
from shorturl import shorturl
from get_weather import get_weather
from decodes import *
from discord.ext import commands
from challenge import *

client = discord.Client()
intents = discord.Intents.default()
intents.members=True
client = discord.Client(intents=intents)
channel_id = 692690549487960155


@client.event
async def on_ready():
  game = discord.Game('#help')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
  await client.change_presence(status=discord.Status.online, activity=game)
  guild = client.get_guild(channel_id)
  with open('log','a') as s:
    for r in guild.members:
      s.write(str(r)+'\n')


@client.event
async def on_message_join(member):
    channel = client.get_channel(channel_id)
    embed=discord.Embed(title=f"Welcome {member.name}", description=f"Thanks for joining {member.guild.name}!") # F-Strings!
    embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!
    await channel.send(embed=embed)

@client.event
async def on_message(message):
  i = message.content
  print(message.content)
  print(message.author)
  if i.startswith('flag{'):
    if flag_check(i,message.author):
      await message.channel.send('Congrat !!!! You solve the challenge.')
      await message.delete()

    else:
      await message.channel.send('It seems to have some problem with ur flag.')
      await message.delete()
  if i.startswith("#help") and i.find('ctf')==-1:
    await message.channel.send("1. ctftool : A set of ctf tool.\n2. api : Some useful api.\n3. sendbox : Run a python send box online\n4. challenge : Some eazy ctf challenge." )
    i = ''
  if i.startswith("#help ctftool"):
    await message.channel.send("""ctftool man page:\n\n 1: base64 or base32 {text} : base64/32 decode :)\n2: xor {text} {key} : xor de/encryption . if the output string is unprintable then it will shows the result as byte string .\n3: long_byte or byte_long {long int}or{byte} : The conversion of the Crypto library .\n4 rsapq {p} {q} {e} {ct} : Reverse the plaintext by using Extended Euclidean algorithm. # Notes the ct is stand for cipher text. """)

  if i.startswith("#sandbox"):
    await message.channel.send('start the snadbox~~~~')
  if i.startswith("#lol"):
    await message.channel.send(f'{message.author.mention} this != funny at all')
  if i.startswith("#quote"):
    await message.channel.send(get_quote())
  if i.startswith("#screenshot"):
    await message.channel.send('status code:'+screenshot(i.split(' ')[1]))
  if i.startswith('#weather'):
    await message.channel.send(get_weather(i.split(' ')[1]))
  if i.startswith('#shorturl'):
    await message.channel.send(shorturl(i.split(' ')[1]))
  if i.startswith('#ctftool'):
    if i.find('base64')!=-1:
      await message.channel.send(bass64(i.split(' ')[2]).decode())
    if i.find('long_byte')!=-1:
      await message.channel.send(long_byte(int(i.split(' ')[2])).decode())
    if i.find('base32')!=-1:
      await message.channel.send(bass32(i.split(' ')[2]).decode())
    if i.find('xor')!=-1:
      await message.channel.send(xor(i.split(' ')[2],i.split(' ')[3]))
    if i.find('rsapq')!=-1:
      await message.channel.send(rsapq(i.split(' ')[2],i.split(' ')[3],i.split(' ')[4],i.split(' ')[5]))
    if i.find('factordb')!=-1:
      await message.channel.send(factordb(i.split(' ')[2]))
    if i.find('hex2ascii')!=-1:
      await message.channel.send(hex2ascii(i.split(' ')[2]))
    if i.find('dec2ascii')!=-1:
      await message.channel.send(dec2ascii(i.split(' ')[2:]))
  if i.startswith('test'):
    #names = list()
    #for user in Guild.members:
      #names.append(user.name)
    #print(names)
    guild = client.get_guild(channel_id)
    print(guild.members)
  if i.startswith('#challenge'):
    if i.find('1')!=-1:
      embed=discord.Embed(title="challenge1", url="https://challenge222324.w3spaces.com/", description="First web challenge ：）", color=0x781717)
      embed.set_author(name="e04qqq", icon_url="https://avatars.githubusercontent.com/u/66953227?s=40&v=4")
      embed.add_field(name="Difficulty", value="eazy", inline=True)
      embed.add_field(name="Category ", value="web", inline=True)
      embed.set_footer(text="https://challenge222324.w3spaces.com/")
      await message.channel.send(embed=embed)
    if i.find('2')!=-1:
      embed=discord.Embed(title="challenge2", url="https://challenge1002.000webhostapp.com/c1/", description="This is a only about php.", color=0x781717)
      embed.set_author(name="e04qqq", icon_url="https://avatars.githubusercontent.com/u/66953227?s=40&v=4")
      embed.add_field(name="Difficulty", value="eazy", inline=True)
      embed.add_field(name="Category ", value="web", inline=True)
      embed.set_footer(text="https://challenge1002.000webhostapp.com/c1/")
      await message.channel.send(embed=embed)
    if i.find('3')!=-1:
      embed=discord.Embed(title="challenge3", url="https://leohammer123.github.io/python-package-test/1.html", description="if you wanna get rickrolled -->", color=0x781717)
      embed.set_author(name="e04qqq", icon_url="https://avatars.githubusercontent.com/u/66953227?s=40&v=4")
      embed.add_field(name="Difficulty", value="eazy", inline=True)
      embed.add_field(name="Category ", value="web", inline=True)
      embed.set_footer(text="https://leohammer123.github.io/python-package-test/1.html")
      await message.channel.send(embed=embed)
    if i.find('4')!=-1:
      embed=discord.Embed(title="challenge4", description="bass64 ", color=0x781717)
      embed.set_author(name="e04qqq", icon_url="https://avatars.githubusercontent.com/u/66953227?s=40&v=4")
      embed.add_field(name="Difficulty", value="eazy", inline=True)
      embed.add_field(name="Category ", value="crypto", inline=True)
      embed.set_footer(text="ZmxhZ3tiYXNlNjRfaXNfbm90X2FuX2VuY3J5cHRpb259==")
      await message.channel.send(embed=embed)
    if i.find('5')!=-1:
      embed=discord.Embed(title="challenge5", url="https://raw.githubusercontent.com/leohammer123/python-package-test/main/threading/encrypt.py", description="This should be secure enough so i even give you my encrypt script.", color=0x781717)
      embed.set_author(name="e04qqq", icon_url="https://avatars.githubusercontent.com/u/66953227?s=40&v=4")
      embed.add_field(name="Difficulty", value="medium", inline=True)
      embed.add_field(name="Category ", value="crypto", inline=True)
      embed.set_footer(text="https://raw.githubusercontent.com/leohammer123/python-package-test/main/threading/encrypt.py")
      await message.channel.send(embed=embed)



client.run()


