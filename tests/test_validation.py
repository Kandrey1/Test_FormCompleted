from app.validation import Validation


def test_validation_date():
    """Проверка является ли строка датой в формате 'DD.MM.YYYY'
       или 'YYYY-MM-DD'.
    """
    d1 = '12.12.2022'
    d2 = '32.12.2022'
    d3 = '15.14.2023'
    d4 = '19.11.20235'
    d5 = '12.12-2022'

    d6 = '2023-12-18'
    d7 = '2023-13-18'
    d8 = '2023-13-45'
    d9 = '12023-09-27'
    d10 = '2023.12-18'

    assert Validation._date(validation_string=d1) is True
    assert Validation._date(validation_string=d2) is False
    assert Validation._date(validation_string=d3) is False
    assert Validation._date(validation_string=d4) is False
    assert Validation._date(validation_string=d5) is False
    assert Validation._date(validation_string=d6) is True
    assert Validation._date(validation_string=d7) is False
    assert Validation._date(validation_string=d8) is False
    assert Validation._date(validation_string=d9) is False
    assert Validation._date(validation_string=d10) is False


def test_validation_phone():
    """Проверка является ли строка номером телефона."""

    n1 = '+79478652347'
    n2 = '89478652347'
    n3 = '+712375a9347'
    n4 = '+21237552347'

    assert Validation._phone(validation_string=n1) is True
    assert Validation._phone(validation_string=n2) is False
    assert Validation._phone(validation_string=n3) is False
    assert Validation._phone(validation_string=n4) is False


def test_validation_email():
    """Проверка является ли строка почтовым ящиком."""

    e1 = 'abs@qw.rt'
    e2 = 'ab23s@qw223.rt23'
    e3 = 'absqw.rt'
    e4 = 'abs@qwrt'

    assert Validation._email(validation_string=e1) is True
    assert Validation._email(validation_string=e2) is True
    assert Validation._email(validation_string=e3) is False
    assert Validation._email(validation_string=e4) is False


def test_validation_get_type():
    """Получить тип строки."""
    str_1 = '+79478652347'
    str_2 = 'abs@qw.rt'
    str_3 = '12.12.2022'
    str_4 = '12.122022'

    assert Validation.get_type(validation_string=str_1) == 'phone'
    assert Validation.get_type(validation_string=str_2) == 'email'
    assert Validation.get_type(validation_string=str_3) == 'date'
    assert Validation.get_type(validation_string=str_4) == 'text'
