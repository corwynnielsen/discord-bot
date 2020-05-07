from bot import Bot
from cogs.audio import Audio
from cogs.util import Util
from config_handler import ConfigHandler

#Instantiate single config handler to be used accross classes
config = ConfigHandler()

#Add cogs to bot
wrapper_bot = Bot(config)
real_bot_instance = wrapper_bot.bot
real_bot_instance.add_cog(Audio(real_bot_instance, config))
real_bot_instance.add_cog(Util(real_bot_instance))

if __name__ == '__main__':
    wrapper_bot.run()
