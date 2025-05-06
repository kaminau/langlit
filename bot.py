from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
import asyncio

# Ваш токен от BotFather
API_TOKEN = "7514174562:AAHSi6gUn4vng2yyHm3aa6xzrQa_BQ36lh8"

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Создание клавиатуры
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Beginner"), KeyboardButton(text="Intermediate")],
        [KeyboardButton(text="Advanced")]
    ],
    resize_keyboard=True
)

# Обработчик команды /start
@dp.message(F.text == "/start")
async def send_welcome(message: Message):
    await message.answer(
        "Привет! Я помогу подобрать современные книги для изучения иностранных языков. Выберите ваш уровень:",

        reply_markup=keyboard
    )

# Обработчик нажатий на кнопки
@dp.message(F.text.in_({"Beginner", "Intermediate", "Advanced"}))
async def recommend_books(message: Message):
    level = message.text
    if level == "Beginner":
        books = "1. Five Feet Apart by Rachael Lippincott\n2. One day in December by Josie Silver"
    elif level == "Intermediate":
        books = "1. Normal people by Sally Rooney\n2. The Bullet That Missed by Richard Osman\n3. Shadow and Bone by Leigh Bardugo\n4. The Cruel Prince by Holly Black"
    else:  # Advanced
        books = "1. Yellowface by Rebecca Kuang\n2. Six of Crows by Leigh Bardugo\n3. Crescent City:House of Earth and Blood by Sarah Maas"
    await message.answer(f"Для {level}:\n{books}")

# Главная функция для запуска бота
async def main():
    # Регистрация обработчиков
    dp.message.register(send_welcome, F.text == "/start")
    dp.message.register(recommend_books, F.text.in_({"Beginner", "Intermediate", "Advanced"}))

    # Удаление старого webhook и запуск polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
