import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ["BOT_TOKEN"]
GAME_URL = "https://dadu-online-dun.vercel.app/"
BUBBLE_URL = "https://bubble-hero-run-by-xobe-development.vercel.app/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Mainkan Dadu 🎲", url=GAME_URL)],
        [InlineKeyboardButton("Mainkan Bubble 🟢", url=BUBBLE_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.message:
        await update.message.reply_text(
            "Pilih game yang ingin kamu mainkan:",
            reply_markup=reply_markup
        )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
