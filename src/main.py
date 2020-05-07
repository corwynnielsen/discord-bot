import os

import discord
from discord.ext import commands

from config import token

#Add cogs to bot
client = commands.Bot(command_prefix='pls ')

for filename in os.listdir('./src/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

if __name__ == '__main__':
    client.run(token)

