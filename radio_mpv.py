import threading
import requests as r
import subprocess
from api_radio import API
from time import sleep

url_to_open = "http://186.4.158.16:8080/livestream/stream.m3u8"

def open_url_with_mplayer(url):
    try:
        #mpv_path = r'C:\mpv\mpv.exe'
        #subprocess.run([mpv_path, url])
        mpv_path = ["mpv", url]
        subprocess.Popen(mpv_path)
    except Exception as e:
        print(f"Error: {e}")

class Radio():
    def __init__(self, use_socket=False):
	
        self.use_socket = use_socket
        self.is_playing = False
        self.mensaje = ""
        self.api = API("prod")  
        print("OK")
        self.player = ""
        t = threading.Thread(target=self.probar_internet)
        t.start()

    def check_internet(self, host='http://google.com'):
        try:
            r.get(host)
            return True
        except Exception:
            return False

    def probar_internet(self):
        while True:
            self.mensaje = ";"
            if self.check_internet():
                self.mensaje += ";"
                if self.is_playing:
                    self.mensaje += ""
                else:
                    if self.player is not None:
                        self.player=open_url_with_mplayer(url_to_open)
                        self.is_playing = True
                        #self.mensaje += ";"+"reproducciendo"
                    #reconectar en caso de perder conectividad
                    else:
                        self.player=open_url_with_mplayer(url_to_open)
                        self.is_playing = True           
                        self.mensaje += ";"+"reproducciendo"
            else:
                self.mensaje += ";"
                try:
                    self.is_playing = False
                    self.player.stop()
                except Exception:
                    pass
                self.mensaje += ""
            sleep(5)


Radio(True)
