from error import Error
import random


def validate(name: str, age: int) -> None:
    """Проверяет имя и возраст на оишбки."""
    name = cleaner(name)
    if age <= 0:
        raise Error('Возраст не может быть отрицательным числом')
    if age < 14:
        raise Error('Минимальный возраст - 14')
    if name == '':
        raise Error('Имя не может быть пустой строкой')
    if len(name) < 3:
        raise Error('Минимальное количесвто символов в имени - 3')
    if '' in name.split(' '):
        raise Error('Ненужный пробел')


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


def cleaner(name: str) -> str:
    """Очищает имя от пробелов в начале и конце."""
    return name.strip()


def game() -> None:
    """Выбирает рандомное число, а пользователь его отгадывает"""
    number: int = random.randint(0, 10)
    while True:
        try:
            num: int = int(input('Введите число:'))
            if num != number:
                print('Неверно. Попробуйте ещё раз(')
            else:
                print('Верно! Вы победили!')
                break
        except ValueError:
            print('Вам нужно ввести ЧИСЛО.')


def main() -> None:
    """Совершаются все действия."""
    while True:
        try:
            name, age = input('Введите имя: '), int(input("Введите возраст: "))
            validate(name, age)
            break
        except Error as e:
            print(f"Ошибка: {e}")
        except ValueError:
            print('Возраст должен быть числом.')

    print(advice_about_passport(age, name))
    game()


if __name__ == '__main__':
    main()

