import os
import discord
from discord.ext import commands
from discord import app_commands
import sys
import random

# 定义 Intents 对象
#intents = discord.Intents.default()

# 如果你的 Bot 需要发送/接收消息和读取成员列表
intents = discord.Intents.all()
intents.messages = True
intents.members = True
intents.guilds = True # 如果你的機器人需要與伺服器交互，也需要啟用此權限
intents.message_content = True

ADMIN_ID = os.getenv('ADMIN_ID')

# 初始化機器人客戶端
bot = commands.Bot(command_prefix='!', intents=intents)

# 定義命令 !ping
@bot.command()
async def ping(ctx):
    # 计算机器人的当前延迟（ping）值並将延迟值转换为毫秒并发送到 Discord
    await ctx.send(f'ping: {round(bot.latency * 1000)}ms')

# 定義命令 !about
@bot.command()
async def about(ctx):
    await ctx.send('你好, 我是Ania!')

# 定義命令 !restart
@bot.command()
async def restart(ctx):
    if ctx.author.id == ADMIN_ID:
        await ctx.send("重新啟動...")
        await bot.close()
        python = sys.executable
        os.execl(python, python, *sys.argv)
    else:
        await ctx.send("您無權使用此命令。")


#斜線指令 # on_ready定義當機器人啟動時的事件
@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")


# name指令顯示名稱，description指令顯示敘述
# name的名稱，中、英文皆可，但不能使用大寫英文
@bot.tree.command(name = "hello", description = "使用Hello指令")
async def hello(response: discord.InteractionResponse):
    # 回覆使用者的訊息
    await response.send_message("Hello, world!")

@bot.tree.command(name = "shutup", description = "讓人安靜的指令")
async def shutup(response: discord.InteractionResponse):
    # 回覆使用者的訊息
    await response.send_message("破麻 你閉閉!")

@bot.tree.command(name = "help", description="顯示機器人的指令列表")
async def help_command(response: discord.InteractionResponse):
    # 自定义帮助消息
    help_message = "我能使用的功能：\\n"\
                   "/help - 顯示幫助訊息\\n"\
                   "/play - 如何播放音樂\\n"\
                   "/roulette - 輪盤怎麼用\\n"\
                   "/translate - 翻譯文字"
    # 回复用户帮助信息
    await response.send_message(help_message)

@bot.tree.command(name="roulette", description="輪盤啟動!")
async def roulette(response: discord.InteractionResponse):
    # 模拟轮盘游戏，这里我们简单地随机生成一个结果
    results = ["藍色", "綠色", "紅色"]
    result = random.choice(results)
    
    # 回复用户轮盘结果
    await response.send_message(f"結果是：{result}") 


@bot.tree.command(name="play", description="播放音乐")
async def play_music(response: discord.InteractionResponse):
    # 播放音乐逻辑，这里假设你有一个 play_music() 函数来处理音乐播放
    #await play_music()
    
    # 回复用户播放音乐
    await response.send_message("音乐已开始播放")




# 登錄機器人
bot.run(os.getenv('DISCORD_TOKEN'))
