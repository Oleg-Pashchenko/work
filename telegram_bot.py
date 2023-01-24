import os
import asyncio

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

API_TOKEN = '5398420004:AAF1PxwUSTnPPYZCC2hnVpOovMM2YcOTdEc'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Set of subscribed chat_id
subscribed_chat_id = set()


@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    await message.reply("Welcome! Use /subscribe to get notifications")


@dp.message_handler(commands=['subscribe'])
async def subscribe(message: Message):
    chat_id = message.chat.id
    subscribed_chat_id.add(chat_id)
    await message.reply("You have successfully subscribed for notifications!")


@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: Message):
    chat_id = message.chat.id
    subscribed_chat_id.remove(chat_id)
    await message.reply("You have successfully unsubscribed for notifications!")


def send_document_to_telegram():
    file = open("Result.xlsx", "rb")
    for subscriber_id in subscribed_chat_id:
        bot.send_document(subscriber_id, file)


def bot():
    executor.start_polling(dp, skip_updates=True)
