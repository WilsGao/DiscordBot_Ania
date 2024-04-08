import os
import discord
from discord.ext import commands

# 定义 Intents 对象
intents = discord.Intents.default()

# 如果你的 Bot 需要发送/接收消息和读取成员列表
intents.messages = True
intents.members = True

#intents = discord.Intents.default()
intents = discord.Intents.all()
#intents.messages = True # 啟用發送/接收訊息的權限
intents.guilds = True # 如果你的機器人需要與伺服器交互，也需要啟用此權限
intent.message_content = True

# 初始化機器人客戶端
bot = commands.Bot(command_prefix='!', intents=intents)

# 定義當機器人啟動時的事件
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# 定義命令 !ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# 定義命令 !about
@bot.command()
async def about(ctx):
    await ctx.send('你好, 我是Ania!')

# 登錄機器人
bot.run(os.getenv('DISCORD_TOKEN'))
