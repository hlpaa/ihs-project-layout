import pygame

pygame.mixer.init()

pygame.mixer.music.load("data/inicio.mp3")

def checkPortao(valor, gate):
    if(valor == 51 and gate[1]):
        return True
    if(valor == 52 and gate[2]):
        return True
    if(valor == 53 and gate[3]):
        return True
    if(valor == 54 and gate[4]):
        return True
    if(valor == 55 and gate[5]):
        return True
    if(valor == 56 and gate[6]):
        return True