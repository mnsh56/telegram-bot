import telebot
import os
from flask import Flask

API_TOKEN = '7853238610:AAG1SOXqfetg36_rbtVmWw5ZQSTlSoDlNuc'
MY_ID = 288677626

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def forward_to_me(message):
    try:
        bot.forward_message(MY_ID, message.chat.id, message.message_id)
    except Exception as e:
        print(f"Error forwarding message: {e}")

# شروع Polling در یک Thread جداگانه
import threading
threading.Thread(target=bot.polling, daemon=True).start()

# Flask برای باز کردن پورت (فقط برای خوشحال کردن Render!)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
