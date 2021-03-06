import yaml
import logging

from telegram import Update, ForceReply, update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, callbackcontext, dispatcher, handler  

CONFIG = yaml.safe_load(open("config/config.yml"))

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# Define a few command handlers. These usually take the two arguments update and 
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued"""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True)
    )

def test(update: Update, context: CallbackContext) -> None:
    update.message.reply_markdown_v2(
        'test'        
    )


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)    

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass the bot's token
    updater = Updater(CONFIG['BOT_TOKEN'])

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    
    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    test()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()



if __name__ == '__main__':
    main()