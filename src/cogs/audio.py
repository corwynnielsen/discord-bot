import inspect
from os import listdir
from os.path import isfile, join, splitext
from sys import path

import discord
from discord.ext import commands

path.append("..\\")
from constants import AUDIO_FOLDER
from config import bot_settings, get_config_value, write_bot_config


class Audio(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.__setup_audio_commands()

    
    @staticmethod
    async def __play_audio(self, ctx):

        '''
        Generic function to play an audio file specified by the context object
        '''

        await self.connect(ctx)
        vc = ctx.voice_client
        filename = ctx.command.name

        audio_source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(source='{}\\{}.mp3'.format(AUDIO_FOLDER, filename)))
        audio_source.volume = get_config_value('volume')

        if not vc.is_playing():
            vc.play(audio_source)
        else:
            await self.__play_audio(ctx)


    def __setup_audio_commands(self):

        '''
        Procedurally create audio commands based on filename
        '''

        audio_files = [f for f in listdir(AUDIO_FOLDER) if isfile(join(AUDIO_FOLDER, f))]
        command_details = bot_settings['commands']
        for file in audio_files:
            filename, ext = splitext(file)
            command_description = command_details[filename]['description']
            bot_command = commands.Command(Audio.__play_audio, name=filename, help=command_description)
            bot_command.cog = self
            self.client.add_command(bot_command)

    @commands.command()
    async def v(self, ctx):

        '''
        Bot command to change the volume
        '''
        
        message = ctx.message.content
        volume_idx = 2
        split_message = message.split(' ')
        volume = int(split_message[volume_idx])
        if (split_message[volume_idx].isdigit() and volume >= 0 and volume <= 100):
            write_bot_config('volume', volume / 100)
            await ctx.send(content=('Success! Volume set to {}'.format(volume)))
        else:
            await ctx.send(content='Volume not must be between 1 and 100')


    @v.before_invoke
    async def connect(self, ctx):

        '''
        If bot is not already connected to the channel, connect to message author's channel
        '''

        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")


def setup(client):
    client.add_cog(Audio(client))