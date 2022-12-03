from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes


def gen_keyboard():
    keyboard = [[
        InlineKeyboardButton('Да', callback_data='True'),
        InlineKeyboardButton('Нет', callback_data='False')
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('What do you want to do?:', reply_markup=gen_keyboard())


async def user_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.edit_message_text(text=f'Selected: {query.data}')