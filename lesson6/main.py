from Authenticator import Authenticator
from RegistrationError import RegistrationError
from AuthorizationError import AuthorizationError
from functools import wraps


def repeat_until_true(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                if func(*args, **kwargs):
                    break
            except (AuthorizationError and RegistrationError) as e:
                print(e)
    return wrapper


@repeat_until_true
def main():
    """Проверяет вас нужно зарегистрироваться или авторизоваться, приветсвует вас."""
    a = Authenticator()
    if a.login is None:
        print('Пройдите регистрацию.')
        reg: bool = False
    else:
        print("Введите почту и пароль для авторизации.")
        reg: bool = True
    while True:
        login: str = input('Введите почту:')
        password: str = input('Введите пароль:')
        if not reg:
            try:
                a.registrate(login, password)
                reg: bool = True
                print('Вы успешно зарегестрировались. Теперь авторизуйтесь')
            except RegistrationError as e:
                print(e)

        else:
            try:
                a.authorize(login, password)
                print(f'Добро пожаловать {login}!')
                print(f'Время регистрации:{a.last_success_login_at}')
                print(f"Количество ошибок:{a.errors_count}")
                return True
            except AuthorizationError as e:
                print(e)


if __name__ == '__main__':
    main()




