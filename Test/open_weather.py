import datetime
from config import open_weather_key
import requests
from pprint import pprint
def get_weather(city, open_weather_key):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_key}&units=metric"
        )
        data = r.json()
        # pprint(data)
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

        print(f'**** {datetime.datetime.now().strftime("%d-%m-%Y %H:%M")} ****'
              f'\nПогода в городе: {city}'
              f'\nТемпаратура: {temp}°С {wd}'
              f'\nВлажность: {humidity}%'
              f'\nДавление: {pressure}-мм.рт.ст'
              f'\nВетер: {wind_speed}-м/с'
              f'\nВосход солнца: {sunrise_timestamp}'
              f'\nЗакат солнца: {sunset_timestamp}'
              f'\nПродолжительность дня: {length_of_the_day}'
              f'\nХорошего дня')


    except Exception as ex:
        print(ex)
        print('Проверьте название города!')

def main():
    city = input('Введите город: ')
    get_weather(city, open_weather_key)

if __name__ == '__main__':
    main()