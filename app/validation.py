import datetime
import re


class Validation:
    """
    Класс для проверки строки.
    Методы:
        get_type: Возвращает тип проверяемой строки
        _date: Проверяет, является ли строка датой.
        _phone: Проверяет, является ли строка номером телефона.
        _email: Проверяет, является ли строка почтовым ящиком.
    """

    @classmethod
    def get_type(cls, validation_string: str) -> str:
        """
        :param validation_string: строка которую необходимо проверить.

        :return: Возвращает тип проверяемой строки.
                 Один из 4-х вариантов:
                    date - Дата.
                    phone - Телефон.
                    email - Почта.
                    text - Текст.
        """
        if cls._date(validation_string):
            return 'date'
        elif cls._phone(validation_string):
            return 'phone'
        elif cls._email(validation_string):
            return 'email'
        else:
            return 'text'

    @classmethod
    def _date(cls, validation_string: str) -> bool:
        """
        :param validation_string: строка которую необходимо проверить.

        :return: Возвращает True если строка является датой в одном из
                 двух форматов 'DD.MM.YYYY' или 'YYYY-MM-DD', иначе False.
        """
        try:
            regex_1 = r'(\d{2})[.](\d{2})[.](\d{4})$'  # DD.MM.YYYY
            regex_2 = r'(\d{4})[-](\d{2})[-](\d{2})$'  # YYYY-MM-DD

            match_1 = re.match(regex_1, validation_string)
            match_2 = re.match(regex_2, validation_string)

            if match_1:
                datetime.datetime(*(map(int, match_1.groups()[::-1])))
                return True

            if match_2:
                datetime.datetime(*(map(int, match_2.groups())))
                return True

        except ValueError:
            pass

        return False

    @classmethod
    def _phone(cls, validation_string: str) -> bool:
        """
        :param validation_string: строка которую необходимо проверить.

        :return: Возвращает True если строка является номером телефона
                 в формате '+7xxxxxxxxxx', иначе False.
        """
        try:
            if re.match(r'([ ]|[+])?[7]\d{10}', validation_string):
                return True

        except ValueError:
            pass

        return False

    @classmethod
    def _email(cls, validation_string: str) -> bool:
        """
        :param validation_string: строка которую необходимо проверить.

        :return: Возвращает True если строка является почтовым ящиком в
                 формате '*@*.*', иначе False.
        """
        try:
            regex = r'^(\w{1,100})[@](\w{1,10})[.](\w{1,4})$'
            match = re.match(regex, validation_string)
            if match:
                return True

        except ValueError:
            pass

        return False
