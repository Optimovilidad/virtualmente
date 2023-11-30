import vlc
import socket
import time
import subprocess

def check_internet_connection():
    try:
        # Intentar abrir una conexión a un servidor conocido (por ejemplo, el servidor de Google)
        socket.create_connection(("www.google.com", 80), timeout=5)
        return True
    except (socket.error, socket.timeout):
        return False

def play_live_stream(url, position=None):
    instance = vlc.Instance("--no-xlib")  # Especifica "--no-xlib" para evitar problemas en entornos sin GUI
    player = instance.media_player_new()
    media = instance.media_new(url)
    media.get_mrl()
    player.set_media(media)

    
    if position is not None:
        player.set_position(position)
    #try:
        # Intentar abrir una conexión a un servidor conocido (por ejemplo, el servidor de Google)
        #player.stop()
        #player.release()
        #player.play()
    #except ():
        #player.play()
    player.play()
    return player

def close_player(player, valor):
	url = "http://186.4.224.169:8080/livestream/stream.m3u8"
	try:
		#play.stop()
		#print('cerrado')
		if valor not in [vlc.State.Ended, vlc.State.Error]:
			print('parando reproduccion actual')
			player.stop()
			print('cerrado')
		else:
			print('valor cambio a ended')
			player = play_live_stream(url)
			
	except:
		print('none')
		time.sleep(20)
		reiniciar_raspberry()
		
		
		
	player.release()

def reiniciar_raspberry():
    print("Reiniciando la Raspberry Pi...")
    subprocess.run(["sudo", "reboot"])

def live_stream_program(url):
    while not check_internet_connection():
        print("Esperando a que haya conexión a Internet...")
        time.sleep(10)

    print("Conexión a Internet detectada. Reproduciendo transmisión en vivo.")
    

    player = play_live_stream(url)
    #time.sleep(10)
    # player.release()
    # time.sleep(10)
    # player = play_live_stream(url)
    #if not check_internet_connection():
         #print("Perdiendo conectividad")
         #player.release()
    while True:
        if not check_internet_connection():
            print("Se perdió la conexión a Internet. Esperando 10 segundos...")
            time.sleep(10)
            tiempo_espera = 0
            valor = ''
            while not check_internet_connection():
                print("Esperando a que la conexión a Internet se restablezca...")
                print(player.get_state())
                time.sleep(10)
                tiempo_espera +=10
                #if tiempo_espera >=70:
						#player.get_state() = 'State.Ended'
                if tiempo_espera >= 100:  # Esperar 5 minutos (300 segundos)
                        player.get_state() == vlc.State.Error
                        valor = vlc.State.Ended
                        player.get_state() == valor
                        print('estado actualizado a: ', player.get_state(), valor)
                if tiempo_espera >= 240:  # Esperar 5 minutos (300 segundos)
                        print("No se pudo establecer conexión a Internet. Reiniciando la Raspberry Pi...")
                        reiniciar_raspberry()
            print(valor)
            print("Conexión a Internet restablecida. Volviendo a abrir la transmisión en vivo.")
            #position = player.get_position()  # Obtiene la posición actual de la reproducción
            close_player(player, valor)
            print('cerrado 1')
            player = play_live_stream(url)

        time.sleep(1)

if __name__ == "__main__":
    # URL de la transmisión en vivo
    live_stream_url = "http://186.4.224.169:8080/livestream/stream.m3u8"
    # Iniciar el programa de transmisión en vivo
    live_stream_program(live_stream_url)
    

