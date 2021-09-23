import sys
sys.path.insert(1, './api/')
sys.path.insert(1, './ctftool/')


import discord
import os
from get_quote import get_quote
from screenshot import screenshot
from shorturl import shorturl
from get_weather import get_weather
from decodes import *

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
  
   

client.run(os.getenv('TOKEN'))




