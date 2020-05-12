from json import dump, load
from constants import CONFIG_FOLDER

bot_settings = {}
volume = 0
token = ''


def __assign_variables():
    global bot_settings
    bot_settings = settings['bot']
    global volume
    volume = bot_settings['volume']
    global token
    token = bot_settings['token']


def write_bot_config(key, value):
    settings['bot'][key] = value
    with open('config.json', 'w') as f:
        dump(settings, f)
    __assign_variables()


def get_config_value(key):
    with open(CONFIG_FOLDER, 'r') as f:
        json_file = load(f)
        return json_file['bot'][key]


with open(CONFIG_FOLDER, 'r') as f:
    json_file = load(f)
    settings = json_file
    __assign_variables()
