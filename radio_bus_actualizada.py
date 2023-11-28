import requests
import time
import vlc
import subprocess

def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=10)
        return response.status_code == 200
    # except requests.ConnectionError:
    #     return False
    except requests.exceptions.ReadTimeout:
        print("Tiempo de espera de lectura agotado. Reintentando la solicitud...")
    # Puedes volver a intentar la solicitud o tomar otras acciones aquí
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")

def reproducir_video(enlace):
    # Configuración de VLC
    instance = vlc.Instance("--no-xlib")
    player = instance.media_player_new()
    media = instance.media_new(enlace)
    media.get_mrl()
    player.set_media(media)

    # Reproducir el video
    player.play()

    # Esperar hasta que termine el video o se pierda la conexión
    #while not check_internet_connection():
    try:
        while player.get_state() != vlc.State.Ended:
            if not check_internet_connection():
                # player.stop()
                # player.release()
                print("Se perdió la conexión a Internet. Esperando 10 segundos...")
                time.sleep(10)
                tiempo_espera = 0
                while not check_internet_connection():
                    print("Esperando a que la conexión a Internet se restablezca...")
                    time.sleep(10)
                    tiempo_espera += 10
                    # player.release()
                    if tiempo_espera >= 120:  # Esperar 2 minutos (120 segundos)
                        print("No se puede establecer conexión a Internet en 2 minutos. Reiniciando la Raspberry Pi...")
                        reiniciar_raspberry()
                print("Conexión a Internet restablecida. Retomando la reproducción.")
                player.play()
    except:
        print("error inesperado, espere...")

    # Liberar recursos de VLC al finalizar
    player.release()

def reiniciar_raspberry():
    print("Reiniciando la Raspberry Pi...")
    subprocess.run(["sudo", "reboot"])

# Enlace del video que deseas reproducir
video_enlace = "http://186.4.224.169:8080/livestream/stream.m3u8"

while True:
    if check_internet_connection():
        print("Conexión a Internet establecida. Reproduciendo video en VLC.")
        reproducir_video(video_enlace)
    else:
        print("No hay conexión a Internet. Esperando...")
        while not check_internet_connection():
            time.sleep(10)
        print("Conexión a Internet restablecida... Retomando la reproducción en un momento.")
