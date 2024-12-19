from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters.command import Command
API_TOKEN='8190952322:AAERAD2E1hMKY4P8lTJ0BSZuGaoYviyONZM'
bot=Bot(token=API_TOKEN)
dp=Dispatcher()
@dp.message(Command("start"))
async def send_welcome(message:types.message): await message.reply("Привет, пришли мн елюбое сообщение и я тебе отвечу")
@dp.message()
async def echo(message: types.Message):await message.answer(message.text)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
