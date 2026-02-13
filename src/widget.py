def mask_account_card(number: str) -> str:
    """Маскирует информацию карты или счета"""
    if number[:4] == "Счет":
        musk_number = "Счет " + "**" + number[-4:]
    else:
        musk_number = number[:-12] + " " + number[-12:-10] + "** **** " + number[-4:]
    return musk_number
