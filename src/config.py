from json import dump, load
from constants import CONFIG_FOLDER

bot_settings = {}
volume = 0
token = ''
channel_id = -1

def __assign_variables():
    global bot_settings
    bot_settings = settings['bot']
    global volume
    volume = bot_settings['volume']
    global token
    token = bot_settings['token']
    global channel_id
    channel_id = bot_settings['channel']


def write_bot_config(key, value):
    settings['bot'][key] = value
    with open('config.json', 'w') as f:
        dump(settings, f)
    __assign_variables()

with open(CONFIG_FOLDER, 'r') as f:
    json_file = load(f)
    settings = json_file
    __assign_variables()

