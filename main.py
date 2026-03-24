from pathlib import Path

from src import data_loader, generators, process_bank, processing, utils, widget

PROJECT_DIR = Path(__file__).parent


def main():
    # choosing file type to work with
    menu_dict = {
        1: ["JSON", f"{PROJECT_DIR}/data/operations.json"],
        2: ["CSV", f"{PROJECT_DIR}/data/transactions.csv"],
        3: ["XLSX", f"{PROJECT_DIR}/data/transactions_excel.xlsx"],
    }

    while True:
        try:
            menu = int(
                input(
                    """
    Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла\t
    """
                )
            )
            if menu in menu_dict:
                break
        except ValueError:
            print("\tВведите число от 1 до 3.\n")

    file_type, file_path = menu_dict[menu]

    print(f"\tДля обработки выбран {file_type}-файл.\n")

    if menu == 1:
        loaded_data = utils.load_json_operations(file_path)
    elif menu == 2:
        loaded_data = data_loader.read_csv(file_path)
    elif menu == 3:
        loaded_data = data_loader.read_excel(file_path)

    statuses = ["EXECUTED", "CANCELED", "PENDING"]

    # choosing status to work with
    status = str(
        input(
            """
    Введите статус, по которому необходимо выполнить фильтрацию. 
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\t
    """
        )
    )

    while status.upper() not in statuses:
        status = input(
            f"""
    Статус операции "{status}" недоступен.
    Введите статус, по которому необходимо выполнить фильтрацию. 
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\t
    """
        )

    # sorting by state
    result = processing.filter_by_state(list_of_dicts=loaded_data, state=status.upper())

    print(f'\tОперации отфильтрованы по статусу "{status}"\n\t')

    answers = {"да": True, "нет": False}
    answers_descending = {"по убыванию": True, "по возрастанию": False}

    # sorting by date in desc/asc order
    date_sort = str(input("\tОтсортировать операции по дате? Да/Нет\n\t"))

    while date_sort.lower() not in answers:
        date_sort = str(input("\tОтсортировать операции по дате? Да/Нет\n\t"))

    date_sorting = answers[date_sort.lower()]

    if date_sorting:
        descending_sort = str(input("\tОтсортировать по возрастанию или по убыванию?\n\t")).lower()
        while descending_sort not in answers_descending:
            descending_sort = str(input("\tОтсортировать по возрастанию или по убыванию?\n\t"))
        result = processing.sort_by_date(list_of_dicts=result, reverse=answers_descending[descending_sort])

    # sorting by currency
    rub_sort = str(input("\tВыводить только рублевые транзакции? Да/Нет\n\t"))

    while rub_sort.lower() not in answers:
        rub_sort = str(input("\tВыводить только рублевые транзакции? Да/Нет\n\t"))

    rub_sorting = answers[rub_sort.lower()]

    if rub_sorting:
        result = list(generators.filter_by_currency(transactions=result, currency="RUB"))

    # sort by word in description
    word_sort = str(input("\tОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n\t"))

    while word_sort.lower() not in answers:
        word_sort = str(input("\tОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n\t"))

    word_sorting = answers[word_sort.lower()]

    if word_sorting:
        key_word = str(input("\tВведите слово для фильтрации:\n\t"))
        result = process_bank.process_bank_search(data=result, search=key_word)

    print(
        f"""
    Распечатываю итоговый список транзакций...
    Всего банковских операций в выборке: {len(result)}
    """
    )

    if len(result) == 0:
        print("\tНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    for transaction in result:
        if menu == 1:
            amount = transaction.get("operationAmount", {}).get("amount")
            currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        else:
            amount = transaction.get("amount")
            currency = transaction.get("currency_code")

        from_acc = transaction.get("from")
        to_acc = transaction.get("to")

        from_valid = isinstance(from_acc, str) and from_acc.strip()
        to_valid = isinstance(to_acc, str) and to_acc.strip()

        print(
            f"""
    {widget.get_date(transaction.get('date'))} {transaction.get('description')}
    {widget.mask_account_card(from_acc) + ' -> ' if from_valid else ''}{widget.mask_account_card(to_acc) if to_valid else ''}
    Сумма: {amount} {currency}
    """
        )
