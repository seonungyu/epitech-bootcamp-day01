import random
from english_words import english_words_lower_alpha_set


def random_word():
    return random.choice(list(english_words_lower_alpha_set)).upper()


def show_word(secret, revealed):
    display = ""
    for letter in secret:
        if letter in revealed:
            display += letter + " "
        else:
            display += "_ "
    return display


def penalty_text(penalties):
    if penalties <= 1:
        return str(penalties) + " penalty"
    return str(penalties) + " penalties"


def is_lost(penalties):
    return penalties > 12