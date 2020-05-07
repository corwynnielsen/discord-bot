from json import dump, load

from constants import CONFIG_FOLDER


class ConfigHandler():

    def __init__(self):
        with open(CONFIG_FOLDER, 'r') as f:
            json_file = load(f)
            self.settings = json_file
            self.assign_variables()

    def assign_variables(self):
        self.bot_settings = self.settings['bot']
        self.volume = self.bot_settings['volume']
        self.token = self.bot_settings['token']
        self.channel_id = self.bot_settings['channel']

    def write_bot_config(self, key, value):
        self.settings['bot'][key] = value
        with open('config.json', 'w') as f:
            dump(self.settings, f)
        self.assign_variables()
