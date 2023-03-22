import asyncio
from loguru import logger
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from telegram_notifications.config import *


logger.add('debug.log', level='INFO', format='{time} {level} {message}', rotation='15MB', compression='zip')

bot = Bot(token=TOKEN)

dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    logger.info(message.from_user.id)
    logger.info(type(message.chat.id))
    await message.answer('Привет. Я буду присылать уведомления о выполнении твоих программ')


async def send_notification(message, user_id=USER_ID):
    await bot.send_message(user_id, message)
    await bot.session.close()


async def main():
    await dp.start_polling(bot)


def notification(message):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_notification(message))


if __name__ == '__main__':
    asyncio.run(main())
