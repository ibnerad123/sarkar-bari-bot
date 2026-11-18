import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalamu Alaikum! Sarkar Bari Bot e welcome 🙏\n\n/start - Suru korte\n/help - Sahajjo pete")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tumi ja likhba ami tar reply dibo.\n\nSarkar Bari Bot - Iswarganj")

async def reply_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Tumi bolso: {text}\n\nAmi Sarkar Bari Bot, ekhon shikhtesi!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_all))
    print("Bot cholche...")
    app.run_polling()

if __name__ == "__main__":
    main()
