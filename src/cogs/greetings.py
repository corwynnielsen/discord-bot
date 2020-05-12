import discord
from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        channel = member.guild.system_channel
        if before.channel is None and after.channel is not None:
            if member.nick == 'Froxo':
                await channel.send('Shut up {0.mention}.'.format(member))
                return
            await channel.send('Welcome {0.mention}!'.format(member))


def setup(client):
    client.add_cog(Greetings(client))