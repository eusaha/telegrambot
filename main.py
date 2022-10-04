import os
import telebot


bot = telebot.TeleBot(' 5623165505:AAEgJEFk0BQK82qwvqDXfxcs8ast57q5NCk ')


@bot.message_handler(commands=["hi"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Chat Bot")
  
  
@bot.message_handler(commands=["hello"])
def send_welcome(message):
  bot.reply_to(message, "ඇයි")
  
  
@bot.message_handler(commands=["ai"])
def send_welcome(message):
  bot.reply_to(message, " අයි පුකද බලන්නෙ ")

bot.polling()
