import os
import telebot


bot = telebot.TeleBot(' 5661907712:AAGbmC647RqtdIpe8UgkqMZS8ohTnXQLBqU ')


@bot.message_handler(commands=["a"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Uvindu Bro Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://youtube.com/c/Uvindubro")



bot.polling()
