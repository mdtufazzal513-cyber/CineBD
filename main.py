import os

BOT_TOKEN = os.getenv("8490429007:AAEI08HnfXrgbnWUKA8VruiIOohfk8aZm6g")
print("Bot token from env:", BOT_TOKEN)

if not BOT_TOKEN:
    print("Error: BOT_TOKEN not found in environment variables!")
    exit(1)
