# Запуск
# Подключаем нужные библиотеки*
from random import *

# Создаем функции
# Приветствие
def privet():
    print('Добро пожаловать в числовую угадайку!')
    print()
    print('Правила игры простые:')
    print('1) В начале игры на ваш баланс поступает 1000 игровых очков')
    print('2) Вы ставите ставку: минимум 100 очков и максимум все ваши очки')
    print('3) Я загадываю число от 0 до 100, ваша задача его угадать')
    print('4) Количество ваших попыток ограничено лишь только вашей ставкой')
    print('5) Если вы отвечаете неправильно, за каждую попытку я вычитаю по 10 баллов из вашей ставки')
    print('Если вы отвечаете правильно я удваиваю оставшееся количество баллов в вашей ставке')
    print()

#Обьявление начального баланса
def start_balance(total):
    print('Ваш начальный баланс равен:', total)
    print()
    return total

# Ставим ставку
def do_stavka(total):
    print('Введите вашу ставку!')
    f = True
    while f:
        stv = int(input())
        if stv <= total and stv >= 100:
            print()
            print('Ваша ставка равна:', stv)
            print()
            total -= stv
            print(total)
            f = False
            return total, stv
        else:
            print('Введите корректную ставку')

# Загадываем число
def zagad_ch():
    n = randint(0,101)
    print('Я загадал число попробуй его угадать!')
    return n

# игровая логика
def main_program(a, b, total, stv, n):
    while a > 0:
        b += 1
        vvod = int(input())
        if vvod == n:
            print('Вы угадали загаданное число! Поздравляем!')
            print('Количество попыток:', b)
            stv *= 2
            total += stv
            print('Ваш баланс равен:', total)
            return total
            break
        elif vvod < n:
            stv -= 10
            print('Ваша ставка теперь равна:', stv)
            print('Слишком мало, попробуйте еще раз!')
            continue
        elif vvod > n:
            stv -= 10
            print('Ваша ставка теперь равна:', stv)        
            print('Слишком много, попробуйте еще раз!')
            continue
        
# вызов игровой логики
def igra(total):
    while total != 0 and total != 3000:
        total, stv = do_stavka(total)
        n = zagad_ch()
        b = 0
        a = 1
        total = main_program(a, b, total, stv, n)


# Основная программа
total = 1000
privet()
start_balance(total)
igra(total)