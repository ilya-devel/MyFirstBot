import functions.ListCommands
import functions.TestingFunc
from functions.getToken import get_token
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler
import functions.start_choice
from telegram import KeyboardButton

TOKEN = get_token()


def run():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', functions.start_choice.start))
    app.add_handler(CallbackQueryHandler(functions.start_choice.user_choice))
    # app.add_handler(CommandHandler('test', functions.TestingFunc.testing))
    # app.add_handler(CommandHandler('help', functions.ListCommands.get_list_commands))
    app.run_polling()


if __name__ == '__main__':
    run()
