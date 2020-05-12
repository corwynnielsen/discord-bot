from sys import exit

import discord
from discord.ext import commands


class Util(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def disconnect(self, ctx):

        '''
        If bot is connected it will disconnect, otherwise a message is sent
        '''

        if ctx.voice_client is None and ctx.command.name != 'kill':
            await ctx.send(content="I'm not in the channel")

        await ctx.voice_client.disconnect()

    @commands.command()
    async def gtfo(self, ctx):

        '''
        Bot command to make the bot leave the channel
        '''
    
        await self.disconnect(ctx)
    

    @commands.command(hidden=True)
    async def kill(self, ctx):
        '''
        Kills bot process
        '''
        await self.disconnect(ctx)
        exit(0)


    @kill.before_invoke
    async def before_kill(self, ctx):
        if not await self.client.is_owner(ctx.message.author):
            await ctx.send(content='Only the owner can kill the bot process')
            raise commands.NotOwner(
                message="{} is not the owner".format(ctx.message.author))


def setup(client):
    client.add_cog(Util(client))