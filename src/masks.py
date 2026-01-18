from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """This function returns a hidden card number"""
    number_str = str(card_number)

    card_masked = number_str[:4] + " " + number_str[4:6] + "*" * 2 + " " + "*" * 4 + " " + number_str[12:]
    return card_masked


def get_mask_account(account_number: Union[int, str]) -> str:
    """This function returns a hidden account number"""
    number_str = str(account_number)

    account_masked = "*" * 2 + number_str[-4:]
    return account_masked
