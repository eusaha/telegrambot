import os
import telebot


bot = telebot.TeleBot('5623165505:AAEgJEFk0BQK82qwvqDXfxcs8ast57q5NCk')


@bot.message_handler(commands=["a"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Uvindu Bro Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://youtube.com/c/Uvindubro")



bot.polling()
