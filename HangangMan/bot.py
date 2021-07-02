import os
from dotenv import load_dotenv

import discord
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}!!!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'pong!')

@bot.command(name='갈!')
async def 갈(ctx):
    await ctx.send('멈춰!!!')

bot.run(TOKEN)
