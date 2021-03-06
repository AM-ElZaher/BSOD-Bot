from os import read
import requests
#python-telegram-bot
from telegram.ext import *
import csv
import sys
import pandas as pd


API_Key = '1870058185:AAF1_qrjgny04vXb4bpV01X12unkdl85n40'
print("Bot Started..!")



def respond(input_text):
    user_message = str(input_text).lower()
    if "hi" in user_message:
        return"hello"
    elif "how are you" in user_message:
        return"fine, you?"
    elif "how does it work" in user_message:
        return "type /help to get some info"
    else:
        try:
            df = pd.read_csv("C:\\Users\\ahmed.elzaher\\OneDrive - Palm Hills Developments\\Documents\\PythonTest\\errCode.csv", sep=",")
            searchResult = (list(df.loc[df['STOP Code'].str.lower() == user_message, 'Cause of the Blue Screen'])[0])
            return (searchResult)
        except:
            return("No data found, check spelling or enter the exact error code")

    
  


def start_command(update, context):
    update.message.reply_text('Start by typing BSOD error codes here..')

def help_command(update, context):
    update.message.reply_text('a Read me guide to help users')


def handle_message(update, context):
    text = str(update.message.text)
    res = respond(text)
    update.message.reply_text(res)




def main():
    updater = Updater(API_Key, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling()
    updater.idle()

main()
