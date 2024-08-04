import pygame
from setup import *
from dialog import *
from func import *
from Integration import *

# Initial positions
xPos = 13
yPos = 15
xMapLocation = 13
yMapLocation = 15

# integration = Integration()

# Movement control
wPressed = False
aPressed = False
sPressed = False
dPressed = False

golpeAnimation = [False] * 4

gateArray = [False] * 7

vidaPlayer = 20

dificulty = 0

contadorInimigos = 0
inimigos = []

dispawn = []



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_images['down_idle']
        self.rect = self.image.get_rect(center=(475, 260))
        self.status = 'down_idle'
    
    def update(self):
        global xPos, yPos, xMapLocation, yMapLocation, wPressed, aPressed, sPressed, dPressed, playerStatus, vidaPlayer
        keys = pygame.key.get_pressed()
        moved = False
        
        if keys[pygame.K_w] and not wPressed and not ((mapa_matrix[yMapLocation-1][xMapLocation] > 0) and not checkPortao(mapa_matrix[yMapLocation-1][xMapLocation], gateArray)):
            yPos -= 0.5
            wPressed = True
            yMapLocation -= 1
            self.status = 'up_move'
            moved = True
        elif wPressed and not keys[pygame.K_w]:
            wPressed = False
            yPos -= 0.5
            self.status = 'up_idle'
        elif keys[pygame.K_w]:
            self.status = 'up_idle'
            dialogs(screen,mapa_matrix, yMapLocation, xMapLocation)
            if mapa_matrix[yMapLocation-1][xMapLocation] == 30:
                vidaPlayer = 16
                        
        if keys[pygame.K_s] and not sPressed and not ((mapa_matrix[yMapLocation+1][xMapLocation] > 0) and not checkPortao(mapa_matrix[yMapLocation+1][xMapLocation], gateArray)):
            yPos += 0.5
            sPressed = True
            yMapLocation += 1
            self.status = 'down_move'
            moved = True
        elif sPressed and not keys[pygame.K_s]:
            sPressed = False
            yPos += 0.5
            self.status = 'down_idle'
        elif keys[pygame.K_s]:
            self.status = 'down_idle'
        
        if keys[pygame.K_a] and not aPressed and not (mapa_matrix[yMapLocation][xMapLocation-1] > 0):
            xPos -= 0.5
            aPressed = True
            xMapLocation -= 1
            self.status = 'left_move'
            moved = True
        elif aPressed and not keys[pygame.K_a]:
            aPressed = False
            xPos -= 0.5
            self.status = 'left_idle'
        elif keys[pygame.K_a]:
            self.status = 'left_idle'
        
        if keys[pygame.K_d] and not dPressed and not (mapa_matrix[yMapLocation][xMapLocation+1] > 0):
            xPos += 0.5
            dPressed = True
            xMapLocation += 1
            self.status = 'right_move'
            moved = True
        elif dPressed and not keys[pygame.K_d]:
            dPressed = False
            xPos += 0.5
            self.status = 'right_idle'
        elif keys[pygame.K_d]:
            self.status = 'right_idle'
        
        botao = 5
        integration = Integration()
        
        if (keys[pygame.K_UP] or not integration.Read_Button(1)) and not golpeAnimation[0]: 
            self.status = 'cima_golpe'
            golpeAnimation[0] = True
            HitCheck(xMapLocation, yMapLocation - 1, 0)
        elif golpeAnimation[0]:
            self.status = 'up_idle'
            golpeAnimation[0] = False
            
        if (keys[pygame.K_RIGHT] or not integration.Read_Button(2)) and not golpeAnimation[1]: 
            self.status = 'dir_golpe'
            golpeAnimation[1] = True
            HitCheck(xMapLocation + 1, yMapLocation, 1)
        elif golpeAnimation[1]:
            self.status = 'right_idle'
            golpeAnimation[1] = False
            
        if (keys[pygame.K_DOWN] or not integration.Read_Button(0)) and not golpeAnimation[2]: 
            self.status = 'baixo_golpe'
            golpeAnimation[2] = True
            HitCheck(xMapLocation, yMapLocation + 1, 2)
        elif golpeAnimation[2]:
            self.status = 'down_idle'
            golpeAnimation[2] = False
            
        if (keys[pygame.K_LEFT] or not integration.Read_Button(3)) and not golpeAnimation[3]: 
            self.status = 'esq_golpe'
            golpeAnimation[3] = True
            HitCheck(xMapLocation - 1, yMapLocation , 3)
        elif golpeAnimation[3]:
            self.status = 'left_idle'
            golpeAnimation[3] = False
        
        
        self.image = player_images[self.status]
        self.rect = self.image.get_rect(center=(475, 250))
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self, xDefEn, yDefEn):
        super().__init__()
        self.status = 'down_idle'
        self.EnxPos = xDefEn
        self.EnxAni = xDefEn
        self.EnyPos = yDefEn
        self.EnyAni = yDefEn
        self.direction = [0] * 4
        self.image = enemy_images['down_idle']
        self.rect = self.image.get_rect(center = (((self.EnxAni - xPos + 9) * 50) + 25, ((self.EnyAni - yPos + 5) * 50) + 25))
        self.attackAnimation = [0] * 4
        self.vivo = True
        self.timerCorpo = 0
    
    def update(self, cout):
        global vidaPlayer, dispawn
        mapa_matrix[self.EnyPos][self.EnxPos] = 0
        
        if self.vivo:
            if (yMapLocation < self.EnyPos) and (self.direction[0] == 0) and not (mapa_matrix[self.EnyPos - 1][self.EnxPos] > 0) and not ((yMapLocation + 1 == self.EnyPos) and (xMapLocation == self.EnxPos)):
                self.EnyPos -= 1
                self.EnyAni -= 0.5
                self.direction[0] = 1
                self.status = 'up_move'
            elif self.direction[0] > 10 - (6 - (dificulty*2)):
                self.direction[0] = 0
            elif self.direction[0] == 5 - (3 - dificulty):
                self.direction[0] += 1
                self.EnyAni -= 0.5
                self.status = 'up_idle'
            elif self.direction[0] > 0:
                self.direction[0] += 1
            
            if (yMapLocation > self.EnyPos) and (self.direction[1] == 0) and not (mapa_matrix[self.EnyPos + 1][self.EnxPos] > 0)  and not ((yMapLocation - 1 == self.EnyPos) and (xMapLocation == self.EnxPos)):
                self.EnyPos += 1
                self.EnyAni += 0.5
                self.direction[1] = 1
                self.status = 'down_move'
            elif self.direction[1] > 10 - (6 - (dificulty*2)):
                self.direction[1] = 0
            elif self.direction[1] == 5 - (3 - dificulty):
                self.EnyAni += 0.5
                self.status = 'down_idle'
                self.direction[1] += 1
            elif self.direction[1] > 0:
                self.direction[1] += 1
            
            if (xMapLocation < self.EnxPos) and (self.direction[2] == 0) and not (mapa_matrix[self.EnyPos][self.EnxPos - 1] > 0) and not ((yMapLocation == self.EnyPos) and (xMapLocation + 1 == self.EnxPos)):
                self.EnxPos -= 1
                self.EnxAni -= 0.5
                self.direction[2] = 1
                self.status = 'left_move'
            elif self.direction[2] > 10 - (6 - (dificulty*2)):
                self.direction[2] = 0
            elif self.direction[2] == 5 - (3 - dificulty):
                self.direction[2] += 1
                self.EnxAni -= 0.5
                self.status = 'left_idle'
            elif self.direction[2] > 0:
                self.direction[2] += 1
            
            if (xMapLocation > self.EnxPos) and (self.direction[3] == 0) and not (mapa_matrix[self.EnyPos][self.EnxPos + 1] > 0) and not ((yMapLocation == self.EnyPos) and (xMapLocation - 1 == self.EnxPos)):
                self.EnxPos += 1
                self.EnxAni += 0.5
                self.direction[3] = 1
                self.status = 'right_move'
            elif self.direction[3] > 10 - (6 - (dificulty*2)):
                self.direction[3] = 0
            elif self.direction[3] == 5 - (3 - dificulty):
                self.EnxAni += 0.5
                self.status = 'right_idle'
                self.direction[3] += 1
            elif self.direction[3] > 0:
                self.direction[3] += 1
                
            if yMapLocation == (self.EnyPos - 1) and (self.attackAnimation[0] == 0) and xMapLocation == self.EnxPos: 
                self.attackAnimation[0] = 1
                self.status = 'up_idle'
            elif self.attackAnimation[0] > 4 + dificulty:
                self.attackAnimation[0] = 0
                if yMapLocation == (self.EnyPos - 1) and (self.attackAnimation[0] == 0) and xMapLocation == self.EnxPos:
                    self.status = 'cima_dano'
                    vidaPlayer -= 1
                    screen.fill('red')
            elif self.attackAnimation[0] > 0:
                self.status = 'cima_golpe'
                self.attackAnimation[0] += 1
                
            if xMapLocation == (self.EnxPos + 1) and (self.attackAnimation[1] == 0) and yMapLocation == self.EnyPos: 
                self.attackAnimation[1] = 1
                self.status = 'right_idle'
            elif self.attackAnimation[1] > 4 + dificulty:
                self.attackAnimation[1] = 0
                if xMapLocation == (self.EnxPos + 1) and (self.attackAnimation[1] == 0) and yMapLocation == self.EnyPos:
                    vidaPlayer -= 1
                    screen.fill('red')
                    self.status = 'dir_dano'
            elif self.attackAnimation[1] > 0:
                self.status = 'dir_golpe'
                self.attackAnimation[1] += 1
                
            if yMapLocation == (self.EnyPos + 1) and (self.attackAnimation[2] == 0) and xMapLocation == self.EnxPos: 
                self.attackAnimation[2] = 1
                self.status = 'down_idle'
            elif self.attackAnimation[2] > 4 + dificulty:
                self.attackAnimation[2] = 0
                if yMapLocation == (self.EnyPos + 1) and (self.attackAnimation[2] == 0) and xMapLocation == self.EnxPos:
                    vidaPlayer -= 1 
                    screen.fill('red')
                    self.status = 'baixo_dano'
            elif self.attackAnimation[2] > 0:
                self.status = 'baixo_golpe'
                self.attackAnimation[2] += 1
                
            if xMapLocation == (self.EnxPos - 1) and (self.attackAnimation[3] == 0) and yMapLocation == self.EnyPos:
                self.attackAnimation[3] = 1
                self.status = 'left_idle'
            elif self.attackAnimation[3] > 4 + dificulty:
                self.attackAnimation[3] = 0
                if xMapLocation == (self.EnxPos - 1) and (self.attackAnimation[3] == 0) and yMapLocation == self.EnyPos: 
                    vidaPlayer -= 1
                    self.status = 'esq_dano'
                    screen.fill('red')
            elif self.attackAnimation[3] > 0:
                self.status = 'esq_golpe'
                self.attackAnimation[3] += 1
            
            mapa_matrix[self.EnyPos][self.EnxPos] = 95
        elif self.timerCorpo < 100:
            self.timerCorpo += 1
            self.status = 'dead'
        else:
            dispawn[cout] = 1
        
        self.image = enemy_images[self.status]
        self.rect = self.image.get_rect(center = (((self.EnxAni - xPos + 9) * 50) + 25, ((self.EnyAni - yPos + 5) * 50)))
        
    def checkHit(self, xHit, yHit, direction):
        if(direction == 0) and (xHit >= self.EnxPos -1 and xHit <= self.EnxPos + 1 and yHit == self.EnyPos):
            self.vivo = False
        if(direction == 1) and (yHit >= self.EnyPos -1 and yHit <= self.EnyPos + 1 and xHit == self.EnxPos):
            self.vivo = False
        if(direction == 2) and (xHit >= self.EnxPos -1 and xHit <= self.EnxPos + 1 and yHit == self.EnyPos):
            self.vivo = False
        if(direction == 3) and (yHit >= self.EnyPos -1 and yHit <= self.EnyPos + 1 and xHit == self.EnxPos):
            self.vivo = False
        
        
        

def gerarBlocos():
    global inimigos, contadorInimigos
    for xGrass in range(xMapLocation-12, xMapLocation+12):
        for yGrass in range(yMapLocation-8, yMapLocation+8):
            if xGrass % 4 == 0 and yGrass % 4 == 0:
                grama(xGrass, yGrass)
    
    for xB in range(yMapLocation-8, yMapLocation+8):
        for yB in range(xMapLocation-13, xMapLocation+13):
            if xB > 99 or yB > 99:
                i = 1
            elif mapa_matrix[xB][yB] == 1:
                arvore(yB, xB)
            elif mapa_matrix[xB][yB] == 2:
                casa(yB, xB)
            elif mapa_matrix[xB][yB] == 3:
                templo(yB, xB)
            elif mapa_matrix[xB][yB] == 4:
                forte(yB, xB)
            elif mapa_matrix[xB][yB] == 6:
                pedra(yB, xB)
            elif mapa_matrix[xB][yB] == 12 or mapa_matrix[xB][yB] == 13 or mapa_matrix[xB][yB] == 18 or mapa_matrix[xB][yB] == 19 or mapa_matrix[xB][yB] == 20:
                ferreiro(yB, xB)
            elif mapa_matrix[xB][yB] == 11 or mapa_matrix[xB][yB] == 14 or mapa_matrix[xB][yB] == 15 or mapa_matrix[xB][yB] == 16 or mapa_matrix[xB][yB] == 17:
                guarda(yB, xB)
            elif mapa_matrix[xB][yB] > 20 and mapa_matrix[xB][yB] < 30:
                man(yB, xB)
            elif mapa_matrix[xB][yB] >= 30 and mapa_matrix[xB][yB] < 40:
                woman(yB, xB)
            elif mapa_matrix[xB][yB] == 51 and gateArray[1] == False:
                portao(yB,xB)
            elif mapa_matrix[xB][yB] == 51 and gateArray[1] == True:
                portaoAberto(yB,xB)
            elif mapa_matrix[xB][yB] == 52 and gateArray[2] == False:
                portao(yB,xB)
            elif mapa_matrix[xB][yB] == 52 and gateArray[2] == True:
                portaoAberto(yB,xB)
            elif mapa_matrix[xB][yB] == 53 and gateArray[3] == False:
                portao(yB,xB)
            elif mapa_matrix[xB][yB] == 53 and gateArray[3] == True:
                portaoAberto(yB,xB)
            elif mapa_matrix[xB][yB] == 54 and gateArray[4] == False:
                portao(yB,xB)
            elif mapa_matrix[xB][yB] == 54 and gateArray[4] == True:
                portaoAberto(yB,xB)
            elif mapa_matrix[xB][yB] == 55 and gateArray[5] == False:
                portao(yB,xB)
            elif mapa_matrix[xB][yB] == 55 and gateArray[5] == True:
                portaoAberto(yB,xB)
            elif mapa_matrix[xB][yB] == 56 and gateArray[6] == False:
                portao(yB,xB)
            elif mapa_matrix[xB][yB] == 56 and gateArray[6] == True:
                portaoAberto(yB,xB)
            elif mapa_matrix[xB][yB] == 91:
                inimigo = Enemy(yB,xB)
                inimigos.append(pygame.sprite.Group(inimigo))
                dispawn.append(0)
                contadorInimigos += 1
                

def grama(xB, yB):
    screen.blit(grass, (50 * (xB - xPos + 9), (50 * (yB - yPos + 5))))

def arvore(xB, yB):
    screen.blit(tree, (50 * (xB - xPos + 9), (50 * (yB - yPos + 5)) - 25))
    
def pedra(xB, yB):
    screen.blit(rock, (50 * (xB - xPos + 9), (50 * (yB - yPos + 5)) - 25))

def portao(xB, yB):
    screen.blit(gate, (50 * (xB - xPos + 9), (50 * (yB - yPos + 5)) - 20))

def portaoAberto(xB, yB):
    screen.blit(gateOpen, (50 * (xB - xPos + 9) - 11, (50 * (yB - yPos + 5)) - 20))

def casa(xB, yB):
    screen.blit(house, (50 * (xB - xPos + 9), (50 * (yB - yPos + 5)) - 25))

def templo(xB, yB):
    screen.blit(temple, (50 * (xB - xPos + 9), (50 * (yB - yPos + 5)) - 25))

def forte(xB, yB):
    screen.blit(fort, (50 * (xB - xPos + 9), (50 * (yB - yPos + 5)) - 25))

def ferreiro(xB, yB):
    screen.blit(smith, (50 * (xB - xPos + 9), (50 * (yB - yPos + 5)) - 10))

def guarda(xB, yB):
    screen.blit(guard, (50 * (xB - xPos + 9), (50 * (yB - yPos + 5)) - 10))
    
def man(xB, yB):
    screen.blit(homem, (((50 * (xB - xPos + 9)) - 5), ((50 * (yB - yPos + 5)) - 20)))
    
def woman(xB, yB):
    screen.blit(mulher, (((50 * (xB - xPos + 9)) - 5), ((50 * (yB - yPos + 5)) - 20)))
    
def gateCheck():
    global yMapLocation, xMapLocation, wPressed, yPos, xPos, sPressed
    
    Valor = 0
    strValor = "000111"
    
    integration = Integration()
    [Valor, strValor] = integration.Read_Switches()
    keys = pygame.key.get_pressed()
    
    if (mapa_matrix[yMapLocation-1][xMapLocation] == 51 or mapa_matrix[yMapLocation+1][xMapLocation] == 51) and not gateArray[1]:
        pygame.draw.rect(screen, (100,20,20), (200,400,500,100))
        linha1 = font.render('Insira a senha do Portão', True, (255, 255, 255))
        linha2 = font.render(strValor, True, (255, 255, 255))
        screen.blit(linha1, (250, 410))
        screen.blit(linha2, (250, 440))
        if(Valor == 12345) or keys[pygame.K_p]:
            gateArray[1] = True
    
    if (mapa_matrix[yMapLocation-1][xMapLocation] == 52 or mapa_matrix[yMapLocation+1][xMapLocation] == 52) and not gateArray[2]:
        pygame.draw.rect(screen, (100,20,20), (200,400,500,100))
        linha1 = font.render('Insira a senha do Portão', True, (255, 255, 255))
        linha2 = font.render(strValor, True, (255, 255, 255))
        screen.blit(linha1, (250, 410))
        screen.blit(linha2, (250, 440))
        if(Valor == 18) or keys[pygame.K_p]:
            gateArray[2] = True
        
    if (mapa_matrix[yMapLocation-1][xMapLocation] == 53 or mapa_matrix[yMapLocation+1][xMapLocation] == 53) and not gateArray[3]:
        pygame.draw.rect(screen, (100,20,20), (200,400,500,100))
        linha1 = font.render('Insira a senha do Portão', True, (255, 255, 255))
        linha2 = font.render(strValor, True, (255, 255, 255))
        screen.blit(linha1, (250, 410))
        screen.blit(linha2, (250, 440))
        if(Valor == 1) or keys[pygame.K_p]:
            gateArray[3] = True
    
    if (mapa_matrix[yMapLocation-1][xMapLocation] == 54 or mapa_matrix[yMapLocation+1][xMapLocation] == 54) and not gateArray[4]:
        pygame.draw.rect(screen, (100,20,20), (200,400,500,100))
        linha1 = font.render('Insira a senha do Portão', True, (255, 255, 255))
        linha2 = font.render(strValor, True, (255, 255, 255))
        screen.blit(linha1, (250, 410))
        screen.blit(linha2, (250, 440))
        if(Valor == 432) or keys[pygame.K_p]:
            gateArray[4] = True
    
    if (mapa_matrix[yMapLocation-1][xMapLocation] == 55 or mapa_matrix[yMapLocation+1][xMapLocation] == 55) and not gateArray[5]:
        pygame.draw.rect(screen, (100,20,20), (200,400,500,100))
        linha1 = font.render('Insira a senha do Portão', True, (255, 255, 255))
        linha2 = font.render(strValor, True, (255, 255, 255))
        screen.blit(linha1, (250, 410))
        screen.blit(linha2, (250, 440))
        if(Valor == 1313) or keys[pygame.K_p]:
            gateArray[5] = True
        
    if (mapa_matrix[yMapLocation-1][xMapLocation] == 56 or mapa_matrix[yMapLocation+1][xMapLocation] == 56) and not gateArray[6]:
        pygame.draw.rect(screen, (100,20,20), (200,400,500,100))
        linha1 = font.render('Insira a senha do Portão', True, (255, 255, 255))
        linha2 = font.render(strValor, True, (255, 255, 255))
        screen.blit(linha1, (250, 410))
        screen.blit(linha2, (250, 440))
        if(Valor == 111) or keys[pygame.K_p]:
            gateArray[6] = True
        

def displayVida():
    global vidaPlayer
    integration = Integration()
    integration.Write_Led_Red((2**vidaPlayer)-1)
    vida = font.render(str(vidaPlayer), True, (20, 20, 20))
    screen.blit(vida, (10, 10))
    
def displayInimigos():
    for cout in range(contadorInimigos):
        if dispawn[cout] == 0:
            inimigos[cout].update(cout)
            inimigos[cout].draw(screen)


    
def HitCheck(xHit, yHit, direction):
    for cout in range(contadorInimigos):
        for inimigo in inimigos[cout]:
            inimigo.checkHit(xHit, yHit, direction)

# Initialize player sprite
player = Player()
player_group = pygame.sprite.Group(player)

pygame.mixer.music.play(-1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if vidaPlayer > 0 and vidaPlayer < 20:
        gerarBlocos()
        gateCheck()
        displayInimigos()
        
        player_group.update()
        player_group.draw(screen)

        displayVida()

    elif vidaPlayer == 20:
        screen.fill('black')
        linha1 = font.render('Wrath of the Empire', True, (255, 255, 255))
        linha2 = font.render('Para andar, utilize as teclas wasd, segure w para falar com os NPCs', True, (255, 255, 255))
        linha3 = font.render('Para iniciar o jogo aperte K', True, (255, 255, 255))
        screen.blit(linha1, (200, 200))
        screen.blit(linha2, (120, 242))
        screen.blit(linha3, (120, 260)) 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_k]:
            vidaPlayer = 16

    else:
        screen.fill('black')
        linha1 = font.render('GAME OVER', True, (255, 255, 255))
        linha2 = font.render('Você morreu', True, (255, 255, 255))
        linha3 = font.render('Reinicie o jogo para tentar novamente', True, (255, 255, 255))
        screen.blit(linha1, (240, 200))
        screen.blit(linha2, (240, 242))
        screen.blit(linha3, (240, 260)) 

    # Update display
    pygame.display.flip()
    clock.tick(24)

pygame.quit()
