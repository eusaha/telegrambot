import os
import telebot


bot = telebot.TeleBot(' 5623165505:AAEgJEFk0BQK82qwvqDXfxcs8ast57q5NCk ')


@bot.message_handler(commands=["hi"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Chat Bot")
  
  


bot.polling()
