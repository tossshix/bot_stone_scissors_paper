
from aiogram.types import Message
from aiogram import Router
from lexicon.lexicon_ru import LEXICON_RU

router: Router = Router()


@router.message()
async def other_message(message: Message):
    await message.answer(text=LEXICON_RU['other'])
