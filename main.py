import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("Assalamu Alaikum! Sarkar Bari Bot e welcome 🙏")

async def help_cmd(update, context):
    await update.message.reply_text("Tumi ja likhba ami tar reply dibo.")

async def reply_all(update, context):
    await update.message.reply_text(f"Tumi bolso: {update.message.text}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_all))
    print("Bot cholche...")
    app.run_polling()

if __name__ == "__main__":
    main()
