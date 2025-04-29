import telebot
import os
from flask import Flask
import threading

API_TOKEN = '7587491573:AAHa4tzovNpt1qCHn8JWmzbhDil2DqP02dw'
MY_ID = 288677626

bot = telebot.TeleBot(API_TOKEN)

# حذف Webhook قبلی
bot.remove_webhook()

# هندلر برای تمام پیام‌ها
@bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'audio', 'voice', 'sticker'])
def forward_all(message):
    try:
        bot.forward_message(MY_ID, message.chat.id, message.message_id)
    except Exception as e:
        print(f"Error forwarding message: {e}")

# اجرای ربات در پس‌زمینه
threading.Thread(target=bot.polling, daemon=True).start()

# اجرای Flask برای Render
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
