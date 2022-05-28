from telegram.ext import Updater, CommandHandler
from bot_commands import *

updater = Updater("5384058738:AAEf4Nqx6ox56GIHVzz1g8KtJEo7GcDU-Yg")

updater.dispatcher.add_handler(CommandHandler("hello", hello))
updater.dispatcher.add_handler(CommandHandler("hi", hi))
updater.dispatcher.add_handler(CommandHandler("time", time))
updater.dispatcher.add_handler(CommandHandler("help", help))
updater.dispatcher.add_handler(CommandHandler("start", help))
updater.dispatcher.add_handler(CommandHandler("sum", sum))
updater.dispatcher.add_handler(CommandHandler("math", math))

print('Start Bot')
updater.start_polling()
updater.idle()