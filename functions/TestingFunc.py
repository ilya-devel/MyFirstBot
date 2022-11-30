from telegram.ext import ContextTypes
from telegram import Update


async def testing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tmp = update.message.text.split(maxsplit=1)
    if len(tmp)>1:
        tmp = update.message.text.split(maxsplit=1)[1]
        a, b = map(int, tmp.split('+'))
        await update.message.reply_text(f'{a} + {b} = {a + b}')
    else:
        await update.message.reply_text('Вам нужно указать текст после комманды!')