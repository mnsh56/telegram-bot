import telebot
import os
from flask import Flask
import threading

API_TOKEN = '7853238610:AAG1SOXqfetg36_rbtVmWw5ZQSTlSoDlNuc'
MY_ID = 288677626

bot = telebot.TeleBot(API_TOKEN)

# قبل از شروع polling، Webhook قبلی رو حذف کن
bot.remove_webhook()

# هندلر برای تمام پیام‌ها (متن، عکس، ویدیو، ویس و...)
@bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'audio', 'voice', 'sticker'])
def forward_all(message):
    try:
        bot.forward_message(MY_ID, message.chat.id, message.message_id)
    except Exception as e:
        print(f"Error forwarding message: {e}")

# اجرای ربات در پس‌زمینه
threading.Thread(target=bot.polling, daemon=True).start()

# اجرای Flask برای Render
app = Flask(_name_)

@app.route('/')
def home():
    return "Bot is running!"

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
