
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.lexicon_ru import LEXICON_RU

button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_yes],
                                                               [button_no]], resize_keyboard=True)

scissors_but = KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
paper_but = KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])
rock_but = KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])

game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[scissors_but],
                                                             [paper_but],
                                                             [rock_but]], resize_keyboard=True)
