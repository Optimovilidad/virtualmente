import re
import vlc
import pytz
import uuid
import socket
import threading
import requests as r
from api_radio import API
from time import sleep
from datetime import datetime


class Radio():
    def __init__(self, use_socket=False):
        self.use_socket = use_socket
        self.is_playing = False
        self.stream_url = self.__get_link()
        self.mensaje = self.get_host()+";"+self.get_fecha()
        self.api = API("prod")
        if self.stream_url is not None:
            self.player = vlc.MediaPlayer(self.stream_url)
        else:
            self.player = None
        t = threading.Thread(target=self.probar_internet)
        tstatus = threading.Thread(target=self.send_status)
        t.start()
        tstatus.start()

    def get_host(self):
        hostname = socket.gethostname()
        return self.get_mac_address()+";"+hostname

    def send_status(self):
        while True:
            if self.use_socket:
                self.api.send_data(self.mensaje)
                # print(self.mensaje)
            sleep(10)

    def get_fecha(self):
        timezone = pytz.timezone('America/Guayaquil')
        now = datetime.now(timezone)
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def check_internet(self, host='http://google.com'):
        try:
            r.get(host)
            return True
        except Exception:
            return False

    def __get_link(self):
        try:
            url = r.get('https://virtual-mente.net/radio/').text
            if self.check_url(url):
                return url
            #return "rtmp://186.4.158.16/livestream/stream"
            return "http://186.4.224.169:8080/livestream/stream.m3u8"
        except Exception as e:
            print(e)
            return None

    def check_url(self, url):
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            # domain...
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None

    def get_mac_address(self):
        mac_address = uuid.getnode()
        return str(mac_address)

        '''mac_address_hex = ':'.join(['{:02x}'.format(
            (mac_address >> elements) & 0xff) for elements in range(0, 8*6, 8)][::-1])
        print(mac_address_hex)'''

    def probar_internet(self):
        while True:
            self.mensaje = self.get_host()+";"+self.get_fecha()
            if self.check_internet():
                self.mensaje += ";"+"conectado"
                if self.is_playing:
                    self.mensaje += ";"+"reproducciendo"
                else:
                    if self.player is not None:
                        self.player.play()
                        self.is_playing = True
                        self.mensaje += ";"+"reproducciendo"
                    else:
                        self.stream_url = self.__get_link()
                        if self.stream_url is not None:
                            self.player = vlc.MediaPlayer(self.stream_url)
                            self.player.play()
                            self.is_playing = True
                            self.mensaje += ";"+"reproducciendo"
            else:
                self.mensaje += ";"+"desconectado"
                try:
                    self.is_playing = False
                    self.player.stop()
                except Exception:
                    pass
                self.mensaje += ";"+"detenido"
            # print(self.mensaje)
            sleep(10)


Radio(True)

