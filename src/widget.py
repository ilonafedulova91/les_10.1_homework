from src import masks


def mask_account_card(number: str) -> str:
    """This function masks both account and card numbers"""

    if number == "" or number is None:
        raise ValueError("Please enter account number or card number")
    if not isinstance(number, str):
        return ""

    number_splitted = number.split()

    if number_splitted[0].isdigit():
        raise TypeError("The first word must be a name of card or account")

    if number_splitted[0] == "Счет" or number_splitted[0] == "Счёт":
        account_number_masked = masks.get_mask_account(number_splitted[-1])
        account_masked = number_splitted[0] + " " + account_number_masked
        return str(account_masked)
    else:
        card_number_masked = masks.get_mask_card_number(number_splitted[-1])

        card_masked = " ".join(number_splitted[:-1])
        card_masked += " "
        card_masked += card_number_masked
        return str(card_masked)


def get_date(date_str: str) -> str:
    """This function transforms a date string"""

    if date_str == "":
        raise ValueError("Please enter date string")

    date_str = date_str[:10]
    splitted_date = date_str.split("-")

    for i in splitted_date:
        if not i.isdigit():
            raise TypeError("Date must be a number")

    return f"{splitted_date[-1]}.{splitted_date[-2]}.{splitted_date[-3]}"
