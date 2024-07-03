import datetime
import pytz
from exceptions import ValidationError


class Data:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._clear_whitespaces()

    def _clear_whitespaces(self):
        self.name = self.name.strip()


class DataWithDate(Data):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.timezone = pytz.timezone('Europe/Moscow')
        self.current_time = datetime.datetime.now(self.timezone)


class Validator:
    def __init__(self):
        self.data_history = []

    def _validate_name(self):
        name = self.data_history[-1].name
        if name == '':
            raise ValidationError('Имя не может быть пустой строкой.')
        if len(name) < 3:
            raise ValidationError('Минимальное количесвто символов в имени - 3.')
        if '' in name.split(' '):
            raise ValidationError('Ненужный пробел')

    def _validate_age(self):
        age = self.data_history[-1].age
        if age <= 0:
            raise ValidationError('Возраст не может быть отрицательным числом')
        if age < 14:
            raise ValidationError('Минимальный возраст - 14')

    def validate(self, data):
        self.data_history.append(data)
        self._validate_name()
        self._validate_age()




