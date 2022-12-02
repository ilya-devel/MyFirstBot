from telegram.ext import ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update


async def testing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Option 1", callback_data="1"), InlineKeyboardButton("Option 2", callback_data="2"), ],
        [InlineKeyboardButton("Option 3", callback_data="3")], ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose:", reply_markup=reply_markup)
    # if len(tmp)>1:
    #     tmp = update.message.text.split(maxsplit=1)[1]
    #     a, b = map(int, tmp.split('+'))
    #     await update.message.reply_text(f'{a} + {b} = {a + b}')
    # else:
    #     await update.message.reply_text('Вам нужно указать текст после комманды!')
