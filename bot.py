import discord
import asyncio
from threading import Thread
import time
import openai
import os
TOKEN = 'YOUR TOKEN' #token for dc
KEY = 'YOUR KEY' #API key for chatgpt

# new property needed when create client in the update at 2022.12.9
# check this for details: https://discordpy.readthedocs.io/en/stable/api.html#intents

#Discord client
intents = discord.Intents.all() #All Permissions
client = discord.Client(intents = intents)

#ChatGPT
conditions = 'you are a chatbot in discord. your name is PeaceKeeper'
play_music = '''
if I told you to play a video or music, find the link for the music on internet and reply me with the following format:
"playing" + music name + music link
'''
#私货
mycondition = '你爹叫Louis'

def get_reply(message):
    openai.api_key = KEY
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": conditions},
            {"role": "system", "content": mycondition},
            {"role": "user", "content": message}
        ]
    )
    reply = completion.choices[0].message.content
    print(reply)
    return reply

@client.event
async def on_ready():
    print(client.user, "has logged in.")


@client.event
async def on_message(message):
    # ignore messages sent by the bot
    if message.author == client.user:
        return
    
    #commands for testing only
    if message.content.startswith('$join'):
        channel = message.author.voice.channel
        await channel.connect()
        return
    if message.content.startswith('$leave'):
        print(client.voice_clients[0])
        await client.voice_clients[0].disconnect()

    # when mentioned
    if client.user in message.mentions:
        #message text:   "@user content"
        #message format: "<mentioned user> content"
        text = message.content
        text = text[text.find('>') + 1:] #delete mention part and get text content
        print(text)
        reply = get_reply(text)
        await message.channel.send(reply)
        return
client.run(TOKEN)
