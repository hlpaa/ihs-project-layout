import pygame
from setup import *

def dialogs(screen,mapa_matrix, yMapLocation, xMapLocation):
     
    if(mapa_matrix[yMapLocation-1][xMapLocation] == 11):
        pygame.draw.rect(screen, (100,100,100), (20,400,800,100))
        linha1 = font.render('Nossa Orbe foi roubada pelo Imperador, você precisa recuperá-la para lutarmos ', True, (255, 255, 255))
        linha2 = font.render('pela nossa independencia! Não suportamos mais essa tirania!', True, (255, 255, 255))
        linha3 = font.render('Procure o ferreiro a leste, ele vai te ajudar na sua missão!', True, (255, 255, 255))
        screen.blit(linha1, (50, 410))
        screen.blit(linha2, (50, 430))
        screen.blit(linha3, (50, 460))     
        
    elif(mapa_matrix[yMapLocation-1][xMapLocation] == 12):
        pygame.draw.rect(screen, (100,100,100), (20,400,800,100))
        linha1 = font.render('Olá, sou Erik o ferreiro, soube que você vai recuperar nossa Orbe do Poder!', True, (255, 255, 255))
        linha2 = font.render('Use os botões da placa para atacar usando a espada, cada botão é uma direção:', True, (255, 255, 255))
        linha3 = font.render('1ª botão -> Oeste, 2ª Botão -> Leste, 3ª Botão -> Norte, 4ª Botão -> Sul', True, (255, 255, 255))
        screen.blit(linha1, (50, 410))
        screen.blit(linha2, (50, 440))
        screen.blit(linha3, (50, 460))

    elif(mapa_matrix[yMapLocation-1][xMapLocation] == 13):
        pygame.draw.rect(screen, (100,100,100), (20,400,800,100))
        linha1 = font.render('Olá, sou Jhon o ferreiro, Erik me falou que você precisava de ajuda!', True, (255, 255, 255))
        linha2 = font.render('Nosso porteiro foi para a cidade de Luvitan ao norte para juntar soldados', True, (255, 255, 255))
        linha3 = font.render('e deixou nesse portão o seu filho, a senha da cidade de Luvitan é 432', True, (255, 255, 255))
        screen.blit(linha1, (50, 410))
        screen.blit(linha2, (50, 440))
        screen.blit(linha3, (50, 460))
        
    elif(mapa_matrix[yMapLocation-1][xMapLocation] == 14):
        pygame.draw.rect(screen, (100,100,100), (20,400,800,100))
        linha1 = font.render('Sou o monge do Templo de Luvitan! Ainda estamos resistindo aos avanços do', True, (255, 255, 255))
        linha2 = font.render('Império! A leste da cidade de Tuili fica a Floresta Negra, o caminho para a', True, (255, 255, 255))
        linha3 = font.render('capital do Império e ao castelo do Imperador. A senha de sua porta é 1313', True, (255, 255, 255))
        screen.blit(linha1, (50, 410))
        screen.blit(linha2, (50, 440))
        screen.blit(linha3, (50, 460))

    elif(mapa_matrix[yMapLocation-1][xMapLocation] == 15):
        pygame.draw.rect(screen, (100,100,100), (20,400,800,100))
        linha1 = font.render('Sou o monge do Templo do Fogo! Orgulhosa capital do Império! Ao norte fica', True, (255, 255, 255))
        linha2 = font.render('o incrível castelo do nosso Imperador e fortemente guardado e protegido!!!', True, (255, 255, 255))
        linha3 = font.render('Apenas eu e o Imperador sabemos a sua senha e você nunca vai descobrir!!', True, (255, 255, 255))
        screen.blit(linha1, (50, 410))
        screen.blit(linha2, (50, 440))
        screen.blit(linha3, (50, 460))
        
    elif(mapa_matrix[yMapLocation-1][xMapLocation] == 17):
        pygame.draw.rect(screen, (100,100,100), (20,400,800,100))
        linha1 = font.render('Sou o Guarda do Portão, vou te ensinar a passar pelos portões que você encontrar!', True, (255, 255, 255))
        linha2 = font.render('Os Switchs da placa serão sua chave, cada porta tem sua senha, você precisa', True, (255, 255, 255))
        linha3 = font.render('combinar para dar o número binário da senha. A senha dessa porta é 12345', True, (255, 255, 255))
        screen.blit(linha1, (50, 410))
        screen.blit(linha2, (50, 440))
        screen.blit(linha3, (50, 460))
        
    elif(mapa_matrix[yMapLocation-1][xMapLocation] == 19):
        pygame.draw.rect(screen, (100,100,100), (20,400,800,100))
        linha1 = font.render('Obrigado por me salvar, sou eternamente grato a você!!!', True, (255, 255, 255))
        linha2 = font.render('Estou muito machucado então não poderei te levar até a porta, ela fica a leste', True, (255, 255, 255))
        linha3 = font.render('daqui e a senha dela é 18', True, (255, 255, 255))
        screen.blit(linha1, (50, 410))
        screen.blit(linha2, (50, 440))
        screen.blit(linha3, (50, 460))

    elif(mapa_matrix[yMapLocation-1][xMapLocation] == 20):
        pygame.draw.rect(screen, (100,100,100), (20,400,800,100))
        linha1 = font.render('Meu pai me deixou aqui para cuidar do portão, mas eu não lembro da senha', True, (255, 255, 255))
        linha2 = font.render('Apenas quem lembra da senha é o monge do tempo de Luvitan ou meu pai', True, (255, 255, 255))
        screen.blit(linha1, (50, 410))
        screen.blit(linha2, (50, 440))

    elif(mapa_matrix[yMapLocation-1][xMapLocation] == 21):
        pygame.draw.rect(screen, (100,100,100), (20,400,800,100))
        linha1 = font.render('A Oeste está nosso templo sagrado onde guardavamos nossa Orbe, mas ela foi', True, (255, 255, 255))
        linha2 = font.render('roubada pelo Imperador! Meu filho morreu na luta contra o Império...', True, (255, 255, 255))
        screen.blit(linha1, (50, 410))
        screen.blit(linha2, (50, 440))

    elif (mapa_matrix[yMapLocation-1][xMapLocation] == 27):
        pygame.draw.rect(screen, (100,100,100), (20,400,800,100))
        linha1 = font.render('Estou esperando meu filho retornar, ele ia para a vila de Tuili ao sul buscar', True, (255, 255, 255))
        linha2 = font.render('umas espadas, mas ainda não retornou', True, (255, 255, 255))
        screen.blit(linha1, (50, 410))
        screen.blit(linha2, (50, 440))
        
    elif(mapa_matrix[yMapLocation-1][xMapLocation] == 28):
        pygame.draw.rect(screen, (100,100,100), (20,400,800,100))
        linha1 = font.render('Essa floresta é dominada pelo Império, o guarda da porta da próxima cidade foi', True, (255, 255, 255))
        linha2 = font.render('capturado e está em algum dos fortes construidos nessa floresta, você pode', True, (255, 255, 255))
        linha3 = font.render('salva-lo ou tentar sua sorte no Labirinto Secreto ao sul, escolha seu caminho', True, (255, 255, 255))
        screen.blit(linha1, (50, 410))
        screen.blit(linha2, (50, 430))
        screen.blit(linha3, (50, 450))

    elif(mapa_matrix[yMapLocation-1][xMapLocation] == 29):
        pygame.draw.rect(screen, (100,100,100), (20,400,800,100))
        linha1 = font.render('Essa é a entrada do Labirinto Secreto!', True, (255, 255, 255))
        linha2 = font.render('Tome cuidado pois poucas pessoas sobrevivem aqui, o meu pai me enviou para buscar', True, (255, 255, 255))
        linha3 = font.render('umas espadas na vila mas o porteiro foi capturado, e eu tenho medo do Labirinto', True, (255, 255, 255))
        screen.blit(linha1, (50, 410))
        screen.blit(linha2, (50, 430))
        screen.blit(linha3, (50, 450))

    elif(mapa_matrix[yMapLocation-1][xMapLocation] == 30):
        pygame.draw.rect(screen, (100,100,100), (20,400,800,100))
        linha1 = font.render('Ainda bem que sua mãe nos enviou para nos ajudar! Estou responsavel por você', True, (255, 255, 255))
        linha2 = font.render('Se precisar descansar para recuperar a vida, só precisa falar comigo novamente!', True, (255, 255, 255))
        screen.blit(linha1, (50, 410))
        screen.blit(linha2, (50, 440))


    elif(mapa_matrix[yMapLocation-1][xMapLocation] == 31):
        pygame.draw.rect(screen, (100,100,100), (20,400,800,100))
        linha1 = font.render('Meu marido, o ferreiro Erik, foi o único sobrevivente da batalha da Orbe,', True, (255, 255, 255))
        linha2 = font.render('ele pode te ajudar na sua missão, a cabana dele fica a leste da vila', True, (255, 255, 255))
        screen.blit(linha1, (50, 410))
        screen.blit(linha2, (50, 440))

    elif(mapa_matrix[yMapLocation-1][xMapLocation] == 36):
        pygame.draw.rect(screen, (100,100,100), (20,400,800,100))
        linha1 = font.render('Não aguento mais meu marido, o Monge, falando do Império isso e aquilo, se eu', True, (255, 255, 255))
        linha2 = font.render('pudesse falaria para todo mundo que a senha da porta é 111 mas ele não deixa...', True, (255, 255, 255))
        screen.blit(linha1, (50, 410))
        screen.blit(linha2, (50, 440))

    elif(mapa_matrix[yMapLocation-1][xMapLocation] == 39):
        pygame.draw.rect(screen, (100,100,100), (20,400,800,100))
        linha1 = font.render('Cuidado, aqui é a entrada do castelo do Imperador, ele é fortemente protegido e ', True, (255, 255, 255))
        linha2 = font.render('apenas passe se tiver certeza que está pronto. A sua senha é guardada pelo Monge', True, (255, 255, 255))
        screen.blit(linha1, (50, 410))
        screen.blit(linha2, (50, 440))
