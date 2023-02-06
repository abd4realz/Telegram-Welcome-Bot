import logging
import os
import telegram
from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Load the environment variables from the .env file
load_dotenv()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define the welcome function to welcome new users
def welcome(update: telegram.Update, context: CallbackContext):
    new_user = update.message.new_chat_members[0]
    message = "Welcome to the group, {}!".format(new_user.first_name)
    context.bot.send_message(chat_id=update.message.chat_id, text=message)

# Define the main function to run the bot
def main():
    # Get the bot token from the .env file
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    # Create the Updater and pass it the bot's token
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add the welcome handler to the dispatcher
    welcome_handler = MessageHandler(Filters.status_update.new_chat_members, welcome)
    dp.add_handler(welcome_handler)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
