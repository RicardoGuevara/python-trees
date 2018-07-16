# Ricardo G. Payán // Árboles binarios
#Arboles binarios / Rick
from threading import Thread
from tkinter import *
import logging
import time

#just to debug something ( -_-)
def debugSomething():
    	print("it founds well ( -_-)")

#TDA para cada nodo raiz dentro del arbol binario
class Arbin(object):
    'Nodo raíz de un arbol'
    descendence = False
    content = object()

    def __init__(self,content_in):
        self.content = content_in
        print("test")        

    def definePos(self,root_in,orientation):
        self.root_arbin = root_in
        self.root_arbin.descendence = True
        if orientation:
            self.root_arbin.rgt_arbin = self
        else:
            self.root_arbin.lft_arbin = self

    def voidArbin(self):
        return not self.descendence

    def calcPeso(self):
        if self.voidArbin():
            return 0
        else:
            return 1+self.lft_arbin.calcPeso()+self.rgt_arbin.calcPeso()

    def contains(self,elem):
        if self.voidArbin():
        	return False
        elif elem == self.content:
        	return True
        else:
        	return self.lft_arbin.contains(elem) or self.rgt_arbin.contains(elem)

    def numHojas(self):
    	if self.voidArbin():
    		return 0
    	elif self.rgt_arbin.voidArbin() and self.lft_arbin.voidArbin():
    		return 1
    	else:
    		return self.rgt_arbin.numHojas() + self.lft_arbin.numHojas()

    def howMany(self,elem):
    	if self.voidArbin():
    		return 0
    	elif elem == self.content:
    		return 1  + self.lft_arbin.howMany(elem) + self.rgt_arbin.howMany(elem)
    	else:
    		return self.lft_arbin.howMany(elem) + self.rgt_arbin.howMany(elem)

    def wayExistBethween(self,elemA,elemB):
    	if self.voidArbin():
    		return False
    	elif elemA == self.content:
    		return self.contains(elemB)
    	else:
    		return self.lft_arbin.wayExistBethween(elemA,elemB) or self.rgt_arbin.wayExistBethween(elemA,elemB)
    	

class Aplication:
    'generate GUI'

    def __init__(self):
        self.root_window = Tk()
    
    def addLabel(self,label_text,anchor_in=CENTER,he_in=20,wd_in=100,bcg="white"):
        Label(self.root_window, text=label_text, anchor=anchor_in, height=he_in,width=wd_in,bg=bcg).pack()

    def addButton(self,function=debugSomething,label_text="ACTION",anchor_in=CENTER,he_in=20,wd_in=100,bcg="white"):
    	Button(self.root_window, command=function, text=label_text, anchor=anchor_in, height=he_in,width=wd_in,bg=bcg).pack()

    def addEntry(self):
    	Entry(self.root_window).pack()

    def generate(self):
        self.root_window.mainloop()
        self.root_window.destroy()
    
    def startpage(self):
        self.root_window.title("Binary tree / Ricardo Guevara")
        self.root_window.geometry("500x500")
        self.addLabel("BINARY TREES",he_in=2,wd_in=100)
        self.addButton(wd_in=20,he_in=5)
        self.addButton(wd_in=50,he_in=5,label_text="Generar una entrada de texto",function=self.addEntry)
    
#Genera la interfaz de usuario
def gui_loader():
    logging.debug("hilo de vtn lanzado")
    root_wd = Aplication()
    root_wd.startpage()
    root_wd.generate()

#Establece un hilo paralelo para la ejecución de la interfaz de usuario
try:
    graph_init = Thread(target=gui_loader,name="root_window")
    graph_init.start()
except Exception:
    raise TypeError("i seriously want to die")
finally:
    print("principal_thread_end")


#FIN