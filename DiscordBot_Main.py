import os
import discord 
import datetime
import sys
import random #輪盤用
from discord.ext import commands
from discord import app_commands#增加文字用
#from discord_slash import SlashCommand #無法使用
#from discord.app_commands import Option #音樂部分用
#from youtube_dl import YoutubeDL #音樂部分用
from typing import Optional#可選擇的項目用


# 定义 Intents 对象
intents = discord.Intents.all()
client = discord.Client(intents=intents)
# 如果你的 Bot 需要发送/接收消息和读取成员列表
intents.messages = True
intents.members = True
intents.guilds = True # 如果你的機器人需要與伺服器交互，也需要啟用此權限
intents.message_content = True

ADMIN_ID = 307524002942025731

bot = commands.Bot(command_prefix='!', intents=intents)

# on_ready 當機器人準備好時會執行的事件
@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")
    game = discord.Game('新手教學')
    await bot.change_presence(status=discord.Status.idle, activity=game)

#---------管理指令---------
# 重啟命令 !restart
@bot.command()
async def restart(ctx):
    if ctx.author.id == ADMIN_ID:
        await ctx.send("重新啟動...")
        await bot.close()
        python = sys.executable
        os.execl(python, python, *sys.argv)
    else:
        await ctx.send("您無權使用此命令。")

# 關機指令 !shutdown
@bot.command()
async def shutdown(ctx):
    if ctx.author.id == ADMIN_ID:
        await ctx.send("Shutting down...")
        await bot.close()
    else:
        await ctx.send("You do not have permission to use this command.")
#---------分隔線---------

#-----斜線指令-----
# name指令顯示名稱，description指令顯示敘述
# name的名稱，中、英文皆可，但不能使用大寫英文
@bot.tree.command(name = "hello", description = "使用Hello指令")
async def hello(ctx):
    await ctx.response.send_message("Hello, world!")

@bot.tree.command(name="about", description="關於我")
async def about(ctx):
    await ctx.response.send_message('你好, 我是Ania!, 我喜歡花生')

@bot.tree.command(name="shutup", description="讓人安靜的指令")
@app_commands.describe(first = "破麻前的文字",secon = "破麻後的字")
async def shutup(ctx, first: Optional[str] = None, secon: Optional[str] = None):
    if first == None:
        first = " "
    if secon == None:
        secon = " "
    await ctx.response.send_message(f"{first}破麻{secon}閉閉啦!")

@bot.tree.command(name="roulette", description="輪盤三選一!")
async def roulette(ctx, option1: str, option2: str, option3: str):
    options = [option1, option2, option3]
    result = random.choice(options)
    await ctx.response.send_message(f"結果是：{result}")

@bot.tree.command(name="ping", description="測延遲")
async def ping(ctx):
    # 计算机器人的当前延迟（ping）值並将延迟值转换为毫秒并发送到 Discord
    await ctx.response.send_message(f'ping: {round(bot.latency * 1000)}ms')

@bot.tree.command(name="embedbase", description="嵌入式內容")
@app_commands.describe(標題 = "大標題",內文 = "要呈現的內容")
async def embed_base(ctx, 標題: str, 內文: str = None, imaurl: Optional[str] = None):
    embed = discord.Embed(
        title = f"{標題}", #標題
        #url = "https://www.youtube.com/", #縮圖
        description = f"{內文}xxx", #內容
        color = 0xdfe228,#框左側的顏色
        timestamp = datetime.datetime.now()
    )
    #頭像
    embed.set_author(name="作者姓名", icon_url="")
    #圖片
    embed.set_image(url=imaurl)
    #embed.set_thumbnail(url="https://imgur.com/A4oZJQ5")
    await ctx.response.send_message(embed=embed)

@bot.tree.command(name = "join", description = "讓機器人進到語音頻道")
async def join(interaction):

    # 這裡的指令會讓機器人進入調用者所在的語音頻道
    await ctx.response.send_message("IN")
    # 獲取用戶的語音頻道
    author = interaction.user
    voice_state = author.voice
    if voice_state is None or voice_state.channel is None:
        await interaction.response.send_message("You are not connected to any voice channel")
        return
    
    # 檢查機器人是否已經在語音頻道中
    voice_client = discord.utils.get(bot.voice_clients, guild=interaction.guild)
    if voice_client is not None:
        await interaction.response.send_message("Already connected to a voice channel")
        return
    # 加入語音頻道
    await voice_state.channel.connect()
    
@bot.tree.command(name = "leave", description = "讓機器人離開語音頻道")
async def leave(ctx):

    #離開call他那個伺服器的所在頻道
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if voice == None:
            await ctx.response.send("The Mbot is not connected to a voice channel")
        else:
            await voice.disconnect()

#---------測試指令---------
@bot.event #成功
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('new Script'):
        await message.channel.send('Hello, World!')

@bot.tree.command(name = "userinfo", description = "使用userinfo指令")
async def userinfo(ctx, member: discord.Member):

    roles = [role.name for role in member.roles[1:]]

    await ctx.send(
        f"User name: {member.name}\n"
        f"User ID: {member.id}\n"
        f"Joined at: {member.joined_at}\n" 
        f"Roles: {', '.join(roles)}"
    )

warns = {} #警告計數

@bot.tree.command(name = "warn", description = "警告指令")
@app_commands.describe(user = "選擇用戶",reason = "理由")
async def warn(ctx, user: discord.Member,*, reason: str):
    # 检查是否有权限执行警告操作
    if ctx.message.author.guild_permissions.administrator:
        member = message.mentions[0]
        # 在这里执行警告操作，比如向用户发送私信或在特定频道发布警告消息
        await ctx.send(f'{user.mention} 已被警告，原因：{reason}')
    else:
        await ctx.send("你沒有權限執行此操作！")

@bot.tree.command(name = "whatwarn", description = "警告次數指令")
@app_commands.describe(member = "選擇用戶")
async def whatwarn(ctx, member: discord.Member):
    
    if member.id not in warns:
        warns[member.id] = 1
    else:
        warns[member.id] += 1

    await ctx.send(f"{member.name} 已獲得 {warns[member.id]} 次警告!")

    if warns[member.id] == 3:
        await member.edit(timed_out_until=discord.utils.utcnow() + datetime.timedelta(seconds=10))
        await ctx.send(f'{member.name}已被禁止，將在{seconds}秒後解除。')
#---------分隔線---------

# 登錄機器人
bot.run(os.getenv('DISCORD_TOKEN'))
