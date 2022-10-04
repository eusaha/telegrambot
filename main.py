import os
import telebot


bot = telebot.TeleBot("5623165505:AAEgJEFk0BQK82qwvqDXfxcs8ast57q5NCk")


##@bot.message_handler(commands=["ai"])
##def send_welcome(message):
 ## bot.reply_to(message, " ඇයි පුකද බලන්නෙ")

  def hi(update ,context):
update.message.reply_text("ai ")




bot.polling()
