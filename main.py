import os
import telebot


bot = telebot.TeleBot("5623165505:AAEgJEFk0BQK82qwvqDXfxcs8ast57q5NCk")


@bot.message_handler(message=["ai"])
def send_message(message):
 bot.reply_to(message, " ඇයි පුකද බලන්නෙ")





bot.polling()
