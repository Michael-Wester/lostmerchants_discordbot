import os
import discord
from dotenv import load_dotenv
from constants import *
from merchants import save_merchant_screenshot

def run():
    
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content == PREFIX + 'merchants':
            save_merchant_screenshot()
            await message.channel.send(file=discord.File(SCREENSHOT))
            return
        if message.content == PREFIX + 'help':
            await message.channel.send('Commands are: ' + PREFIX + 'merchants ' + PREFIX + 'help')
            return
        if message.content.startswith(PREFIX):
            await message.channel.send('Command not found. Type ' + PREFIX + 'help for a list of commands.')
            return

    client.run(TOKEN)





