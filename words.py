import random
from pathlib import Path

word_list=Path('words.txt').read_text()

word_list=word_list.split(" ")

def load_words():
    return word_list


def choose_word():
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()
    return secret_word

choose_word()