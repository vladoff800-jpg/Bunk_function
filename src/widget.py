from src import masks


def mask_account_card(number: str) -> str:
    """Маскирует информацию карты или счета"""
    if number[:4] == "Счет":
        musk_number = "Счет " + masks.get_mask_account(number)
    else:
        musk_number = masks.get_mask_card_number(number)
    return musk_number


def get_date(date: str) -> str:
    """Форматирует время ДД.ММ.ГГГГ"""
    form_date = date[8:10] + "." + date[5:7] + "." + date[:4]
    return form_date
