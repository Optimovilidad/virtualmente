import requests
import time
import vlc
import os
import subprocess

def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def play_music():
    # Ruta al archivo de música que deseas reproducir
    music_file_path = "http://186.4.224.169:8080/livestream/stream.m3u8"

    # Configuración de VLC
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(music_file_path)
    media.get_mrl()
    player.set_media(media)

    # Reproducir la música
    while check_internet_connection() == True:
        player.play()
    while check_internet_connection() == False:
        media.close()

def close_vlc():
    # Comando para cerrar VLC en sistemas Windows
    os.system("taskkill /f /im vlc.exe")


# def close_vlc():
#     # Comando para cerrar VLC en sistemas Linux
#     os.system("pkill vlc")
#     # Asegúrate de que el comando sea adecuado para tu sistema operativo


while True:
    try:
        play_music()
    except:
        print("No hay conexión a Internet. Intentando nuevamente... en 10 segundos.")
        close_vlc()
    time.sleep(10)
