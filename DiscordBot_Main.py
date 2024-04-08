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
intents.message_content = True

# 初始化機器人客戶端
bot = commands.Bot(command_prefix='!', intents=intents)

# 定義當機器人啟動時的事件
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# 定義命令 !ping
@bot.command()
async def ping(ctx):
    # 计算机器人的当前延迟（ping）值
    latency = bot.latency
    # 将延迟值转换为毫秒并发送到 Discord
    await ctx.send(f'Pong! My ping is {round(latency * 1000)}ms')

# 定義命令 !about
@bot.command()
async def about(ctx):
    await ctx.send('你好, 我是Ania!')

#斜線指令
@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")


# name指令顯示名稱，description指令顯示敘述
# name的名稱，中、英文皆可，但不能使用大寫英文
@app_commands.command(name = "hello", description = "Hello, world!")
async def hello(self, interaction: discord.Interaction):
    # 回覆使用者的訊息
    await interaction.response.send_message("Hello, world!")

# async def on_message(message):
    # if message.content.startswith('/'):
        # command = message.content[1:].split(' ')[0]
        # arguments = message.content[1+len(command):].strip()
        # if command == 'hello':
            # await message.channel.send('Hello!')
        # elif command == 'about':
            # await message.channel.send('我是Ania!，我喜歡花生')

    #await bot.process_commands(message)

# 登錄機器人
bot.run(os.getenv('DISCORD_TOKEN'))
