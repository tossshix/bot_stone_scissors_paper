
from aiogram.types import Message
from aiogram.filters import CommandStart, Text, Command
from aiogram import Router
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboard import yes_no_kb, game_kb
from services.services import get_bot_choice, get_winner
from external_services.cats_api import cats_link
import requests

router: Router = Router()


@router.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)


@router.message(Command(commands=['help']))
async def process_command_help(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)


@router.message(Text(text=LEXICON_RU['no_button']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])


@router.message(Text(text=LEXICON_RU['yes_button']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)


@router.message(Text(text=[LEXICON_RU['paper'], LEXICON_RU['rock'], LEXICON_RU['scissors']]))
async def game_bot_choice(message: Message):
    bot_choice = get_bot_choice()

    await message.answer(text=f'{LEXICON_RU["bot_choice"]}'
                              f' - {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)
    if winner == 'user' and cats_link.status_code == 200:
        await message.answer(text=LEXICON_RU['cat'])
        await message.answer_photo(cats_link.json()[0]['url'])
