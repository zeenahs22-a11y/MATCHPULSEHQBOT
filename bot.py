import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Get token from Railway environment variable
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when /start is issued."""
    await update.message.reply_text(
        "Welcome to MatchPulseHQ! ⚽\n"
        "I am under construction. Soon I will bring you live scores and stats."
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Echo the user message (placeholder for real commands)."""
    await update.message.reply_text(f"You said: {update.message.text}")

def main():
    if not TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN is missing!")
        return
    
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    logger.info("Bot is starting...")
    application.run_polling()

if __name__ == "__main__":
    main()
