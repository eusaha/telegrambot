import os
import telebot


bot = telebot.TeleBot("API එක දාහන් උස්සන්නෙ නැතුව මගෙ ඒව")


@bot.message_handler(commands=["ADO"])
def send_welcome(message):
  bot.reply_to(message, "AI YAKO")






bot.polling()
