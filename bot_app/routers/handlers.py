from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
import re


router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(
        text=f"Hello, {markdown.hbold(message.from_user.full_name)}!",
        parse_mode=ParseMode.HTML,
    )


@router.message(Command("Nufore_bot", prefix="@"))
async def test_handle(message: types.Message,):

    pattern = r"^[0-9]+[h, d, w, m]$"
    period = message.text.split(' ')[-1]
    print(message.chat.id)

    if re.fullmatch(pattern, period):
        message_from_user = ' '.join(message.text.split(' ')[1:-1])
        text = f"Задача \"{message_from_user}\" принята. Напомню о ней через {period}."
        await message.answer(text)
