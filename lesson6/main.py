from Authenticator import Authenticator
from RegistrationError import RegistrationError
from AuthorizationError import AuthorizationError


def main():
    """Проверяет вас нужно зарегистрироваться или авторизоваться, приветсвует вас."""
    a = Authenticator()
    if a.login is None:
        print('Пройдите регистрацию.')
        reg: bool = False
    else:
        print("Введите логин и пароль для авторизации.")
        reg: bool = True
    while True:
        login: str = input('Введите логин:')
        password: str = input('Введите пароль:')
        if not reg:
            try:
                a.registrate(login, password)
                reg: bool = True
                print('Вы успешно зарегестрировались. Теперь авторизуйтесь')
            except RegistrationError as e:
                return e

        else:
            try:
                a.authorize(login, password)
                break
            except AuthorizationError as e:
                print(e)

    print(f'Добро пожаловать {login}!')
    print(f'Время регистрации:{a.last_success_login_at}')
    print(f"Количество ошибок:{a.errors_count}")


if __name__ == '__main__':
    print(main())




