import os

os.system('pgrep python3 > /home/orange/Desktop/radio/pyt.txt')
archivo = open('/home/orange/Desktop/radio/pyt.txt')
linea = archivo.readlines()
#l = linea[len(linea)-1]
#l = linea[1]
#print(l)

#lsof +D /home/orange/Desktop/radio

if(len(linea) > 1):
	for i in range(0,len(linea)-1):
		os.system('kill -9 '+linea[i])

os.system('python3 /home/orange/Desktop/radio/testR.py')