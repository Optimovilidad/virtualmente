import requests
import time
import vlc
import os
import subprocess

total_minutos = 0

def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def open_url_with_mplayer(url):
    try:
        mpv_path = r'C:\Program Files\VideoLAN\VLC\vlc.exe'
        
        #mpv_path 
        subprocess.run([mpv_path, url])
    except Exception as e:
        print(f"Error: {e}")


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
        #close_vlc()
        #break

def close_vlc():
    # Comando para cerrar VLC en sistemas Windows
    os.system("taskkill /f /im vlc.exe")


# def close_vlc():
#     # Comando para cerrar VLC en sistemas Linux
#     os.system("pkill vlc")
#     # Asegúrate de que el comando sea adecuado para tu sistema operativo

def reiniciar_raspberry():
    try:
        # Comando para reiniciar la Raspberry Pi
        subprocess.run(["sudo", "reboot"])
    except Exception as e:
        print(f"Error al reiniciar la Raspberry Pi: {e}")

while True:
    try:
        play_music()
    except:
        print("No hay conexión a Internet. Intentando nuevamente... en 10 segundos.")
        total_minutos = total_minutos +1
        print(total_minutos)
        if total_minutos == 2:
            print("se va a reiniciar la compu")
            reiniciar_raspberry()
        close_vlc()
    time.sleep(10)
