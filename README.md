# Virtualmente

Aplicacion de la radio Virtual-mente

# Configuración del crontab

Para iniciar la radio al arrancar el equipo se debe configurar una tarea en el crontab

1. Ingresar al terminal
2. Escribir el comando<br>
   <b><code>$ crontab -e</code></b>
3. Agregar al final del archivo la siguiente linea<br>
   <b><code>@reboot sleep 40; python3 /home/\<Username>/\<path_to_code_location>/radio/restartRadio.py</code></b><br>
   ejemplo: <em>@reboot sleep 40; python3 /home/orange/Desktop/radio/restartRadio.py</em>

Se debe repetir los mismos pasos en el archivo crontab del usuario root. Se debe abrir el archivo con el comando <b><code>$ sudo crontab -e</code></b> y repetir el paso 3.

<b>Nota:</b> El comando python3 puede cambiar segun el sistema operativo, para determinar el comanto correcto se debe probar en el terminal el comando
<b><code>$ python3 /home/\<Username>/\<path_to_code_location>/radio/restartRadio.py</code></b>

En caso de error cambiar el <b><code>python3</code></b> por las siguientes variaciones: <b><code>python</code></b> o <b><code>py</code></b>

ejemplo: <b><code>python3 /home/orange/Desktop/radio/restartRadio.py</code></b>
