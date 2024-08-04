import pygame
import pandas as pd

# Load the CSV file with the correct delimiter
file_path = './data/Mapa.csv'
mapa_df = pd.read_csv(file_path, delimiter=';', header=None)

# Convert the DataFrame to a list of lists (matrix)
mapa_matrix = mapa_df.values.tolist()

# pygame setup
pygame.init()
screen = pygame.display.set_mode((950, 550))
clock = pygame.time.Clock()
running = True

# Load and scale images
grass = pygame.image.load("data/grass.png")
tree = pygame.image.load("data/tree.png")
rock = pygame.image.load("data/rock.png")
gate = pygame.image.load("data/portao.png")
gateOpen = pygame.image.load("data/portaoAberto.png")
house = pygame.image.load("data/casa.png")
fort = pygame.image.load("data/forte.png")
temple = pygame.image.load("data/temple.png")

propSize = (50, 60)
treeSize = (50, 75)
gateOpenSize = (74,60)
playerSize = (60,60)
sideAttackSize = (80 ,60)
grassSize = (950, 575)
houseSize = (150, 175)
fortSize = (150, 225)
templeSize = (250, 325)

tree = pygame.transform.scale(tree, treeSize)
rock = pygame.transform.scale(rock, propSize)
gate = pygame.transform.scale(gate, propSize)
gateOpen = pygame.transform.scale(gateOpen, gateOpenSize)
house = pygame.transform.scale(house, houseSize)
fort = pygame.transform.scale(fort, fortSize)
temple = pygame.transform.scale(temple, templeSize)

# Load and Scale Player Animation
player_images = {
    'up_idle': pygame.transform.scale(pygame.image.load("data/PCimaParado.png"), playerSize),
    'up_move': pygame.transform.scale(pygame.image.load("data/PCimaMov.png"), playerSize),
    'down_idle': pygame.transform.scale(pygame.image.load("data/PBaixoParado.png"), playerSize),
    'down_move': pygame.transform.scale(pygame.image.load("data/PBaixoMov.png"), playerSize),
    'left_idle': pygame.transform.scale(pygame.image.load("data/PEsqParado.png"), playerSize),
    'left_move': pygame.transform.scale(pygame.image.load("data/PEsqMov.png"), playerSize),
    'right_idle': pygame.transform.scale(pygame.image.load("data/PDirParado.png"), playerSize),
    'right_move': pygame.transform.scale(pygame.image.load("data/PDirMov.png"), playerSize),
    
    'cima_golpe': pygame.transform.scale(pygame.image.load("data/GolpeCima.png"), playerSize),
    'baixo_golpe': pygame.transform.scale(pygame.image.load("data/GolpeBaixo.png"), playerSize),
    'dir_golpe': pygame.transform.scale(pygame.image.load("data/GolpeDir.png"), sideAttackSize),
    'esq_golpe': pygame.transform.scale(pygame.image.load("data/GolpeEsq.png"), sideAttackSize)
}

enemy_images = {
    'up_idle': pygame.transform.scale(pygame.image.load("data/EnCima.png"), playerSize),
    'up_move': pygame.transform.scale(pygame.image.load("data/EnCimaMov.png"), playerSize),
    'down_idle': pygame.transform.scale(pygame.image.load("data/EnBaixo.png"), playerSize),
    'down_move': pygame.transform.scale(pygame.image.load("data/EnBaixoMov.png"), playerSize),
    'left_idle': pygame.transform.scale(pygame.image.load("data/EnEsquerda.png"), playerSize),
    'left_move': pygame.transform.scale(pygame.image.load("data/EnEsquerdaMov.png"), playerSize),
    'right_idle': pygame.transform.scale(pygame.image.load("data/EnDireita.png"), playerSize),
    'right_move': pygame.transform.scale(pygame.image.load("data/EnDireitaMov.png"), playerSize),
    'dead': pygame.transform.scale(pygame.image.load("data/EnMorto.png"), playerSize),
    
    'cima_golpe': pygame.transform.scale(pygame.image.load("data/EnCimaGolpe.png"), playerSize),
    'baixo_golpe': pygame.transform.scale(pygame.image.load("data/EnBaixoGolpe.png"), playerSize),
    'cima_dano': pygame.transform.scale(pygame.image.load("data/EnCimaDano.png"), playerSize),
    'baixo_dano': pygame.transform.scale(pygame.image.load("data/EnBaixoDano.png"), playerSize),
    'dir_golpe': pygame.transform.scale(pygame.image.load("data/EnDirGolpe.png"), playerSize),
    'esq_golpe': pygame.transform.scale(pygame.image.load("data/EnEsqGolpe.png"), playerSize),
    'dir_dano': pygame.transform.scale(pygame.image.load("data/EnDirDano.png"), playerSize),
    'esq_dano': pygame.transform.scale(pygame.image.load("data/EnEsqDano.png"), playerSize),
}

# NPC Load
smith = pygame.image.load("data/ferreiro.png")
guard = pygame.image.load("data/guard.png")

homem = pygame.image.load("data/ManNPC.png")
mulher = pygame.image.load("data/WomanNPC.png")

smith = pygame.transform.scale(smith, propSize)
guard = pygame.transform.scale(guard, propSize)

NPCsize = (60, 65)

homem = pygame.transform.scale(homem, NPCsize)
mulher = pygame.transform.scale(mulher, NPCsize)


# Fonts and Texts
pygame.font.init()
font = pygame.font.SysFont('Arial', 20)