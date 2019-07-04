import logging
import telegram
import requests
import subprocess
import urllib
import time
from telegram.error import NetworkError, Unauthorized
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from time import sleep

accessToken = 'Paste your Access-Token here'
chat_id = 'Paste your Chat-Id here'

def motionDetected():
    url = 'https://api.telegram.org/bot' + accessToken +  '/sendPhoto'
    files = { 'photo' : open('/mnt/dietpi_userdata/motioneye/Camera1/lastsnap.jpg', 'rb')}
    data = { 'chat_id ' : chat_id }
    r = requests.post(url, files=files, data=data)

def sendHTTPMessage(message):
    r = requests.post('https://api.telegram.org/bot' + accessToken + '/sendMessage?chat_id=' + chat_id + '&text=' + message)

def snap(bot, update):
    r = requests.get('http://localhost:7999/1/action/snapshot')
    re = requests.get('http://localhost:7999/1/action/snapshot')
    time.sleep(4)
    bot.sendPhoto(chat_id=chat_id, photo=open('/mnt/dietpi_userdata/motioneye/Camera1/lastsnap.jpg', 'rb'))

def trap(bot, update):
    bot.sendPhoto(chat_id=chat_id, photo=open('/mnt/dietpi_userdata/motioneye/Camera1/lastsnap.jpg', 'rb'))

def pause(bot, update):
    r = requests.get('http://localhost:7999/1/detection/pause')
    if r.status_code == 200:
        sendMessage(bot, update, 'Bewegungserkennung pausiert. /resume senden um wieder zu starten.')
    else:
        sendMessage(bot, update, 'Fehler bei der Deaktivierung der Bewegungserkennung.')

def resume(bot, update):
    r = requests.get('http://localhost:7999/1/detection/start')
    if r.status_code == 200:
        sendMessage(bot, update, 'Bewegungserkennung gestartet. /pause senden um zu pausieren.')
    else:
        sendMessage(bot, update, 'Fehler bei der Aktivierung der Bewegungserkennung.')

def status(bot, update):
    r = requests.get('http://localhost:7999/1/detection/start')
    sendMessage(bot, update, 'Status wird geladen... Bitte warten...')
    if r.status_code == 200:
        sendMessage(bot, update, 'Bewegungserkennung ist derzeit aktiv. Sende /pause um zu unterbrechen.')
    else:
        sendMessage(bot, update, 'Fehler bei der Statusabfrage.')
        

def sendMessage(bot, update, message):
    bot.sendMessage(chat_id = chat_id, text = message)

def main():
    updater = Updater(accessToken)
    disp = updater.dispatcher
    sendHTTPMessage('SvalgurSecurity wurde gestartet...')
    disp.add_handler(CommandHandler('snap', snap))
    disp.add_handler(CommandHandler('trap', trap))
    disp.add_handler(CommandHandler('pause', pause))
    disp.add_handler(CommandHandler('resume', resume))
    disp.add_handler(CommandHandler('status', status))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()