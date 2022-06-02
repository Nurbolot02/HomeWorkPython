import datetime
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from Lesson_10.Wheather.log import log
from config import tg_bot_token, open_weather_key

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(massage: types.Message):
    log(massage)
    await massage.reply('Привет! '
                        '\nНапиши мне название города и я пришлю сводку погоды!')


@dp.message_handler()
async def start_command(massage: types.Message):
    log(massage)
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облочно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={massage.text}&appid={open_weather_key}&units=metric"
        )
        data = r.json()
        weather_Descryption = data["weather"][0]["main"]
        if weather_Descryption in code_to_smile:
            wd = code_to_smile[weather_Descryption]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"

        city = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        wind_speed = data["wind"]["speed"]
        length_of_the_day = sunset_timestamp - sunrise_timestamp

        await massage.reply(f'**** {datetime.datetime.now().strftime("%d-%m-%Y %H:%M")} ****'
                            f'\nПогода в городе: {city}'
                            f'\nТемпаратура: {temp}°С {wd}'
                            f'\nВлажность: {humidity}%'
                            f'\nДавление: {pressure}-мм.рт.ст'
                            f'\nВетер: {wind_speed}-м/с'
                            f'\nВосход солнца: {sunrise_timestamp}'
                            f'\nЗакат солнца: {sunset_timestamp}'
                            f'\nПродолжительность дня: {length_of_the_day}'
                            f'\n***** Хорошего дня *****')
    except:
        await massage.reply('\U0000262B Проверьте название города \U00002620')


if __name__ == '__main__':
    executor.start_polling(dp)
