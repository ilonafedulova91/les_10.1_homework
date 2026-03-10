import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")


def convert_transaction(transaction: dict, url=BASE_URL) -> float:
    """This function converts a transaction into a floating point number in RUB"""

    if transaction == {}:
        raise ValueError("Transaction cannot be empty")

    currency = str(transaction.get("operationAmount", {}).get("currency", "").get("code", ""))
    value = float(transaction.get("operationAmount", {}).get("amount", "0"))

    if currency == "":
        raise ValueError("Currency cannot be empty")

    if currency == "RUB":
        return value
    else:
        headers = {"apikey": API_KEY}

        params = {"to": "RUB", "from": currency, "amount": value}

        response = requests.get(url=url, params=params, headers=headers)

        if response.status_code != 200:
            raise ValueError("Transaction cannot be converted to RUB")

        converted_transaction = response.json()
        return round(converted_transaction.get("result", 0), 2)
