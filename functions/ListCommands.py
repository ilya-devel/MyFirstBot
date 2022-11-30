from telegram import Update
from telegram.ext import ContextTypes


async def get_list_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu = """
    /test - тестовая проверка работы бота

    """
    await update.message.reply_text(menu)