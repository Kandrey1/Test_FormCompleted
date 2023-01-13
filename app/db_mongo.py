from pymongo import MongoClient
from config import Settings


client = MongoClient(Settings.MONGODB_HOST, Settings.MONGODB_PORT)

db = client['FormsTemplates']

collection_forms = db['forms']


def insert_document(collection: db, data: dict) -> None:
    """
    Вставляет документ в коллекцию и возвращает id документа.

    :param collection: коллекция в которую необходимо добавить документ.
    :param data: документ(словарь) который необходимо добавить.
    :return: id добавленного документа.
    """
    return collection.insert_one(data).inserted_id


def search_form(field: str, value: str) -> list[dict]:
    """
    Ищет формы удовлетворяющие условиям и возвращает найденный
    результат списком.

    :param field: имя поля по которому будет произведен поиск.
    :param value: значение которое необходимо найти.
    :return: возвращает список содержащий документы удовлетворяющие поиску.
    """
    return list(collection_forms.find({field: value}))
