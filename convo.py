import discord
from discord.ext import commands
import logging
import asyncio
import random
import time
import os

@client.event
async def on_message(message):
    if message.content.lower().startswith('?test'):
        await client.send_message(message.channel, "Test bestanden")

    if message.content.lower().startswith('?coin'): #Coinflip 50/50% chance kopf oder zahl
        choice = random.randint(1,2)
        if choice == 1:
            await client.add_reaction(message, '🌑')
        if choice == 2:
            await client.add_reaction(message, '🌕')
client.run(os.environ['BOT_TOKEN'])
