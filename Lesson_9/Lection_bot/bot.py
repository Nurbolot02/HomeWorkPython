from telegram.ext import Updater, CommandHandler
from bot_commands import *

updater = Updater("5384058738:AAEUp6Xw78o5uDYxC6vzaJnKlDMPxt8KgQs")

updater.dispatcher.add_handler(CommandHandler("hello", hello))
updater.dispatcher.add_handler(CommandHandler("hi", hi))
updater.dispatcher.add_handler(CommandHandler("time", time))
updater.dispatcher.add_handler(CommandHandler("help", help))
updater.dispatcher.add_handler(CommandHandler("start", help))
updater.dispatcher.add_handler(CommandHandler("sum", sum))
updater.dispatcher.add_handler(CommandHandler("math", math))
updater.dispatcher.add_handler(CommandHandler("Exchange", Exchange))
updater.dispatcher.add_handler(CommandHandler("Calc_Exchange", Calc_Exchange))
updater.dispatcher.add_handler(CommandHandler("getVideo", getVideo))

print('Start Bot')
updater.start_polling()
updater.idle()