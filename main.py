from flask import request

from app import create_app
from app.search import SearchForm
from create_test_data import create_data


app = create_app()


@app.route("/", methods=['GET'])
def index():
    """Главная страница приложения."""
    return {'Home page': 'Welcome'}


@app.route("/get_form", methods=['POST'])
def get_form():
    """Страница получения форм."""
    try:
        if request.method == "POST":
            args_request = request.args.to_dict()
            response = SearchForm.get(args_request)

    except Exception as e:
        return {'Error': f'Unknown bug:<{e}>'}

    return response


@app.route("/test_data/create", methods=['GET'])
def create_test_data():
    """Создание начальных данных."""
    try:
        if request.method == "GET":
            create_data()

    except Exception:
        return {'Message': 'Error create data'}

    return {'Message': 'Data created'}


@app.route("/script_test/start", methods=['GET'])
def script_testing():
    """Тестовый скрипт."""
    try:
        from script_for_test import script_test

        if request.method == "GET":
            response = script_test()

    except Exception:
        return {'Message': 'Error create data'}

    return {'Message': response}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
