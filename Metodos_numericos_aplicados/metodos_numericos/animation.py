import time
import sys
import threading

done = False
texto = ''

def text(string):
    global texto
    texto = string

def the_process_function():
    n = 10000000000000000
    global l
    global texto
    global intervalo
    for i in range(n):
        string = texto
        if done == True:
            break
        sys.stdout.write('\r'+string)
        sys.stdout.flush()
        time.sleep(intervalo)
'''
def animated_loading():
    chars = "/—\|" 
    for char in chars:
        sys.stdout.write('\r '+char)
        time.sleep(.1)
        sys.stdout.flush() 
'''


the_process = threading.Thread(name='process', target=the_process_function)

def start(intervalo_tempo):
    global intervalo
    intervalo = intervalo_tempo
    the_process.start()
    #while the_process.is_alive():
    #    animated_loading()
        
def stop():
    global done
    done = True

if __name__ == "__main__":
    l = [0,0]
    intervalo = 0.25
    text(f"        Nº de termos: {l[1]}       Erro: {l[0]} ")
    start()
