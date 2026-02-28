def filter_by_state(list_data: list, state='EXECUTED') -> list:
    """Сортирует список по критерию"""
    new_list = []
    for dictionary in list_data:
        if dictionary['state'] == state:
            new_list.append(dictionary)
    return new_list


def sort_by_date(list_data: list, metod=True) -> list:
    """Сортирует список по дате. По умолчанию сортирует по убыванию"""
    sorted_list = sorted(list_data, key=lambda dic: dic['date'], reverse=metod)
    return sorted_list
