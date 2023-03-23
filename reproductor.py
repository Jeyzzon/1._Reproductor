
#JEYZON MAURILIO BARRAGAN ESPINO
from tkinter import *
import pygame, sys
from pygame.locals import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

pygame.init() 
def openFileSong():
    cancion = filedialog.askopenfilename() 
    print(cancion)
    pygame.mixer.music.load(cancion)
        
    
def playSong():
    pygame.mixer.music.play()

def stopSong():
    pygame.mixer.music.stop()

def resumeSong():
    pygame.mixer.music.unpause()
    
def pauseSong():
    pygame.mixer.music.pause()
    
def volumenUp():
    levelup=pygame.mixer.music.get_volume() +0.1
    print(levelup)
    pygame.mixer.music.set_volume(levelup)

def volumenDown():
    leveldown=pygame.mixer.music.get_volume() -0.1
    print(leveldown)
    pygame.mixer.music.set_volume(leveldown)

raiz = Tk()
raiz.title("Reproductor MP3")
raiz.geometry("900x500")
raiz.resizable(0,0)
framePrincipal = Frame(raiz, bg="#CC3300")
framePrincipal.pack(fill="both", expand=1)

Reproductorr = Label(framePrincipal, text="Reproductor MP3", font=("Arial", 20, "bold"), bg="#CC3300", fg="#fbfbfb")
Reproductorr.place(relx=0.20,rely=0.4)

botonabrir = Button(framePrincipal, text="Abrir cancion", bg="#00FF00", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=openFileSong)
botonabrir.place(relx=0.01, rely=0.5)

bottondale = Button(framePrincipal, text="reproducir", bg="#FF0000", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=playSong) #e2504c rojo, #42ab49 verde, #ffc400 amarillo, #55009 morado, #0000FF
bottondale.place(relx= 0.15, rely=0.5)

bottonparar = Button(framePrincipal, text="Parar", bg="#000000", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=stopSong)
bottonparar.place(relx= 0.3, rely=0.5)

bottoncontinuar = Button(framePrincipal, text="Continuar", bg="#FF0000", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=resumeSong)
bottoncontinuar.place(relx= 0.45, rely=0.5)

bottonPausa = Button(framePrincipal, text="Pausar", bg="#00FF00", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=pauseSong)
bottonPausa.place(relx= 0.60, rely=0.5)

bottonVolumenmas = Button(framePrincipal, text="Volumen +", bg="#FF9900", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=volumenUp)
bottonVolumenmas.place(relx= 0.15, rely=0.8)

bottonVolumenbajo = Button(framePrincipal, text="Volumen -", bg="#FF9900", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=volumenDown)
bottonVolumenbajo.place(relx= 0.45, rely=0.8)

raiz.mainloop()