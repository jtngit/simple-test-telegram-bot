from messages import MessagesAndName
#from telegram.ext import *
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

API_KEY = '5120629068:AAHxvdDG0tCgqCsiZYrL54dOTTj3ERoYUNw'
updater = Updater(API_KEY,use_context=True)


def start(update: Update, context: CallbackContext):
	
        print(update)
        name = update.message.chat.first_name
        update.message.reply_text(
        f"hi {name} Welcome to the Bot.Please write ' /help ' to see the commands available.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/creator - To get the name of creator
	/github - To get github url""")


def creator(update: Update, context: CallbackContext):
	update.message.reply_text("the bot created by jtngit !!!")

def github(update: Update, context: CallbackContext):
	update.message.reply_text("https://github.com/")




def handle_message(update, context):
    text = str(update.message.text).lower()
    id = update.message.chat.id
    name = update.message.chat.first_name
    print(f"id of person = {id}")
    print(text)
    id = MessagesAndName(name,text)

    
    
    update.message.reply_text(id.calling())
    update.message.reply_text(id.cal())
    #print(update)


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)


def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
     
    dp = updater.dispatcher

    ### handle commands #############
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('creator', creator))
    dp.add_handler(CommandHandler('github', github))
    dp.add_handler(CommandHandler('help', help))
    
    ####### handle errors of command and message ############
    #dp.add_handler(MessageHandler(Filters.text, unknown))
    dp.add_handler(MessageHandler(Filters.command, unknown)) # Filters out unknown commands
    dp.add_error_handler(error)

    ############# handle messages ###################
    dp.add_handler(MessageHandler(Filters.text, handle_message))


    updater.start_polling()
    updater.idle()

main()