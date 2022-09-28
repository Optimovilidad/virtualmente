import time
import vlc
import requests as r
import os
import urllib.request as rq

stream_url = ''
def check_internet(host='http://google.com'):
    try:
        r.get(host)
        return True
    except:
        return False


def get_link():
    link = r.get('https://virtual-mente.net/radio/').text
    return link


if check_internet():
    stream_url = get_link()
    print("Starting")
    p = vlc.MediaPlayer(stream_url)
    p.play()
    print("Playing")
    #p.stop()
    #quit()
else:
    print('sin internet')

while check_internet():
    pass

time.sleep(10)
print('Fin del programa')

os.system('python3 /home/orange/Desktop/radio/restartRadio.py')