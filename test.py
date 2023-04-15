#discord api
import discord
import asyncio
import random
from discord.ext import commands

# youtube api
import youtube_dl

#os
import os
import subprocess

#define area
curseWords = [
    "文明的语言就下你给一张精致的名片，能彰显一个人的修养与品德",
    "文明的语言就像一座桥梁，能够称为人与人沟通的纽带",
    "文明的语言可以营造和谐的气氛，化解戾气，令人心平气顺",
    "文明的语言可以如沐春风，丝丝沁人心脾"
]


#naming area
# client = discord.Client()
bot = commands.Bot(command_prefix='$')


# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))


@bot.command()
async def join(ctx):
    try:
        if (len(bot.voice_clients) != 0):
            await ctx.voice_client.disconnect()
        await ctx.author.voice.channel.connect()
    except Exception as e:
        await ctx.send('connection error')
        print(str(e))
        return

@bot.command()
async def disconnect(ctx):
    try:
        await ctx.voice_client.disconnect()
    except Exception as e:
        await ctx.send('disconnect error')
        print(str(e))
        return

@bot.command()
async def test(ctx, arg):
    print(arg)
    await ctx.send(arg)
    
@bot.command()
async def play(ctx, arg):
    youtube_dl.YoutubeDL()
# curseWordCount = 0
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
        
#     if message.content:
#         author = message.author 
#         mess = message.content
#         words = mess.split()

#     #get a Member type of bot 
#     bot_member = None
#     for member in client.get_all_members():
#         if member.bot:
#             bot_member = member
#             break     

#     #check if the message contains a curse word
#     for words in words:
#         if words == 'test':
#             global curseWordCount
#             curseWordCount += 1
#             rand = random.random()
#             rand *= len(curseWords)
#             await message.channel.send(curseWords[int(rand)] + " counts: " + str(curseWordCount))
        
        
#         if words == '$join':
#             try:
#                 await author.voice.channel.connect()
#                 #else:
#                     #await bot_member.move_to(author.voice.channel)
#             except Exception as e:
#                 await message.channel.send('connection error')
#                 print(str(e))
#                 return
#             break
#         if words == '$disconnect':
#             try:
#                 None
#                 #await bot_member.move_to(None)
#                 #await bot_member.voice.channel.disconnect()
#             except Exception as e:
#                 await message.channel.send('connection error')
#                 print(str(e))
#                 return
#             break
        

@bot.command()
async def p(ctx, arg):
    try :
        voice_channel = ctx.voice_client
        filename = "【原创音乐】《超级敏感》A-SOUL全新团曲MV-1vQ4y1Z7C2.flv"
        exe = r"I:\desktop\projects\discord_bot\ffmpeg-2021-11-18-git-85a6b7f7b7-full_build\ffmpeg-2021-11-18-git-85a6b7f7b7-full_build\bin\ffmpeg.exe"
        print("after read")
        voice_channel.play(discord.FFmpegPCMAudio(executable=exe, source=filename))
        print("after play")
        await ctx.send('**Now playing:** {}'.format(filename))
    except Exception as e:
        print(str(e))

@bot.command()
async def pa(ctx):
    try:
        voice_channel = ctx.voice_client
        voice_channel.pause()
    except Exception as e:
        print(str(e))

@bot.command()
async def stop(ctx):
    try:
        voice_channel = ctx.voice_client
        voice_channel.stop()
    except Exception as e:
        print(str(e))

@bot.command()
async def re(ctx):
    try:
        voice_channel = ctx.voice_client
        voice_channel.resume()
    except Exception as e:
        print(str(e))

@bot.command()
async def playurl(ctx, url):
    #输入网址规范(bilibili特供)
    #若网址中有&seid，需替换为%3D，若网址中有&spm_id_from，全部删除
    #例：原版 https://www.bilibili.com/video/BV1vQ4y1Z7C2?from=search&seid=5108490346672401765&spm_id_from=333.337.0.0
    #接受的格式 https://www.bilibili.com/video/BV1vQ4y1Z7C2?from=search%3D=5108490346672401765
    try:
        title = helpPlay(url)
        print(title)
        voice_channel = ctx.voice_client
        exe = r"I:\desktop\projects\discord_bot\ffmpeg-2021-11-18-git-85a6b7f7b7-full_build\ffmpeg-2021-11-18-git-85a6b7f7b7-full_build\bin\ffmpeg.exe"
        print("after read")
        voice_channel.play(discord.FFmpegPCMAudio(executable=exe, source=title))
        print("after play")
        await ctx.send('**Now playing:** {}'.format(title))
    except Exception as e:
        print(str(e))

def helpPlay(url):
    try:
        os.system(r"youtube-dl.exe -x --audio-format mp3" + " " + url)
        fin = os.popen("youtube-dl.exe --get-filename" + " " + url)
        title = fin.readlines()[0]
        return title
    except Exception as e:
        print(str(e))
#def deleteAll():
 #   os.system(r"cd I:\desktop\projects\discord_bot\temp")
  #  os.system("rm -r")


# client.run('OTA4ODk4MDI2MjAwOTE1OTc4.YY8bPw.vSSkBlRyuhFbbspNJiYCrk8ymi8')
bot.run('OTA4ODk4MDI2MjAwOTE1OTc4.YY8bPw.vSSkBlRyuhFbbspNJiYCrk8ymi8')


#https://github.com/Rapptz/discord.py