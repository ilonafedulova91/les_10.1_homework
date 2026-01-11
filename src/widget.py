import masks

def mask_account_card (number: str) -> str:

    number_splitted = number.split()

    if number_splitted[0] == 'Счет' or number_splitted[0] == 'Счёт':
        account_number_masked = masks.get_mask_account(number_splitted[-1])
        account_masked = number_splitted[0] + ' ' + account_number_masked
        return account_masked
    else:
        card_number_masked = masks.get_mask_card_number(number_splitted[-1])

        card_masked = ' '.join(number_splitted[:-1])
        card_masked += ' '
        card_masked += card_number_masked
        return card_masked