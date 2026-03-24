from unittest.mock import Mock, patch

import pytest

from src.external_api import convert_transaction


def test_convert_transaction_rub():
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {
                "code": "RUB",
            },
        }
    }

    result = convert_transaction(transaction)

    assert result == 100


def test_convert_transaction_usd_success():
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {
                "code": "USD",
            },
        }
    }

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 9000}

    with patch("external_api.requests.get", return_value=mock_response):
        result = convert_transaction(transaction)

    assert result == 9000


def test_convert_transaction_usd_error():
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {
                "code": "USD",
            },
        }
    }

    mock_response = Mock()
    mock_response.status_cose = 500

    with patch("external_api.requests.get", return_value=mock_response):
        with pytest.raises(ValueError):
            convert_transaction(transaction)


def test_convert_transaction_empty_transaction():
    with pytest.raises(ValueError):
        convert_transaction({})


def test_convert_transaction_usd_empty_currency():
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {
                "code": "",
            },
        }
    }

    with pytest.raises(ValueError):
        convert_transaction(transaction)
