import pytest
from src import process_bank

data = [
    {"description": "Перевод организации", "amount": 1000},
    {"description": "Открытие вклада", "amount": 5000},
    {"description": "Перевод с карты на карту", "amount": 200},
    {"description": "Оплата коммунальных услуг", "amount": 300},
    {"description": "Перевод на карту друга", "amount": 400}
]

categories = ["перевод", "вклад", "оплата"]

def test_search_found():
    result = process_bank.process_bank_search(data, "вклад")
    assert len(result) == 1
    assert result[0]["description"] == "Открытие вклада"

def test_search_case_insensitive():
    result = process_bank.process_bank_search(data, "ПЕРЕвод")
    assert len(result) == 3

def test_search_not_found():
    result = process_bank.process_bank_search(data, "заработная плата")
    assert result == []

def test_search_empty_string():
    result = process_bank.process_bank_search(data, "")
    assert len(result) == 5

def test_process_bank_counts():
    result = process_bank.process_bank(data, categories)
    assert result == {"перевод": 3, "вклад": 1, "оплата": 1}

def test_process_bank_empty_data():
    result = process_bank.process_bank([], categories)
    assert result == {"перевод": 0, "вклад": 0, "оплата": 0}

def test_process_bank_empty_categories():
    result = process_bank.process_bank(data, [])
    assert result == {}

def test_process_bank_case_insensitive():
    result = process_bank.process_bank(data, ["ВКЛАД", "пЕрЕвод"])
    assert result == {"ВКЛАД": 1, "пЕрЕвод": 3}