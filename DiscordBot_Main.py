import discord
from discord.ext import commands
import os

# 初始化機器人客戶端
bot = commands.Bot(command_prefix='!')

# 定義當機器人啟動時的事件
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# 定義命令 !ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# 從環境變量中讀取機器人令牌
discord_token = os.getenv('DISCORD_TOKEN')

# 登錄機器人
bot.run(discord_token)
