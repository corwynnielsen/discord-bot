import asyncio
import inspect
from os import listdir
from os.path import isfile, join, splitext
from sys import path

import discord
from discord.ext import commands

path.append("..\\")
from constants import AUDIO_FOLDER


class Audio(commands.Cog):
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__setup_audio_commands())

        
    async def __connect(self, ctx):

        '''
        If bot is not already connected to the channel, connect to the channel
        '''

        channel = self.bot.get_channel(self.config.channel_id)
        if not ctx.voice_client:
            await channel.connect()


    async def __play_audio(self, ctx):

        '''
        Generic function to play an audio file specified by the context object
        '''

        await self.__connect(ctx)
        vc = ctx.voice_client
        filename = ctx.command.name
        saved_volume = self.config.volume

        audio_source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(
            source='{}\\{}.mp3'.format(AUDIO_FOLDER, filename)))
        audio_source.volume = saved_volume

        if not vc.is_playing():
            vc.play(audio_source)


    async def __setup_audio_commands(self):

        '''
        Procedurally create audio commands based on filename
        '''

        audio_files = [f for f in listdir(AUDIO_FOLDER) if isfile(join(AUDIO_FOLDER, f))]
        command_details = self.config.bot_settings['commands']
        for file in audio_files:
            filename, ext = splitext(file)
            command_description = command_details[filename]['description']
            bot_command = commands.Command(self.__play_audio , name=filename, help=command_description)
            self.bot.add_command(bot_command)

    @commands.command()
    async def v(self, ctx):

        '''
        Bot command to change the volume
        '''
        
        message = ctx.message.content
        split_message = message.split(' ')
        volume = int(split_message[1])
        if (split_message[1].isdigit() and volume >= 0 and volume <= 100):
            self.config.write_bot_config('volume', volume / 100)
            await ctx.send(content=('Success! Volume set to {}'.format(volume)))
        else:
            await ctx.send(content='Volume not must be between 1 and 100')