import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """This function takes a bank operations data and a search string in it"""
    pattern = re.compile(search, re.IGNORECASE)

    result = []
    for transaction in data:
        description = transaction.get("description", "")
        if pattern.search(description):
            result.append(transaction)

    return result


def process_bank(data: list[dict], categories: list) -> dict:
    result = {category: 0 for category in categories}

    for transaction in data:
        description = transaction.get("description", "")

        for category in categories:
            if category.lower() in description.lower():
                result[category] += 1

    return result
