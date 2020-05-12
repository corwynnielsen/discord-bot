import os
import logging
from datetime import datetime

import discord
from discord.ext import commands

from config import token

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='./logs/discord-{:%d-%m-%Y__%H.%M}.log'.format(datetime.now()), encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client = commands.Bot(command_prefix='pls ')

for filename in os.listdir('./src/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

if __name__ == '__main__':
    client.run(token)

