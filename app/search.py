from typing import Union

from app.db_mongo import search_form
from app.validation import Validation


class SearchForm:
    """
    Класс для поиска форм по запросу.
    Методы:
        get:
    """
    @classmethod
    def get(cls, arg_request: dict) -> Union[list[str], dict]:
        """
        Получает данные из запроса(словарь) и возвращает список названий форм
        удовлетворяющих запросу, иначе возвращает
        словарь {'имя поля': 'тип значения'}.

        :param arg_request: аргументы в запросе.
        :return: Возвращает список названий форм.
        """
        formatting_dct = cls._formatting_data_request(arg_request)
        all_docs = cls._search_all_docs(formatting_dct)
        templates = cls._get_set_name_templates(all_docs, formatting_dct)

        return templates if templates else formatting_dct

    @classmethod
    def _formatting_data_request(cls, arg_request: dict) -> dict:
        """
        Преобразует данные из запроса. Значения полей преобразуются в их тип.
        Возвращается словарь {'имя поля': 'тип значения'}.
        :param arg_request: данные из запроса.
        :return: словарь {'имя поля': 'тип значения'}
        """
        dct = dict()
        for key, val in arg_request.items():
            dct[key] = Validation.get_type(val)
        return dct

    @classmethod
    def _search_all_docs(cls, dct_format: dict) -> list[dict]:
        """
        Ищет совпадение по каждому ключу в БД, и результаты собирает в список.
        Возвращает список словарей.
        :param dct_format: словарь содержащий имя поля и значение.
        :return: Список словарей.
        """
        all_docs = list()
        for k, v in dct_format.items():
            all_docs.extend(search_form(k, v))

        return all_docs

    @classmethod
    def _get_set_name_templates(cls, all_docs: list,
                                dct_format: dict) -> list[str]:
        """
        Возвращает список названия шаблонов, если такие есть.
        Сравнивает документ полученный из БД на соответствие параметрам
        запроса. Если все поля в документе есть в запросе, имя документа
        добавляется к результату.

        :param all_docs: список словарей из БД, полученных в результате поиска.
        :param dct_format: словарь данных из запроса в
                           формате {'имя поля': 'тип значения'}
        :return: список названия шаблонов, если такие есть.
        """
        ignore = ['_id', 'name']
        name_templates = set()

        for item in all_docs:
            cnt = 0
            for k in item.keys():
                if k not in ignore and dct_format.get(k) == item[k]:
                    cnt += 1

            if cnt == len(item) - 2:
                name_templates.add(item['name'])

        return list(name_templates)
