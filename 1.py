import datetime
import pytz
import random
from Valudator import Validator, DataWithDate
from exceptions import ValidationError


def advice_about_passport(age: int, name: str) -> str | None:
    """Приветствует пользователя и напоминает получить или сменить паспорт."""
    welcome = f'Привет {name}! Тебе {age}.'
    if age == 16 or age == 17:
        return f'{welcome} Не забудьте получить паспорт'
    if age == 25 or age == 26:
        return f'{welcome}Не забудьте сменить паспорт'
    if age == 45 or age == 46:
        return f'{welcome}Не забудьте заменить паспорт во второй раз'

    print(welcome)


def game() -> None:
    """Выбирает рандомное число, а пользователь его отгадывает"""
    number: int = random.randint(0, 10)
    while True:
        try:
            num: int = int(input('* Введите число:'))
            if num != number:
                print('Неверно. Попробуйте ещё раз(')
            else:
                print('Верно! Вы победили!')
                break
        except ValueError:
            print('Вам нужно ввести ЧИСЛО.')


def main() -> None:
    timezone = pytz.timezone('Europe/Moscow')
    v = Validator()
    first_time = datetime.datetime.now(timezone)
    mistakes: int = 0
    while True:
        name = input('Введите имя: ')
        age = int(input("Введите возраст: "))
        data = DataWithDate(name, age)
        try:
            v.validate(data)
            last_time = datetime.datetime.now(timezone)
            break
        except ValidationError as e:
            mistakes += 1
            print(f"!!Ошибка: {e}!!")
        except ValueError:
            mistakes += 1
            print('!!Возраст должен быть ЧИСЛОМ!!')

    print(advice_about_passport(data.age, data.name))
    if mistakes > 0:
        print(f"Количество сделанных ошибок: {mistakes}")
        print(f"Время первой ошибки: {first_time.strftime("%H:%M:%S")}")
        print(f"Время последней ошибки: {last_time.strftime("%H:%M:%S")}")
        a = last_time - first_time
        print(f'Прошло времени:{a}')
    game()


if __name__ == '__main__':
    main()
