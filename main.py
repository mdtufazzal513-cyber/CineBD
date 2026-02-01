from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.document:
        file_id = update.message.document.file_id
        await update.message.reply_text(f"FILE_ID:\n{file_id}")
    else:
        await update.message.reply_text("Please send a file.")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, get_file_id))
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
