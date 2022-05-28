from telegram import Update
from telegram.ext import CallbackContext
def log(update: Update, context: CallbackContext) -> None:
    path = 'db.csv'
    with open(path, 'a') as file:
        file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
