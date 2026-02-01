from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import os

BOT_TOKEN = os.getenv("8490429007:AAEI08HnfXrgbnWUKA8VruiIOohfk8aZm6g")
print("8490429007:AAEI08HnfXrgbnWUKA8VruiIOohfk8aZm6g", BOT_TOKEN)
# movie_code : file_id
MOVIES = {}

# (user_id, movie_code)
USED = set()

ADMIN_ID = 7450191608  # <-- এখানে তোমার Telegram user ID বসাও

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    args = context.args

    if not args:
        await update.message.reply_text("Website theke asho.")
        return

    movie_code = args[0]

    if movie_code not in MOVIES:
        await update.message.reply_text("Movie not found or expired.")
        return

    if (user_id, movie_code) in USED:
        await update.message.reply_text("You already got this movie.")
        return

    await context.bot.send_document(
        chat_id=update.effective_chat.id,
        document=MOVIES[movie_code],
        caption="Enjoy 🍿"
    )

    USED.add((user_id, movie_code))

async def admin_upload(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    if not update.message.document:
        await update.message.reply_text("Send movie file.")
        return

    file_id = update.message.document.file_id
    file_name = update.message.document.file_name

    movie_code = file_name.split(".")[0].lower().replace(" ", "_")

    MOVIES[movie_code] = file_id

    await update.message.reply_text(
        f"Movie added ✅\n\nCode:\n{movie_code}"
    )

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL, admin_upload))

    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
