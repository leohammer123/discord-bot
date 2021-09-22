import sys
sys.path.insert(1, './api/')
sys.path.insert(1, './ctftool/')


import discord
import os
from get_quote import get_quote
from screenshot import screenshot
from shorturl import shorturl
from get_weather import get_weather
from discord.ext import commands
from bass import bass32,bass64
from xor import xor
from long_byte import long_byte
from rsapq import rsapq
from factordb import factordb

client = discord.Client()


@client.event
async def on_ready():
  game = discord.Game('#help')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
  await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
  i = message.content
  if i.find("#help") != -1 and i.find('ctf')==-1:
    await message.channel.send("1. ctftool : A set of ctf tool.\n2. api : Some useful api.\n3. sendbox : Run a python send box online\n4. challenge : Some eazy ctf challenge." )
    i = ''
  if i.find("#help ctftool")!=-1:
    await message.channel.send("""ctftool man page:\n\n 1: base64 or base32 {text} : base64/32 decode :)\n2: xor {text} {key} : xor de/encryption . if the output string is unprintable then it will shows the result as byte string .\n3: long_byte or byte_long {long int}or{byte} : The conversion of the Crypto library .\n4 rsapq {p} {q} {e} {ct} : Reverse the plaintext by using Extended Euclidean algorithm. # Notes the ct is stand for cipher text. """)

  if i.find("#sandbox") != -1:
    await message.channel.send('start the snadbox~~~~')
  if i.find("#lol") != -1:
    await message.channel.send('this != funny at all')
  if i.find("#quote") != -1:
    await message.channel.send(get_quote())
  if i.find("#screenshot") != -1:
    await message.channel.send('status code:'+screenshot(i.split(' ')[1]))
  if i.find('#weather') != -1:
    await message.channel.send(get_weather(i.split(' ')[1]))
  if i.find('#shorturl') != -1:
    await message.channel.send(shorturl(i.split(' ')[1]))
  if i.find('#ctftool') != -1:
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
  if i.find('#request')!= -1:
    await message.channel.send('testing')
   

client.run(os.getenv('TOKEN'))

