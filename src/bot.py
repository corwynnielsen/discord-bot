import discord
from discord.ext import commands

from config_handler import ConfigHandler


class Bot():

    def __init__(self, config):
        self.bot = commands.Bot(command_prefix='!')
        self.config = config

    def run(self):
        self.bot.run(self.config.token)
