def get_mask_card_number(card_number: str) -> str:
    """ Маскирует номер карты в формате XXXX XX** **** XXXX."""
    mask_card_number = card_number[:-12] + " " + card_number[-12:-10] + "** **** " + card_number[-4:]
    return mask_card_number


def get_mask_account(account: str) -> str:
    """Маскирует номер счета в формате **ХХХХ"""

    mask_account = "**" + account[-4:]
    return mask_account
