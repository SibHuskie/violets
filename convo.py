import discord
from discord.ext import commands
import logging
import asyncio
import random
import time
import os

@client.event
async def on_message(message):
    if message.content.startswith('v!greet'):
        await client.send_message(message.channel, 'Say hello')
        msg = await client.wait_for_message(author=message.author, content='hello')
        await client.send_message(message.channel, 'Hello.')
