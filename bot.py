import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔥 Hardcoded Token (for testing only – don’t use this in production!)
TOKEN = "7396112938:AAFznGgpmHVuYqLkFheeTYG3GW2Jwm3j0AM"

# Logging Setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Welcome to WealthGrowX! Refer and earn. Type /balance to see your earnings.")

# Balance Command
async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💰 Your current balance is €0.00")

# Run Bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("balance", balance))
    app.run_polling()