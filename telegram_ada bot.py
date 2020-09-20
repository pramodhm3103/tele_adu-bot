from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from Adafruit_IO import Client, Data
import requests
import os
x = os.getenv('x')
y = os.getenv('y')
z = os.getenv('z')
aio = Client(x,y)


def on(bot,update):
    chat_id=update.message.chat_id
    bot.send_photo(chat_id,photo='https://img.icons8.com/plasticine/2x/light-on.png')
    bot.send_message(chat_id,text='led is on')
    aio = Client(x,y)
    value=Data(value=1)
    value_send=aio.create_data('bot',value)


def off(bot,update):
    chat_id=update.message.chat_id
    bot.send_photo(chat_id,photo='https://pngimg.com/uploads/bulb/bulb_PNG1241.png')
    bot.send_message(chat_id,text='led is off')
    aio = Client(x,y)
    value=Data(value=0)
    value_send=aio.create_data('bot',value)

def inmes(bot,update):
    mess_text = update.message.text
    if mess_text == 'turn on':
      on(bot,update)
    elif mess_text == 'turn off':
      off(bot,update)

u=Updater(z)
dp=u.dispatcher
dp.add_handler(CommandHandler('turnon',on))
dp.add_handler(CommandHandler('turnoff',off))
dp.add_handler(MessageHandler(Filters.text&(~Filters.command),inmes))
u.start_polling()
u.idle()
