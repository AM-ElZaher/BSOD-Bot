from os import read
import requests
from telegram.ext import *
import csv
import sys




API_Key = '1870058185:AAF1_qrjgny04vXb4bpV01X12unkdl85n40'

print("Bot Started..!")

# searchCode = input()
# with open("C:\\Users\\BarayeZ\\Desktop\\New folder\\erCodes.csv") as f_obj:
#     reader = csv.reader(f_obj, delimiter=',')
#     for line in reader:
#         if (searchCode) in line:
#             print(line)



def respond(input_text):
    user_message = str(input_text).lower()
    with open("C:\\Users\\BarayeZ\\Desktop\\New folder\\erCodes.csv") as f_obj:
        reader = csv.reader(f_obj, delimiter=',')
        for line in reader:
            if user_message in line:
                return(line)
            else:
                return "try Again"
  



def start_command(update, context):
    update.message.reply_text('Start by typing BSOD error codes here..')




def help_command(update, context):
    update.message.reply_text('a Read me guide to help users')




def handle_message(update, context):
    text = str(update.message.text).lower()
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
