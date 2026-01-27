def filter_by_state(list_of_dicts: list[dict], state: str = "EXECUTED") -> list[dict]:
    """The function filters a list of dictionaries according to the given state"""

    if list_of_dicts == [] or list_of_dicts is None:
        raise ValueError('The list of dictionaries is empty')
    for i in list_of_dicts:
        if i['state'] == '' or i['state'] is None:
            raise ValueError('The state is empty')

    return [item for item in list_of_dicts if item.get("state") == state]


def sort_by_date(list_of_dicts: list[dict], reverse: bool = True) -> list[dict]:
    """The function sorts a list of dictionaries by date"""

    if list_of_dicts == [] or list_of_dicts is None:
        raise ValueError('The list of dictionaries is empty')
    for i in list_of_dicts:
        if i['date'] is None or i['date'] == '':
            raise ValueError('The date is invalid')

    return sorted(list_of_dicts, key=lambda item: item.get("date"), reverse=reverse)