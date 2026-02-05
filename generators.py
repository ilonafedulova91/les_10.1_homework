def filter_by_currency(transactions: list[dict], currency: str):

    if transactions == [] or transactions is None:
        raise ValueError('The data base is empty')

    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == '' or transaction['operationAmount']['currency']['code'] is None:
            raise ValueError('The currency code is empty')
        if transaction['operationAmount']['currency']['code'].isdigit():
            raise TypeError('The currency code is invalid')

        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction

def transaction_descriptions(transactions: list[dict]):
    if transactions == [] or transactions is None:
        raise ValueError('The data base is empty')
    for transaction in transactions:
        if transaction == {}:
            raise ValueError('The transaction is empty')
        if transaction['description'] == '':
            raise ValueError('The description is empty')
        yield transaction['description']

def card_number_generator(start: int, end: int):
    if start > end:
        raise ValueError('The start cannot be bigger than the end')
    if start < 0 or end < 0:
        raise ValueError('The start and end cannot be negative')
    if start < 1 or end > 9999999999999999:
        raise ValueError('Please enter a number in the range of 1 to 9999999999999999')
    for n in range(start, end + 1):
        card_number = f'{n:016d}'
        yield ' '.join(card_number[i:i+4] for i in range(0, 16, 4))