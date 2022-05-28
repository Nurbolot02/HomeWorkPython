from telegram import Update
from telegram.ext import CallbackContext
from useFulFutires.MatN import do
from log import log
import datetime


def hello(update: Update, context: CallbackContext) -> None:
    log(update, context)
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def hi(update: Update, context: CallbackContext) -> None:
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}')


def help(update: Update, context: CallbackContext) -> None:
    log(update, context)
    update.message.reply_text(f'/hi - Приветсвие \n/sum a b \n/math Введите все числа и символы через пробел иначе ответа от меня не дождетесь ха-ха \nПример: /math 2 + 2 + 4 - 5 * 5 \n/time - время \n/help - список команд')


def time(update: Update, context: CallbackContext) -> None:
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def sum(update: Update, context: CallbackContext) -> None:
    log(update, context)
    msg = update.message.text.split()
    a = int(msg[1])
    b = int(msg[2])

    update.message.reply_text(f'{a} + {b} = {a + b}')
def math(update: Update, context: CallbackContext) -> None:
    log(update, context)
    msg = update.message.text
    text = ''
    for i in msg.split():
        if i != '/math':
            text += i + ' '
    print(text)
    try:
        result = do(text)
    except:
        update.message.reply_text(f'Что то пошло не так попробуйте ввести все числа и символы через пробел!')

    update.message.reply_text(f'{text} = {result[0]}')