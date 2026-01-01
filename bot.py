import os
import csv
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from utils import get_best_products_csv

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHANNEL_ID")
CSV_FILE = "products.csv"  # файл CSV с товарами

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

def send_products():
    products = get_best_products_csv(CSV_FILE, count=5)
    for p in products:
        msg = f"📦 {p['title']}\n💰 {p['price']}\n⭐ {p['rating']} ⭐\n"
        buttons = types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("🛒 Купить", url=p["link"])
        )
        bot.send_photo(CHAT_ID, photo=p["image"], caption=msg, reply_markup=buttons)

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.reply("Бот активирован!")

if __name__ == "__main__":
    send_products()
    executor.start_polling(dp, skip_updates=True)
