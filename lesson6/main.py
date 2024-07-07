from Authenticator import Authenticator
from RegistrationError import RegistrationError
from AuthorizationError import AuthorizationError


def main():
    a = Authenticator()
    if a.login is None:
        print('Пройдите регистрацию.')
        reg = False
    else:
        print("Введите логин и пароль для авторизации.")
        reg = True
    while True:
        login = input('Введите логин:')
        password = input('Введите пароль:')
        if not reg:
            try:
                a.registrate(login, password)
                reg = True
            except RegistrationError as e:
                print(e)

        else:
            try:
                a.authorize(login, password)
                break
            except AuthorizationError as e:
                print(e)

    print(f'Добро пожаловать {login}.')
    print(a.last_success_login_at)
    print(a.errors_count)


if __name__ == '__main__':
    main()




