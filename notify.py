import logging
import requests
import time

accessToken = 'Paste your Access-Token here'
chat_id = 'Paste your Group-Token here'

def main():
    time.sleep(7)
    message = '\xF0\x9F\x9A\xA8 Es wurde eine Bewegung erkannt! Sende /trap um das letzte Foto zu sehen. Nutze /snap um ein aktuelles zu schiessen.'
    r = requests.post('https://api.telegram.org/bot' + accessToken + '/sendMessage?chat_id=' + chat_id + '&text=' + message)

if __name__ == '__main__':
    main()