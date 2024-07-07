import datetime
import os
from AuthorizationError import AuthorizationError
from RegistrationError import RegistrationError


class Authenticator:
    def __init__(self):
        self.login: str | None = None
        self.password: str | None = None
        self.last_success_login_at: datetime = None
        self.errors_count: int = 0
        if self._is_auth_file_exist:
            self._read_auth_file()

    def _is_auth_file_exist(self) -> bool:
        return os.path.isfile('auth.txt')

    def _read_auth_file(self):
        with open('auth.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if len(lines) >= 4:
                self.login = lines[0]
                self.password = lines[1]
                self.last_success_login_at = lines[2]
                self.errors_count = int(lines[3])

    def authorize(self, login: str, password: str):
        if self.login is None or self.password is None:
            raise AuthorizationError("Пароль или логин не был найден.")

        if login == self.login and password == self.password:
            print("Авторизация прошла успешно")
            self.last_success_login_at = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            self.errors_count = 0
            self._update_auth_file()

        else:
            self.errors_count += 1
            self._update_auth_file()
            raise AuthorizationError("Неправильный логин или пароль")

    def _update_auth_file(self):
        with open('auth.txt', 'w', encoding='utf-8') as f:
            f.write(f"{self.login}")
            f.write(f"{self.password}")
            f.write(f"{self.last_success_login_at}")
            f.write(f"{self.errors_count}")

    def registrate(self, login, password):
        #if self._is_auth_file_exist():
            #raise RegistrationError('Произошла ошибка регитрации.')
        if self.login is not None:
            raise RegistrationError('Логин уже существует')

        self.login = login
        self.password = password
        self.errors_count = 0
        self.last_success_login_at = datetime.datetime.now()
        self._update_auth_file()




