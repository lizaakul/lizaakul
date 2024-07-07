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
        if self._is_auth_file_exist():
            self._read_auth_file()

    def _is_auth_file_exist(self) -> bool:
        """Проверяет на наличие файла auth.txt в папке."""
        return os.path.isfile('auth.txt')

    def _read_auth_file(self):
        """Читает данные в файле auth.txt."""
        with open('auth.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if len(lines) >= 4:
                self.login: str = lines[0].strip()
                self.password: str = lines[1].strip()
                self.last_success_login_at: str = lines[2].strip()
                self.errors_count: int = int(lines[3])

    def authorize(self, login: str, password: str):
        """Авторизовывает вас."""
        if self.login is None or self.password is None:
            raise AuthorizationError("Пароль или логин не был найден.")

        if login == self.login.strip() and password == self.password.strip():
            print("Авторизация прошла успешно.")
            self.last_success_login_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self._update_auth_file()

        else:
            self.errors_count += 1
            self._update_auth_file()
            raise AuthorizationError("Неправильный логин или пароль")

    def _update_auth_file(self):
        """Обновляет файл auth.txt."""
        with open('auth.txt', 'w', encoding='utf-8') as f:
            f.write(f"{self.login}\n")
            f.write(f"{self.password}\n")
            f.write(f"{self.last_success_login_at}\n")
            f.write(f"{self.errors_count}\n")

    def registrate(self, login, password):
        """Регистрирует вас."""
        if self._is_auth_file_exist():
            raise RegistrationError('Произошла ошибка региcтрации.')
        if self.login is not None:
            raise RegistrationError('Логин уже существует')

        self.login: str = login
        self.password: str = password
        self.errors_count: int = 0
        self.last_success_login_at: datetime = datetime.datetime.now()
        self._update_auth_file()




