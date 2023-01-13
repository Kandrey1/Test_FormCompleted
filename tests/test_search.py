from app.search import SearchForm


def test_formatting_data_request():
    """Форматирование аргументов из запроса."""
    data1 = {'email1': 'asd@sdf.bgf', 'phone1': '+79682233415',
             'date1': '2022-12-25'}
    data2 = {'email1': 'asd@sdfbgf', 'text1': '+79682233415',
             'date2': '12.10.1981'}

    res1 = SearchForm._formatting_data_request(data1)
    res2 = SearchForm._formatting_data_request(data2)

    assert res1 == {'email1': 'email', 'phone1': 'phone', 'date1': 'date'}
    assert res2 == {'email1': 'text', 'text1': 'phone', 'date2': 'date'}

# def test_search_all_docs():

# def test_get_set_name_templates():

# def test_get()
