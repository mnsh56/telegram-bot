import telebot
import time

TOKEN = '7853238610:AAG1SOXqfetg36_rbtVmWw5ZQSTlSoDlNuc'
MY_ID = 288677626  # آیدی عددی خودت

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def forward_all(message):
    bot.forward_message(MY_ID, message.chat.id, message.message_id)

print("Bot is running...")

while True:
    try:
        bot.polling()
    except Exception as e:
        print("Error:", e)
        time.sleep(15)
