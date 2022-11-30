import functions.ListCommands
import functions.TestingFunc
from functions.getToken import get_token
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = get_token()


def app():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('test', functions.TestingFunc.testing))
    app.add_handler(CommandHandler('help', functions.ListCommands.get_list_commands))
    app.run_polling()


if __name__ == '__main__':
    app()
