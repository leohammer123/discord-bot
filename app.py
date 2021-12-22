import os
from io import BytesIO
import discord
from controler import exp
from discord.ext import commands

# Basic setting
client = commands.Bot(command_prefix="#")
channel_id = 692690549487960155


@client.event
async def on_ready():
  game = discord.Game('#help')
  await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message_join(member):
    channel = client.get_channel(channel_id)
    embed=discord.Embed(title=f"Welcome {member.name}", description=f"Thanks for joining {member.guild.name}!") # F-Strings!
    embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!
    await channel.send(embed=embed)

@client.command()
async def api(ctx,*arg):
  try:
    arg1 = arg[0]
    arg2 = arg[1] if len(arg)>1 else None
    arg3 = arg[2] if len(arg)>2 else None
    n = exp.api_cmd(arg1,arg2,arg3)
  except Exception as e:
    await ctx.channel.send(str(e))
  
  if type(n) == tuple:
    for r in n:
      if type(r)==type('str'):
        await ctx.channel.send(str(r)) 
      if type(r)==BytesIO:
        await ctx.channel.send(file=discord.File(r,'test.png'))
  if type(n)==type('str'):
        await ctx.channel.send(str(n))
  if type(n) == BytesIO:
     await ctx.channel.send(file=discord.File(n,'test.png'))
     
@client.command()
async def challenge(ctx,*arg):
  try:
    
    arg1 = arg[0]
    arg2 = arg[1] if len(arg)>1 else None
    arg3 = arg[2] if len(arg)>2 else None
    
    
    n = exp.challenge_cmd(arg1,arg2,arg3)


    if type(n)==discord.embeds.Embed:
      await ctx.channel.send(embed=n)
      
      
    if type(n)==type('str'):
          await ctx.channel.send(str(n))
          
          
    if type(n) == BytesIO:
      await ctx.channel.send(file=discord.File(n,'test.png'))
    
  except Exception as e:
    await ctx.channel.send(str(e))


@client.command()
async def ctftool(ctx,*arg):
  try:
    
    arg1 = arg[0]
    arg2 = arg[1] if len(arg)>1 else None
    arg3 = arg[2] if len(arg)>2 else None
    arg4 = arg[3] if len(arg)>3  else None
    arg5 = arg[4] if len(arg)>4 else None
    
    text = exp.tool_cmd(arg1,arg2,arg3,arg4,arg5)
    
    await ctx.channel.send(text)
    
  except Exception as e:
    await ctx.channel.send(e)



@client.command()
async def clear(ctx,*arg1):
  try:
    num = arg1[0]
    await ctx.channel.purge(limit=int(num)+1)
    
  except IndexError :
    await ctx.channel.send('Error : No arguement')
  except ValueError :
    await ctx.channel.send('Error : argument not an int.')
  except Exception as e:
    await ctx.channel.send(f'Error : {e}')



client.run(os.getenv('TOKEN'))
