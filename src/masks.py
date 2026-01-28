from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """This function returns a hidden card number"""

    if card_number == 0 or card_number == "" or card_number is None:
        raise ValueError("Card number is empty")

    number_str = str(card_number).replace(" ", "")

    if len(number_str) != 16:
        raise ValueError("Card number is invalid")

    card_masked = number_str[:4] + " " + number_str[4:6] + "*" * 2 + " " + "*" * 4 + " " + number_str[12:]
    return card_masked


def get_mask_account(account_number: Union[int, str]) -> str:
    """This function returns a hidden account number"""

    if account_number == 0 or account_number == "" or account_number is None:
        raise ValueError("Account number is empty")

    number_str = str(account_number).replace(" ", "")

    if len(number_str) != 20:
        raise ValueError("Account number is invalid")

    account_masked = "*" * 2 + number_str[-4:]
    return account_masked
