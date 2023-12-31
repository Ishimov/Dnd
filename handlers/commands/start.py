from aiogram.types import Message

from loader import dp
from handlers.commands.help import cmd_help

@dp.message_handler(commands=['start'])
async def cmd_start(message: Message) -> None:
    await message.answer(text=f'Добро пожаловать, {message.from_user.full_name}!')
    await cmd_help(message)