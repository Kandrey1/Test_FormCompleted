from main import app


client = app.test_client()


def script_test() -> list[list, dict]:
    """
    Тестирующий скрипт.
    """
    base = 'http://127.0.0.1:5000/get_form?'
    urls = [
        f'{base}user_phone=+79634556487&user_email=sads@dsd.hwe&user_login=sdfafasdfsdf5',
        f'{base}user_phone=+79653456487&user_login=sdfafasdfsdf5',
        f'{base}client_phone=+79604564587&date_buy=2017-10-15',
        f'{base}user_login=+79604564587&date_reg=25.11.2018',
        f'{base}login_user=7fhdjjdj64587&article=25-11.2018&article=21.01.2018',
        f'{base}login_us=7fhdjjdj64587&article=25-11.2018&article2=21.01.2018',
        f'{base}user_login=oneuse&user_phone=+78451475327&article=redwhite&date_create=15.05.2020&user_email=mail@gm.ru',
        f'{base}user_log=oneuse&user_phone=+784581475327&article=redwhite&date_create=42.05.2020&user_email=mail@gmru'
    ]

    datas = list()
    for url in urls:
        response = client.post(url)
        datas.append(response.json)

    return datas
