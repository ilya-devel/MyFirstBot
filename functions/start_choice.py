from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton('Function 1', callback_data='function 1'),
        InlineKeyboardButton('Function 2', callback_data='function 2'),
        InlineKeyboardButton('Function 3', callback_data='function 3')
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('What do you want to do?:', reply_markup=reply_markup)


async def user_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    # await query.answer()
    await query.edit_message_text(text=f'Selected: {query.data}')
