import pytest


def format_price(price: str) -> str:

    try:
        price_float = float(price)
        price_str = f"{price_float:.2f}"
        integer_part, decimal_part = price_str.split(".")
        formatted_parts = []
        for i in range(len(integer_part), 0, -3):
            start = max(0, i - 3)
            formatted_parts.insert(0, integer_part[start:i])
        return " ".join(formatted_parts) + "." + decimal_part
    except (ValueError, AttributeError):
        return price


@pytest.mark.parametrize("test_data, expected", [
    ("0", "0.00"),
    ("5", "5.00"),
    ("-5", "-5.00"),
    ("20", "20.00"),
    ("999", "999.00"),
    ("1000", "1 000.00"),
    ("12345", "12 345.00"),
    ("123456", "123 456.00"),
    ("1000000", "1 000 000.00"),
    ("1000000000", "1 000 000 000.00"),
    ("10.5", "10.50"),
    ("11.50", "11.50"),
    ("0.1", "0.10"),
    ("10.123", "10.12"),
    ("10.129", "10.13"),
    ("10.666", "10.67"),
    ("19.999", "20.00"),
    ("0.004", "0.00"),
    ("  123  ", "123.00"),
    ])
def test_format_price_positive(test_data, expected):
    assert format_price(test_data) == expected


@pytest.mark.parametrize("test_data", [
    "ABC", "ABC",
    "12.34.56", "12.34.56",
    "%#$@!!!!", "%#$@!!!!",
    "", "",
])
def test_format_price_invalid_strings(test_data):
    assert format_price(test_data) == test_data


""" Тут указан неправильный тип ошибки в except.
Когда у нас в format_price(None), возникает ошибка TypeError. Но в блоке except её нет.
"""
