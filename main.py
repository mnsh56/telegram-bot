import telebot
import os
from flask import Flask
import threading

API_TOKEN = '7853238610:AAG1SOXqfetg36_rbtVmWw5ZQSTlSoDlNuc'
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
def start_bot():
    bot.infinity_polling()

threading.Thread(target=start_bot, daemon=True).start()

# اجرای Flask برای Render
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

if name == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
