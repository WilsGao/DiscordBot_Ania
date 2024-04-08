import discord
from discord.ext import commands

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

# 登錄機器人
bot.run('OTczODg5OTEyOTI5NjYwOTUw.GnVc8B.RscgrajxfB8pRf-JLXvE6jiimUZCPraE0T4OLA')
