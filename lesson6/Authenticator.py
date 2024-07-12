import datetime
import hashlib
import os
import json
from AuthorizationError import AuthorizationError
from RegistrationError import RegistrationError
import re


class Authenticator:
    def __init__(self):
        self.login: str | None = None
        self.password = None
        self.last_success_login_at: datetime = None
        self.errors_count: int = 0
        if self._is_auth_file_exist():
            self._read_auth_file()

    @staticmethod
    def _is_auth_file_exist() -> bool:
        """Проверяет на наличие файла auth.txt в папке."""
        return os.path.isfile('auth.json')

    def _read_auth_file(self):
        """Читает данные в файле auth.txt."""
        with open('auth.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.login = data['login']
            self.password = data['password']
            self.last_success_login_at = data['last_success_login_at']
            self.errors_count = data['errors_count']

    def authorize(self, login: str, password: str):
        """Авторизовывает вас."""
        if self.login is None or self.password is None:
            raise AuthorizationError("Пароль или логин не был найден.")

        if login == self.login.strip() and Validator().hash(password) == self.password:
            print("Авторизация прошла успешно.")
            self._update_auth_file()

        else:
            self.errors_count += 1
            self._update_auth_file()
            raise AuthorizationError("Неправильный логин или пароль")

    def _update_auth_file(self):
        """Обновляет файл auth.txt."""
        with open('auth.json', 'w', encoding='utf-8') as f:
            data = {
                'login': self.login,
                'password': self.password,
                'last_success_login_at': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'errors_count': 0
            }
            json.dump(data, f)

    def registrate(self, login, password):
        """Регистрирует вас."""
        validate = Validator()
        if self._is_auth_file_exist():
            raise RegistrationError('Произошла ошибка региcтрации.')
        if self.login is not None:
            raise RegistrationError('Почта уже существует')
        validate.validate_email(login)
        validate.validate_password(password)

        self.login = login
        self.password = validate.hash(password)
        self.last_success_login_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.errors_count = 0
        self._update_auth_file()


class Validator:
    def __init__(self):
        self.password_bytes = None
        self.salt = None
        self.hash_password = None
        self.pattern = re.compile(
            r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{4,}$'
        )

    def validate_email(self, login: str):
        """Валидация почты"""
        email_regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        )
        if not email_regex.match(login):
            raise RegistrationError("Неправильная форма почты")
        else:
            return True

    def validate_password(self, password: str):
        """Валидация пароля"""
        if not self.pattern.match(password):
            raise RegistrationError('В пароле у вас должно быть минимум 4 символа, минимум 1 заглавный символ, '
                                    'минимум 1 прописной символ, минимум 1 цифра, минимум 1 спецсимвол.')
        else:
            print('Все хорошо')
            return True

    @staticmethod
    def hash(password):
        """Хеширование пароля."""
        hasher = hashlib.sha256()
        hasher.update(password.encode('utf-8'))
        return hasher.hexdigest()
