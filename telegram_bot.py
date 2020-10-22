!pip install adafruit-io
from Adafruit_IO import Client,Data
import os

ADAFRUIT_IO_USERNAME = os.getenv('bablu123')
ADAFRUIT_IO_KEY = os.getenv('aio_LIoe75brhaH1MxvahTnom0ml2rFS')
TOKEN = os.getenv('1191168607:AAFHhNc0jc1l2sGtIYtX')
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
!pip install python-telegram-bot
  
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import os
def turnoff(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Light turned off")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://www.123rf.com/photo_12676342_filament-lamp-on-a-white-background-illustration-for-design.html')
  send_value(0)
def turnon(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Light turned on")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://www.123rf.com/photo_48123160_stock-vector-bright-glowing-incandescent-light-bulb-on-a-white-background.html')
  send_value(1)

def send_value(value):
  feed = aio.feeds('bot')
  aio.send_data(feed.key,value)

def input_message(update, context):
  text=update.message.text
  if text == 'turn on':
    send_value(1)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Light turned on")
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://www.123rf.com/photo_48123160_stock-vector-bright-glowing-incandescent-light-bulb-on-a-white-background.html')
  elif text == 'turn off':
    send_value(0)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Light turned off")
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://www.123rf.com/photo_12676342_filament-lamp-on-a-white-background-illustration-for-design.html')

    
def start(update,context):
  start_message='''
/turnoff :To turn OFF the Light
/turnon :To turn ON the Light
'''
  context.bot.send_message(chat_id=update.effective_chat.id, text=start_message)


updater =Updater('1191168607:AAFHhNc0jc1l2sGtIYtX')
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('turnoff',turnoff))
dispatcher.add_handler(CommandHandler('turnon',turnon))
dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command),input_message))
updater.start_polling
updater.idle()
