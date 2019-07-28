import discord
from discord.ext import commands
import json

# Constants
CONFIG_FOLDER = 'config.json'
AUDIO_FOLDER = 'audio'
TOKEN = None
CHANNEL_ID = None


# Bot setup
bot = commands.Bot(command_prefix='!')
volume = None
json_file = None

with open(CONFIG_FOLDER, 'r') as f:
    json_file = json.load(f)
    bot_settings = json_file['bot']
    volume = bot_settings['volume']
    TOKEN = bot_settings['token']
    CHANNEL_ID = bot_settings['channel']


async def is_connected(ctx):

    '''
    Check if bot is connected to a channel
    '''

    if bot.voice_clients:
        return bot.voice_clients[0].is_connected()
    else:
        return False


async def connect(ctx):

    '''
    If bot is not already connected to the channel, connect to the channel
    '''

    channel = bot.get_channel(CHANNEL_ID)
    if not await is_connected(ctx):
        await channel.connect()


async def play_audio(ctx):

    '''
    Generic function to play an audio file specified by the context object
    '''

    await connect(ctx)
    vc = bot.voice_clients[0]
    filename = ctx.command.name
    saved_volume = json_file['bot']['volume']

    audio_source = discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(source='{}\\{}.mp3'.format(AUDIO_FOLDER, filename)))
    audio_source.volume = saved_volume

    if not vc.is_playing():
        vc.play(audio_source)


@bot.command()
async def crazy(ctx):

    '''
    Bot command to play crazy.mp3
    '''

    await play_audio(ctx)


@bot.command()
async def bradberry(ctx):

    '''
    Bot command to play bradberry.mp3
    '''

    await play_audio(ctx)


@bot.command()
async def haha(ctx):

    '''
    Bot command to play haha.mp3
    '''

    await play_audio(ctx)


@bot.command()
async def yah(ctx):

    '''
    Bot command to play yah.mp3
    '''

    await play_audio(ctx)


@bot.command()
async def easy(ctx):

    '''
    Bot command to play easy.mp3
    '''

    await play_audio(ctx)


@bot.command()
async def slammin(ctx):

    '''
    Bot command to play slammin.mp3
    '''

    await play_audio(ctx)


@bot.command()
async def cheers(ctx):

    '''
    Bot command to play cheers.mp3
    '''

    await play_audio(ctx)


@bot.command()
async def cmon(ctx):

    '''
    Bot command to play cmon.mp3
    '''

    await play_audio(ctx)


@bot.command()
async def regula(ctx):

    '''
    Bot command to play regula.mp3
    '''

    await play_audio(ctx)


@bot.command()
async def shame(ctx):

    '''
    Bot command to play shame.mp3
    '''

    await play_audio(ctx)


@bot.command()
async def rat(ctx):

    '''
    Bot command to play rat.mp3
    '''

    await play_audio(ctx)


@bot.command()
async def sodie(ctx):

    '''
    Bot command to play sodie.mp3
    '''

    await play_audio(ctx)


@bot.command()
async def welcome(ctx):

    '''
    Bot command to play welcome.mp3
    '''

    await play_audio(ctx)


@bot.command()
async def bigtip(ctx):

    '''
    Bot command to play bigtip.mp3
    '''

    await play_audio(ctx)


@bot.command()
async def beau(ctx):

    '''
    Bot command to play beau.mp3
    '''

    await play_audio(ctx)


@bot.command()
async def gtfo(ctx):

    '''
    Bot command to make the bot leave the channel
    '''

    connected = await is_connected(ctx)
    if connected:
        await bot.voice_clients[0].disconnect()
    elif not connected:
        await ctx.send(content="I'm not in the channel")


@bot.command()
async def v(ctx):

    '''
    Bot command to change the volume
    '''

    message = ctx.message.content
    split_message = message.split(' ')
    volume = int(split_message[1])
    if (split_message[1].isdigit() and volume >= 0 and volume <= 100):
        json_file['bot']['volume'] = volume / 100
        with open('config.json', 'w') as f:
            json.dump(json_file, f)
        await ctx.send(content=('Success! Volume set to {}'.format(volume)))
    else:
        await ctx.send(content='Volume not must be between 1 and 100')

# run bot
bot.run(TOKEN)
