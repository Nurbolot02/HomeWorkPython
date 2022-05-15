# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
import random
from useFulFutires.IsNumber import isNumber



def candyMultiplayer(candyCount):
    print('\nДобро пожаловать в игру Конфетка ')
    print('Условие Игры: \nНа столе лежит 2021 конфет.'
          'Первый ход определяется жеребьёвкой. \nЗа один ход можно забрать не более чем 28 конфет. '
          '\nВсе конфеты оппонента достаются сделавшему последний ход.\n')
    players = [input('Введите имя 1 - игрока: '), input('Введите имя 2 - игрока: ')]
    f = True
    while f:
        print('1 - Начать жеребьёвку \n0 - Завершение игры')
        numberText = 'Выберите операцию: '
        userAnswer = isNumber(numberText)
        if userAnswer == 1:
            userMove = random.randint(0, 1)
        elif userAnswer == 0:
            print('\nGoodbye! \nSee you later!\n')
            f = False
            break
        candyCountReserv = candyCount
        f = True
        while f:
            print(f'\nКонфет осталось {candyCount}')
            print(f'Ходит игрок: {players[userMove]}')
            print(f'Для выхода из игры введите 10000')
            while True:
                numberText = f'{players[userMove]} сколько конфет хотите забрать? '
                userAnswer = isNumber(numberText)
                if userAnswer == 10000:
                    print('\nGoodbye! \nSee you later!')
                    f = False
                    break
                elif (userAnswer > 0 and userAnswer <= 28) and userAnswer <= candyCount:
                    candyCount -= userAnswer
                    break
                elif userAnswer > candyCount:
                    print(f'Осталось только {candyCount} конфет')
                else:
                    print('За один ход можно забрать не меньше 0 и не более чем 28 конфет!')
            if candyCount == 0:
                print(f'Поздравляем {players[userMove]} вы победили!')
                while True:
                    print('\n1 - Начать новую игру \n0 - Завершение игры')
                    numberText = 'Выберите операцию: '
                    userAnswer = isNumber(numberText)
                    if userAnswer == 1:
                        userMove = random.randint(0, 1)
                        candyCount = candyCountReserv
                        break
                    elif userAnswer == 0:
                        f = False
                        break

            if userMove == 0:
                userMove = 1
            else:
                userMove = 0

def candyBot(candyCount):
    print('\nДобро пожаловать в игру Конфетка ')
    print('Условие Игры: \nНа столе лежит 2021 конфет.'
          'Первый ход определяется жеребьёвкой. \nЗа один ход можно забрать не более чем 28 конфет. '
          '\nВсе конфеты оппонента достаются сделавшему последний ход.\n')
    player = [input('Введите имя: '), 'Компьютер']
    f = True
    while f:
        print('1 - Начать жеребьёвку \n0 - Завершение игры')
        numberText = 'Выберите операцию: '
        userAnswer = isNumber(numberText)
        if userAnswer == 1:
            userMove = random.randint(0, 1)
        elif userAnswer == 0:
            print('\nGoodbye! \nSee you later!\n')
            f = False
            break
        candyCountReserv = candyCount
        f = True
        while f:
            print(f'\nКонфет осталось {candyCount}')
            print(f'Ходит : {player[userMove]}')
            print(f'Для выхода из игры введите 10000')
            while True:
                if userMove == 0:
                    numberText = f'{player[userMove]} сколько конфет хотите забрать? '
                    userAnswer = isNumber(numberText)
                    if userAnswer == 10000:
                        print('\nGoodbye! \nSee you later!')
                        f = False
                        break
                    elif (userAnswer > 0 and userAnswer <= 28) and userAnswer <= candyCount:
                        candyCount -= userAnswer
                        break
                    elif userAnswer > candyCount:
                        print(f'Осталось только {candyCount} конфет')
                    else:
                        print('За один ход можно забрать не меньше 0 и не более чем 28 конфет!')
                else:
                    while True:
                        randomNumber = random.randint(1, 29)
                        if (candyCount - randomNumber) >= 0:
                            candyCount -= randomNumber
                            print(f'Компьютер забрал {randomNumber} конфет')
                            break
                    break
            if candyCount == 0:
                print(f'Поздравляем {player[userMove]} вы победили!')
                while True:
                    print('\n1 - Начать новую игру \n0 - Завершение игры')
                    numberText = 'Выберите операцию: '
                    userAnswer = isNumber(numberText)
                    if userAnswer == 1:
                        userMove = random.randint(0, 1)
                        candyCount = candyCountReserv
                        break
                    elif userAnswer == 0:
                        f = False
                        break

            if userMove == 0:
                userMove = 1
            else:
                userMove = 0

def candyCleverBot(candyCount, maxCountCandy = 28):
    print('\nДобро пожаловать в игру Конфетка ')
    print('Условие Игры: \nНа столе лежит 2021 конфет.'
          'Первый ход определяется жеребьёвкой. \nЗа один ход можно забрать не более чем 28 конфет. '
          '\nВсе конфеты оппонента достаются сделавшему последний ход.\n')
    player = [input('Введите имя: '), 'Умный компьютер']
    f = True
    while f:
        print('1 - Начать жеребьёвку \n0 - Завершение игры')
        numberText = 'Выберите операцию: '
        userAnswer = isNumber(numberText)
        if userAnswer == 1:
            userMove = random.randint(0, 1)
        elif userAnswer == 0:
            print('\nGoodbye! \nSee you later!\n')
            f = False
            break
        candyCountReserv = candyCount
        firstMove = userMove
        f = True
        while f:
            print(f'\nКонфет осталось {candyCount}')
            print(f'Ходит : {player[userMove]}')
            print(f'Для выхода из игры введите 10000')
            while True:
                if userMove == 0:
                    numberText = f'{player[userMove]} сколько конфет хотите забрать? '
                    userAnswer = isNumber(numberText)
                    if userAnswer == 10000:
                        print('\nGoodbye! \nSee you later!')
                        f = False
                        break
                    elif (userAnswer > 0 and userAnswer <= 28) and userAnswer <= candyCount:
                        candyCount -= userAnswer
                        print(f'{player[0]} забрал {userAnswer} конфет')
                        break
                    elif userAnswer > candyCount:
                        print(f'Осталось только {candyCount} конфет')
                    else:
                        print('За один ход можно забрать не меньше 0 и не более чем 28 конфет!')
                else:
                    if candyCount == candyCountReserv or candyCountReserv == candyCountReserv - userAnswer:
                        if firstMove == 1:
                            compMove = candyCount % 28
                            candyCount -= compMove
                        else:
                            compMove = round((candyCountReserv % maxCountCandy) * maxCountCandy)
                            if userAnswer == maxCountCandy:
                                candyCount -= maxCountCandy
                            elif maxCountCandy - userAnswer + compMove <= maxCountCandy:
                                compMove = maxCountCandy - userAnswer + compMove
                                candyCount -= compMove
                            else:
                                compMove = maxCountCandy - userAnswer
                                candyCount -= compMove
                    else:
                        if candyCount == maxCountCandy:
                            compMove = maxCountCandy
                            candyCount -= compMove
                        elif candyCount < maxCountCandy:
                            compMove = maxCountCandy - candyCount
                            candyCount -= compMove
                        elif firstMove == 1 and candyCount >= maxCountCandy  :
                            if userAnswer == maxCountCandy :
                                compMove = maxCountCandy - 1
                                candyCount -= maxCountCandy - 1
                            else:
                                if maxCountCandy - userAnswer - 1 > 0:
                                    compMove = maxCountCandy - userAnswer - 1
                                    candyCount -= compMove
                                else:
                                    compMove = maxCountCandy - userAnswer
                                    candyCount -= compMove
                        else:
                            if userAnswer == maxCountCandy and candyCount >= maxCountCandy:
                                compMove = maxCountCandy
                                candyCount -= maxCountCandy
                            else:
                                if candyCount >= maxCountCandy:
                                    compMove = maxCountCandy - userAnswer
                                    candyCount -= compMove


                    print(f'Компьютер забрал {compMove} конфет')
                    break
            if candyCount == 0:
                print(f'\nПоздравляем {player[userMove]} вы победили!\n')
                if firstMove == 0:
                    firstMove = 1
                else:
                    firstMove = 0
                while True:
                    print('\n1 - Начать новую игру \n0 - Завершение игры')
                    numberText = 'Выберите операцию: '
                    userAnswer = isNumber(numberText)
                    if userAnswer == 1:
                        userMove = random.randint(0, 1)
                        candyCount = candyCountReserv
                        break
                    elif userAnswer == 0:
                        f = False
                        break

            if userMove == 0:
                userMove = 1
            else:
                userMove = 0


while True:
    print('\nТипы игр')
    print('1 - Человек против человека \n2 - Человек против  бота \n3 - Человек против Умного бота \n0 - Выход из игры')
    numberText = 'Выберите операцию: '
    userAnswer = isNumber(numberText)
    maxCountCandy = 28
    candyCount = 100
    if userAnswer == 0:
        print('\nGoodbye! \nSee you later!')
        break
    elif userAnswer == 1:
        candyMultiplayer(candyCount)
    elif userAnswer == 2:
        candyBot(candyCount)
    elif userAnswer == 3:
        candyCleverBot(candyCount, maxCountCandy)