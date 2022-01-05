import os
from io import BytesIO
import discord
from challenge.user_action import score as sc
from discord.embeds import Embed
from controler import exp
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from challenge.db import test
from operator import itemgetter

# Basic setting
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="#",intents=intents)
channel_id = 692690549487960155

@client.event
async def on_ready():
  game = discord.Game('#help')
  await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message_join(member):
    channel = client.get_channel(channel_id)
    embed=discord.Embed(title=f"Welcome {member.name}", description=f"Thanks for joining {member.guild.name}!")
    embed.set_thumbnail(url=member.avatar_url)
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
      if type(r) is str:
        await ctx.channel.send(str(r)) 
      if type(r) is BytesIO:
        await ctx.channel.send(file=discord.File(r,'test.png'))
  if type(n) is str:
        await ctx.channel.send(str(n))
  if type(n) is BytesIO:
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
      
      
    if type(n) is str:
          await ctx.channel.send(str(n))
          
          
    if type(n) is BytesIO:
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
    await ctx.channel.send('**No arguement**')
  except ValueError :
    await ctx.channel.send('**argument not an int**')
  except Exception as e:
    await ctx.channel.send(f'**Error : {str(e)}**')

@client.command()
async def submit(ctx,message):
  
  user = ctx.message.author
  id = user.id
  channel = client.get_channel(channel_id)
  res = exp.challenge_cmd("submit",id,message)
  await ctx.reply(res,mention_author=True)
  await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
  await channel.send(res)

@client.command()
async def create(ctx):
  
  id = ctx.message.author.id
  res = exp.challenge_cmd("create",id)
  await ctx.channel.send(res)

@client.command()
async def score(ctx):
  try:
    score_board = test()
    score_board = sorted(score_board,key=itemgetter(1),reverse=True)
    index = 0
    
    for r in score_board:
      
      r = list(r)
      user = client.get_user(score_board[index][0])
      if user is None :
        r.append("Unknown User")
      else:
        r.append(user)
        
      score_board[index] = r
      index += 1
      
    names = ''
    

    for index in range(len(score_board)):
      if type(score_board[index][3]) is str:
        names += f'{index+1}#<{score_board[index][3]}> -with {score_board[index][1]}\n'
      else:
        names += f'{index+1}#<{score_board[index][3].mention}> -with {score_board[index][1]}\n'
        
    embed = discord.Embed(title="Leaderboard")
    embed.add_field(name="Names", value=names, inline=False)
    embed.set_footer(text=f"{sc(ctx.message.author.id)}")
    await ctx.send(embed=embed)
  except Exception as e:
    print(e)
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.channel.send(f"**{ctx.message.content} is not a valid command**")

client.run(os.getenv('TOKEN'))