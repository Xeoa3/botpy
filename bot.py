import logging
import config
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename='bot.log'
                    )

def start_bot(updater : Updater, cnt : CallbackContext):
    print(updater)
    text = "Hi {} , I'm a telegram bot. Type /help to see my commands.".format(updater.message.chat.first_name)
    updater.message.reply_text(text)

def chat(updater : Updater, cnt : CallbackContext):
    text = updater.message.text
    logging.info(text)
    updater.message.reply_text(text)

def main() :
    upd = Updater(config.TOKEN_NAME)
    upd.dispatcher.add_handler(CommandHandler('start', start_bot))
    upd.dispatcher.add_handler(MessageHandler(Filters.text, chat))
    upd.start_polling()
    upd.idle()
if __name__ == '__main__':
    logging.info('Starting bot...')
    main()