# Ricardo G. Payán // Árboles binarios

from threading import Thread
from tkinter import *
import logging
import time

#TDA para cada nodo raiz dentro del arbol binario
class arbin(object):
    pass

#Genera la interfaz de usuario
def gui_loader():
    logging.debug("hilo de vtn lanzado")
    root_window = Tk()
    #graphics
    root_window.mainloop()
    
#Establece un hilo paralelo para la ejecución de la interfaz de usuario
try:
    graph_init = Thread(target=gui_loader,name="root_window")
    graph_init.start()
except Exception:
    print("Thread_error")
    pass
finally:
    print("end")
    pass
