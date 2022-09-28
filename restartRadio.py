import os

dir_path = os.path.dirname(os.path.realpath(__file__))
txt_path = dir_path + '/pyt.txt'

os.system('pgrep python3 > '+txt_path)
archivo = open(txt_path)
linea = archivo.readlines()

if(len(linea) > 1):
    for i in range(0, len(linea)-1):
        os.system('kill -9 '+linea[i])
radio_path = dir_path + '/testR.py'
os.system('python3 '+radio_path)
