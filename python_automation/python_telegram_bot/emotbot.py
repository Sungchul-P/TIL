import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import emoji

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(bot, update):
    keyboard = [
        [InlineKeyboardButton("Happy", callback_data='1'),
         InlineKeyboardButton("Whatever", callback_data='2')],
        [InlineKeyboardButton("Sad", callback_data='3')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Hey there! How do you feel today?', reply_markup=reply_markup)

def button(bot, update):
    query = update.callback_query
    print(dir(query))
    print("chat_id : ", query.message.chat_id)
    print("message_id : ", query.message.message_id)
    if query.data == "1":
        em = emoji.emojize(':smile:', use_aliases=True)
        bot.editMessageText(text="Oh wow! %s " % em,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

    if query.data == "2":
        em = emoji.emojize(':expressionless:', use_aliases=True)
        bot.editMessageText(text="Does it matter? %s " % em,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

    if query.data == "3":
        em = emoji.emojize(':disappointed:', use_aliases=True)
        bot.editMessageText(text="Oh man! %s " % em,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")

def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))

# Updater를 생성하고 봇의 토큰을 전달한다.
updater = Updater('Token')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_error_handler(error)

# 봇을 시작한다.
updater.start_polling()

# 사용자가 Ctrl+C를 누르거나 프로세스가 SIGINT 혹은 SIGTERM, SIGABRT를 수신할 때까지 
# 봇을 실행한다.
updater.idle()