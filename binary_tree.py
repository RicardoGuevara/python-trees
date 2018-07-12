# Ricardo G. Payán // Árboles binarios

from threading import Thread
from tkinter import *
import logging
import time

#TDA para cada nodo raiz dentro del arbol binario
class Arbin(object):
    
    content = object()

    def __init__(self,content_in):
        self.content = content_in
        print("test")        

    def definePos(self,root_in,orientation):
        self.root_arbin = root_in
        if orientation:
            self.root_arbin.rgt_arbin = self
        else:
            self.root_arbin.lft_arbin = self

class Aplication:
    
    def __init__(self):
        self.root_window = Tk()

    def generate(self):
        self.root_window.mainloop()

#Genera la interfaz de usuario
def gui_loader():
    logging.debug("hilo de vtn lanzado")
    root_window = Aplication()
    root_window.generate()

#Establece un hilo paralelo para la ejecución de la interfaz de usuario
try:
    graph_init = Thread(target=gui_loader,name="root_window")
    graph_init.start()
except Exception:
    raise TypeError("i seriously want to die")
finally:
    print("principal_thread_end")
