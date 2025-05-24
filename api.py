from flask import Flask, request
from pyrogram import Client, filters
import random
import os

app = Flask(__name__)

BOT_TOKEN = "7480497994:AAF-uFwQTwfFHEKvFxDoEyqFr21XvIXGUsw"
API_ID = 26365804  # Replace with your real API ID
API_HASH = "311437f18ff014a3689409c9eeb44d42"  # Replace with your real API Hash
FORCE_CHANNEL = "@SohilScripter"

bot = Client("bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@app.route("/", methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if update:
        bot.process_update(update)
    return "OK", 200

@bot.on_message(filters.command("start"))
def start(client, message):
    user_id = message.from_user.id
    prediction = random.choice(["Big", "Small", "Odd", "Even"])
    client.send_message(chat_id=user_id, text=f"🔮 Welcome!\nPrediction: `{prediction}`", parse_mode="markdown")

# Start bot in webhook mode
if __name__ == "__main__":
    bot.run()
