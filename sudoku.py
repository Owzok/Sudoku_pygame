from math import sqrt
import pygame, sys
from datetime import datetime
import json

ancho = 550
color_fondo = (255, 255, 255)
color_valores_por_defecto = (52, 31, 151)
buffer = 5
juego_ganado = False

h_win = False
v_win = False

name = ''
clock = pygame.time.Clock()
input_rect = pygame.Rect(50,75,200,50)
name_txt = ''

#iniciar pygame
pygame.init()
win = pygame.display.set_mode((ancho, ancho))
pygame.display.set_caption("Sudoku")
win.fill(color_fondo)
myfont = pygame.font.SysFont('Comic Sans MS', 35)
pygame.display.update()

#clase de boton, es clase porque contiene funciones y no la llamas sino que la creas.
class boton():
    def __init__(self, color, x,y, anchura, altura, text =''):
        self.color = color
        self.x = x
        self.y = y
        self.anchura = anchura
        self.altura = altura
        self.text = text

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.anchura+4, self.altura+4),0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.anchura, self.altura),0)

        if self.text != '':
            text = myfont.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + self.anchura/2 - text.get_width()/2, self.y + (self.altura/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.anchura:
            if pos[1] > self.y and pos[1] < self.y + self.altura:
                return True

        return False     

def insert(win, position,size):
    gsize = int(sqrt(len(grid)))
    # size = 50 (3x3)
    # size = 100 (2x2)
    global incorrectos
    i,j = position[1], position[0]

    if gsize == 3:
        myfont = pygame.font.SysFont('Comic Sans MS', 35)
    else:
        myfont = pygame.font.SysFont('Comic Sans MS', 70)

    if((i != 0 and j != 0) and (i < (gsize**2)+1 and j < (gsize**2)+1)):
        print('ERROR')
        if(grid_original[i-1][j-1] == 0):
            pygame.draw.rect(win, (210, 210, 210), (position[0]*size + buffer, position[1]*size+buffer,size -2*buffer, size - 2*buffer))
            pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if(grid_original[i-1][j-1] != 0):
                        return
                    if(event.key == 48):
                        grid[i-1][j-1] = event.key - 48
                        pygame.draw.rect(win, color_fondo, (position[0]*size + buffer, position[1]*size+buffer,size -2*buffer, size - 2*buffer))
                        pygame.display.update()  

                    if gsize == 3:
                        valor_X = 10
                    else:
                        valor_X = 5
                    if(0 < event.key -48 < valor_X):
                        pygame.draw.rect(win, (210, 210, 210), (position[0]*size + buffer, position[1]*size+buffer,-2*buffer,size - 2*buffer))
                        value = myfont.render(str(event.key-48), True, (0,0,0))
                        
                        for char in grid[i-1]:
                            if char == event.key-48:
                                incorrectos += 1
                                print('incorrecto, numero de intentos:',incorrectos)
                                pygame.draw.rect(win, (255,255,255), (position[0]*size + buffer, position[1]*size+buffer,size - 2*buffer, size - 2*buffer))
                                pygame.display.update()
                                return

                        for char in range(len(grid)):
                            if grid[char][j-1] == event.key-48:
                                incorrectos += 1
                                print('incorrecto, numero de intentos:',incorrectos)
                                pygame.draw.rect(win, (255,255,255), (position[0]*size + buffer, position[1]*size+buffer,size - 2*buffer, size - 2*buffer))
                                pygame.display.update()
                                return
                            
                        if gsize == 3:
                            if (i == 1 and j == 1) or (i == 1 and j == 2) or(i == 1 and j == 3) or(i == 2 and j == 1) or (i == 2 and j == 2) or (i == 2 and j == 3) or (i == 3 and j == 1) or (i == 3 and j == 2) or (i == 3 and j == 3):
                                #print('grid_1')
                                if (event.key-48 == grid[0][0]) or (event.key-48 == grid[0][1]) or (event.key-48 == grid[0][2]) or (event.key-48 == grid[1][0]) or (event.key-48 == grid[1][1]) or (event.key-48 == grid[1][2]) or (event.key-48 == grid[2][0]) or (event.key-48 == grid[2][1]) or (event.key-48 == grid[2][2]):
                                    incorrectos += 1
                                    print('incorrecto, numero de intentos:',incorrectos)
                                    pygame.draw.rect(win, (255,255,255), (position[0]*50 + buffer, position[1]*50+buffer,50 - 2*buffer, 50 - 2*buffer))
                                    pygame.display.update()
                                    return
                            if (i == 1 and j == 4) or (i == 1 and j == 5) or(i == 1 and j == 6) or(i == 2 and j == 4) or (i == 2 and j == 5) or (i == 2 and j == 6) or (i == 3 and j == 4) or (i == 3 and j == 5) or (i == 3 and j == 6):
                                #print('grid_2')
                                if (event.key-48 == grid[0][3]) or (event.key-48 == grid[0][4]) or (event.key-48 == grid[0][5]) or (event.key-48 == grid[1][3]) or (event.key-48 == grid[1][4]) or (event.key-48 == grid[1][5]) or (event.key-48 == grid[2][3]) or (event.key-48 == grid[2][4]) or (event.key-48 == grid[2][5]):
                                    incorrectos += 1
                                    print('incorrecto, numero de intentos:',incorrectos)
                                    pygame.draw.rect(win, (255,255,255), (position[0]*50 + buffer, position[1]*50+buffer,50 - 2*buffer, 50 - 2*buffer))
                                    pygame.display.update()
                                    return
                            if (i == 1 and j == 7) or (i == 1 and j == 8) or(i == 1 and j == 9) or(i == 2 and j == 7) or (i == 2 and j == 8) or (i == 2 and j == 9) or (i == 3 and j == 7) or (i == 3 and j == 8) or (i == 3 and j == 9):
                                #print('grid_3')
                                if (event.key-48 == grid[0][6]) or (event.key-48 == grid[0][7]) or (event.key-48 == grid[0][8]) or (event.key-48 == grid[1][6]) or (event.key-48 == grid[1][7]) or (event.key-48 == grid[1][8]) or (event.key-48 == grid[2][6]) or (event.key-48 == grid[2][7]) or (event.key-48 == grid[2][8]):
                                    incorrectos += 1
                                    print('incorrecto, numero de intentos:',incorrectos)
                                    pygame.draw.rect(win, (255,255,255), (position[0]*50 + buffer, position[1]*50+buffer,50 - 2*buffer, 50 - 2*buffer))
                                    pygame.display.update()
                                    return
                            if (i == 4 and j == 1) or (i == 4 and j == 2) or(i == 4 and j == 3) or(i == 5 and j == 1) or (i == 5 and j == 2) or (i == 5 and j == 3) or (i == 6 and j == 1) or (i == 6 and j == 2) or (i == 6 and j == 3):
                                #print('grid_4')
                                if (event.key-48 == grid[3][0]) or (event.key-48 == grid[3][1]) or (event.key-48 == grid[3][2]) or (event.key-48 == grid[4][0]) or (event.key-48 == grid[4][1]) or (event.key-48 == grid[4][2]) or (event.key-48 == grid[5][0]) or (event.key-48 == grid[5][1]) or (event.key-48 == grid[5][2]):
                                    incorrectos += 1
                                    print('incorrecto, numero de intentos:',incorrectos)
                                    pygame.draw.rect(win, (255,255,255), (position[0]*50 + buffer, position[1]*50+buffer,50 - 2*buffer, 50 - 2*buffer))
                                    pygame.display.update()
                                    return   
                            if (i == 4 and j == 4) or (i == 4 and j == 5) or(i == 4 and j == 6) or(i == 5 and j == 4) or (i == 5 and j == 5) or (i == 5 and j == 6) or (i == 6 and j == 4) or (i == 6 and j == 5) or (i == 6 and j == 6):
                                #print('grid_5')
                                if (event.key-48 == grid[3][3]) or (event.key-48 == grid[3][4]) or (event.key-48 == grid[3][5]) or (event.key-48 == grid[4][3]) or (event.key-48 == grid[4][4]) or (event.key-48 == grid[4][5]) or (event.key-48 == grid[5][3]) or (event.key-48 == grid[5][4]) or (event.key-48 == grid[5][5]):
                                    incorrectos += 1
                                    print('incorrecto, numero de intentos:',incorrectos)
                                    pygame.draw.rect(win, (255,255,255), (position[0]*50 + buffer, position[1]*50+buffer,50 - 2*buffer, 50 - 2*buffer))
                                    pygame.display.update()
                                    return
                            if (i == 4 and j == 7) or (i == 4 and j == 8) or(i == 4 and j == 9) or(i == 5 and j == 7) or (i == 5 and j == 8) or (i == 5 and j == 9) or (i == 6 and j == 7) or (i == 6 and j == 8) or (i == 6 and j == 9):
                                #print('grid_6')
                                if (event.key-48 == grid[3][6]) or (event.key-48 == grid[3][7]) or (event.key-48 == grid[3][8]) or (event.key-48 == grid[4][6]) or (event.key-48 == grid[4][7]) or (event.key-48 == grid[4][8]) or (event.key-48 == grid[5][6]) or (event.key-48 == grid[5][7]) or (event.key-48 == grid[5][8]):
                                    incorrectos += 1
                                    print('incorrecto, numero de intentos:',incorrectos)
                                    pygame.draw.rect(win, (255,255,255), (position[0]*50 + buffer, position[1]*50+buffer,50 - 2*buffer, 50 - 2*buffer))
                                    pygame.display.update()
                                    return    
                            if (i == 7 and j == 1) or (i == 7 and j == 2) or(i == 7 and j == 3) or(i == 8 and j == 1) or (i == 8 and j == 2) or (i == 8 and j == 3) or (i == 9 and j == 1) or (i == 9 and j == 2) or (i == 9 and j == 3):
                                #print('grid_7')
                                if (event.key-48 == grid[6][0]) or (event.key-48 == grid[6][1]) or (event.key-48 == grid[6][2]) or (event.key-48 == grid[7][0]) or (event.key-48 == grid[7][1]) or (event.key-48 == grid[7][2]) or (event.key-48 == grid[8][0]) or (event.key-48 == grid[8][1]) or (event.key-48 == grid[8][2]):
                                    incorrectos += 1
                                    print('incorrecto, numero de intentos:',incorrectos)
                                    pygame.draw.rect(win, (255,255,255), (position[0]*50 + buffer, position[1]*50+buffer,50 - 2*buffer, 50 - 2*buffer))
                                    pygame.display.update()
                                    return    
                            if (i == 7 and j == 4) or (i == 7 and j == 5) or(i == 7 and j == 6) or(i == 8 and j == 4) or (i == 8 and j == 5) or (i == 8 and j == 6) or (i == 9 and j == 4) or (i == 9 and j == 5) or (i == 9 and j == 6):
                                #print('grid_8')
                                if (event.key-48 == grid[6][3]) or (event.key-48 == grid[6][4]) or (event.key-48 == grid[6][5]) or (event.key-48 == grid[7][3]) or (event.key-48 == grid[7][4]) or (event.key-48 == grid[7][5]) or (event.key-48 == grid[8][3]) or (event.key-48 == grid[8][4]) or (event.key-48 == grid[8][5]):
                                    incorrectos += 1
                                    print('incorrecto, numero de intentos:',incorrectos)
                                    pygame.draw.rect(win, (255,255,255), (position[0]*50 + buffer, position[1]*50+buffer,50 - 2*buffer, 50 - 2*buffer))
                                    pygame.display.update()
                                    return    
                            if (i == 7 and j == 7) or (i == 7 and j == 8) or(i == 7 and j == 9) or(i == 8 and j == 7) or (i == 8 and j == 8) or (i == 8 and j == 9) or (i == 9 and j == 7) or (i == 9 and j == 8) or (i == 9 and j == 9):
                                #print('grid_9')
                                if (event.key-48 == grid[6][6]) or (event.key-48 == grid[6][7]) or (event.key-48 == grid[6][8]) or (event.key-48 == grid[7][6]) or (event.key-48 == grid[7][7]) or (event.key-48 == grid[7][8]) or (event.key-48 == grid[8][6]) or (event.key-48 == grid[8][7]) or (event.key-48 == grid[8][8]):
                                    incorrectos += 1
                                    print('incorrecto, numero de intentos:',incorrectos)
                                    pygame.draw.rect(win, (255,255,255), (position[0]*50 + buffer, position[1]*50+buffer,50 - 2*buffer, 50 - 2*buffer))
                                    pygame.display.update()
                                    return                                                
                        else:
                            if (i == 1 and j == 1) or (i == 1 and j == 2) or(i == 2 and j == 1) or(i == 2 and j == 2):
                                #print('grid_1')
                                if (event.key-48 == grid[0][0]) or (event.key-48 == grid[0][1]) or (event.key-48 == grid[1][0]) or (event.key-48 == grid[1][1]):
                                    incorrectos += 1
                                    print('incorrecto, numero de intentos:',incorrectos)
                                    pygame.draw.rect(win, (255,255,255), (position[0]*100 + buffer, position[1]*100+buffer,100 -2*buffer, 100 - 2*buffer))
                                    pygame.display.update()
                                    return
                            if (i == 1 and j == 3) or (i == 1 and j == 4) or(i == 2 and j == 3) or(i == 2 and j == 4):
                                #print('grid_2')
                                if (event.key-48 == grid[0][2]) or (event.key-48 == grid[0][3]) or (event.key-48 == grid[1][2]) or (event.key-48 == grid[1][3]):
                                    incorrectos += 1
                                    print('incorrecto, numero de intentos:',incorrectos)
                                    pygame.draw.rect(win, (255,255,255), (position[0]*100 + buffer, position[1]*100+buffer,100 -2*buffer, 100 - 2*buffer))
                                    pygame.display.update()
                                    return
                            if (i == 3 and j == 0) or (i == 3 and j == 2) or(i == 4 and j == 1) or(i == 4 and j == 2):
                                #print('grid_3')
                                if (event.key-48 == grid[2][0]) or (event.key-48 == grid[2][1]) or (event.key-48 == grid[3][0]) or (event.key-48 == grid[3][1]):
                                    incorrectos += 1
                                    print('incorrecto, numero de intentos:',incorrectos)
                                    pygame.draw.rect(win, (255,255,255), (position[0]*100 + buffer, position[1]*100+buffer,100 -2*buffer, 100 - 2*buffer))
                                    pygame.display.update()
                                    return
                            if (i == 3 and j == 3) or (i == 3 and j == 4) or(i == 4 and j == 3) or(i == 4 and j == 4):      
                                #print('grid_4')
                                if (event.key-48 == grid[2][2]) or (event.key-48 == grid[2][3]) or (event.key-48 == grid[3][2]) or (event.key-48 == grid[3][3]):
                                    incorrectos += 1
                                    print('incorrecto, numero de intentos:',incorrectos)
                                    pygame.draw.rect(win, (255,255,255), (position[0]*100 + buffer, position[1]*100+buffer,100 -2*buffer, 100 - 2*buffer))
                                    pygame.display.update()
                                    return 

                        pygame.draw.rect(win, (255,255,255), (position[0]*size + buffer, position[1]*size+buffer,size - 2*buffer, size - 2*buffer))
                        grid[i-1][j-1] = event.key - 48
                        
                        if gsize == 3:
                            win.blit(value, (position[0]*size + 15, position[1]*size))
                        else:
                            win.blit(value, (position[0]*size + 30, position[1]*size))


                        print('gsize:',gsize)
                        check_win(gsize)
                        pygame.display.update()
                        return
                    return

def check_win(size):
    global juego_ganado
    global horizontal
    global vertical
    h_win = False
    v_win = False
    
    if size == 2:
        numerador = {1,2,3,4}
        horizontal = [0,0,0,0]
        vertical = [0,0,0,0]
    else:
        numerador = {1,2,3,4,5,6,7,8,9}
        horizontal = [0,0,0,0,0,0,0,0,0]
        vertical = [0,0,0,0,0,0,0,0,0]

    for i in range(len(grid)):
        new_set = set()
        for j in range(len(grid)):
            new_set.add(grid[i][j])
            sorted(new_set)
            if new_set == numerador:
                horizontal[i] = 1

    for i in range(len(grid)):
        new_set = set()
        for j in range(len(grid)):
            new_set.add(grid[j][i])
            sorted(new_set)

            if new_set == numerador:
                vertical[i] = 1
    
    if size == 2:
        if horizontal == [1,1,1,1] and vertical == [1,1,1,1]:
            juego_ganado = True
            return
    else:
        if horizontal == [1,1,1,1,1,1,1,1,1] and [1,1,1,1,1,1,1,1,1]:
            juego_ganado = True
            print("GG!")
            return

def clear_screen():
    win.fill((255,255,255))

def main():
    global h_win
    global v_win
    global juego_ganado

    juego_ganado = False
    h_win = False
    v_win = False
    
    clear_screen()
    font = pygame.font.SysFont('Comic Sans MS', 110)
    text = font.render('Sudoku', True, 'black')
    win.blit(text, [90, 100])
    pygame.display.update()

    jugarBotton = boton((76, 138, 245), 150, 300, 250, 75, 'Nuevo Juego')

    jugarBotton.draw(win, (0,0,0))

    exitButton = boton((76, 138, 245), 200, 425, 150, 75, 'Salir')

    exitButton.draw(win, (0,0,0))

    pygame.display.update()

    while True:
        jugarBotton.draw(win, (0,0,0))
        exitButton.draw(win, (0,0,0))
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if jugarBotton.isOver(pos):
                    clear_screen()
                    dificultad()
                if exitButton.isOver(pos):
                    pygame.quit()
                    return

            if event.type == pygame.MOUSEMOTION:
                if jugarBotton.isOver(pos):
                    jugarBotton.color = (209, 230, 255)
                else:
                    jugarBotton.color = (76, 138, 245)

                if exitButton.isOver(pos):
                    exitButton.color = (209, 230, 255)
                else:
                    exitButton.color = (76, 138, 245)

def Name(size, dificultad):
    global name
    global name_txt
    clear_screen()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    name = name_txt
                    print('Name is:',name)
                    clear_screen()
                    tablero(size, dificultad)
                    
                elif event.key == pygame.K_BACKSPACE:
                    name_txt = name_txt[:-1]
                else:
                    name_txt += event.unicode
        win.fill((255,255,255))

        txt = myfont.render('Ingrese su nombre:', True, 'black')
        win.blit(txt,[100,0])
        pygame.draw.rect(win,(0,0,0), input_rect,2)
        text_surface = myfont.render(name_txt,True,(0,0,0))
        win.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)
        pygame.display.flip()
        clock.tick(60)

def dificultad():
    clear_screen()
    ebutton = boton((76, 138, 245), 150, 50, 250, 75, '2x2')
    ebutton.draw(win, (0,0,0))

    hbutton = boton((76, 138, 245), 150, 170, 250, 75, '3x3')
    hbutton.draw(win, (0,0,0))

    pbutton = boton((76, 138, 245), 150, 290, 250, 75, 'Resumir juego')
    pbutton.draw(win, (0,0,0))

    exitButton = boton((76, 138, 245), 175, 410, 200, 75, 'Volver')
    exitButton.draw(win, (0,0,0))
    pygame.display.update()

    while True:
        hbutton.draw(win,(0,0,0))
        ebutton.draw(win,(0,0,0))
        pbutton.draw(win,(0,0,0))
        exitButton.draw(win, (0,0,0))
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if hbutton.isOver(pos):
                    clear_screen()
                    nivel(3)

                if ebutton.isOver(pos):
                    clear_screen()
                    nivel(2)

                if pbutton.isOver(pos):
                    clear_screen()
                    partidas_guardadas()

                if exitButton.isOver(pos):
                    main()
                    pygame.quit()
                    return

            if event.type == pygame.MOUSEMOTION:
                if hbutton.isOver(pos):
                    hbutton.color = (209, 230, 255)
                else:
                    hbutton.color = (76, 138, 245)

                if ebutton.isOver(pos):
                    ebutton.color = (209, 230, 255)
                else:
                    ebutton.color = (76, 138, 245)
                
                if pbutton.isOver(pos):
                    pbutton.color = (209, 230, 255)
                else:
                    pbutton.color = (76, 138, 245)
                    
                if exitButton.isOver(pos):
                    exitButton.color = (209, 230, 255)
                else:
                    exitButton.color = (76, 138, 245)
    return

def nivel(size): #esta es la dificultad, pero en vista a que ya usamos una función llamada dificultad tuvimos que arreglárnosla
    
    clear_screen()
    mbutton = boton((76, 138, 245), 150, 100, 250, 75, 'Medio')
    mbutton.draw(win, (0,0,0))

    ibutton = boton((76, 138, 245), 150, 250, 250, 75, 'Intermedio')
    ibutton.draw(win, (0,0,0))

    aButton = boton((76, 138, 245), 175, 400, 200, 75, 'Avanzado')
    aButton.draw(win, (0,0,0))
    pygame.display.update()

    while True:
        ibutton.draw(win,(0,0,0))
        mbutton.draw(win,(0,0,0))
        aButton.draw(win, (0,0,0))
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mbutton.isOver(pos):
                    clear_screen()
                    Name(size,3)

                if ibutton.isOver(pos):
                    clear_screen()
                    Name(size,5)

                if aButton.isOver(pos):
                    clear_screen()
                    Name(size,7)
                    return

            if event.type == pygame.MOUSEMOTION:
                if ibutton.isOver(pos):
                    ibutton.color = (209, 230, 255)
                else:
                    ibutton.color = (76, 138, 245)

                if mbutton.isOver(pos):
                    mbutton.color = (209, 230, 255)
                else:
                    mbutton.color = (76, 138, 245)
                    
                if aButton.isOver(pos):
                    aButton.color = (209, 230, 255)
                else:
                    aButton.color = (76, 138, 245)
    return

def tablero(size, dificultad):
    global grid
    global incorrectos
    global instanteFinal
    global grid_original
    global instanteInicial

    incorrectos = 0
    
    area = size*size
    # patron para que el tablero sea valido
    def patron(r,c): return (size*(r%size)+r//size+c)%area

    # randomizar columnas numeros y filas para que quede un tablero valido
    from random import sample
    def shuffle(s): return sample(s,len(s)) 
    rBase = range(size) 
    rows  = [ g*size + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*size + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,size*size+1))

    # producir el tablero usando el patron creado arriba
    grid = [ [nums[patron(r,c)] for c in cols] for r in rows ]

    squares = area*area
    empties = squares * dificultad//10
    for p in sample(range(squares),empties):
        grid[p//area][p%area] = 0

    grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

    instanteInicial = datetime.now()
    savebutton = boton((76, 138, 245), 325, 510, 200, 40, 'Guardar')
    savebutton.draw(win,(0,0,0))
    pygame.display.update()

    if size == 3:
        for i in range(0,10):
            if(i%size==0):
                pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i , 500), 4)
                pygame.draw.line(win, (0,0,0), (50, + 50*i + 50), (500, 50 + 50*i), 4)
            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i , 500), 2)
            pygame.draw.line(win, (0,0,0), (50, + 50*i + 50), (500, 50 + 50*i), 2)

        myfont = pygame.font.SysFont('Comic Sans MS', 35)
        for i in range(0, len(grid[0])):
            for j in range(0, len(grid[0])):
                if(0<grid[i][j]<10):
                    value = myfont.render(str(grid[i][j]), True, color_valores_por_defecto)
                    win.blit(value, ((j+1)*50 + 15, (i+1)*50))
    else:
        for i in range(0,10):
            if(i%2==0):
                # (surface, color, start_pos, end_pos, width) -> Rect
                pygame.draw.line(win, (0,0,0), (100 + 100*i, 100), (100 + 100*i , 500), 6)
                pygame.draw.line(win, (0,0,0), (100, + 100*i + 100), (500, 100 + 100*i), 6)
            pygame.draw.line(win, (0,0,0), (100 + 100*i, 100), (100 + 100*i , 500), 3)
            pygame.draw.line(win, (0,0,0), (100, + 100*i + 100), (500, 100 + 100*i), 3)

        myfont = pygame.font.SysFont('Comic Sans MS', 70)
        for i in range(0, len(grid[0])):
            for j in range(0, len(grid[0])):
                if(0<grid[i][j]<10):
                    value = myfont.render(str(grid[i][j]), True, color_valores_por_defecto)
                    win.blit(value, ((j+1)*100 + 30, (i+1)*100))                
    pygame.display.update()
    while True:
        savebutton.draw(win,(0,0,0))
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if savebutton.isOver(pos):
                    guardar(size,dificultad)
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                if size == 3:
                    insert(win, (pos[0]//50, pos[1]//50), 50)
                else:
                    insert(win, (pos[0]//100, pos[1]//100), 100)

            if event.type == pygame.MOUSEMOTION:
                if savebutton.isOver(pos):
                    savebutton.color = (209, 230, 255)
                else:
                    savebutton.color = (76, 138, 245)

            if juego_ganado == True:
                instanteFinal = datetime.now()
                tiempo = instanteFinal - instanteInicial 
                segundos = tiempo.seconds
                puntaje = 10000 - (segundos*(dificultad**-1)) - incorrectos *(100*dificultad)
                round(puntaje)
                if(puntaje < 0):
                    puntaje = 0
                print('puntaje final:', puntaje)

                x = open('highscore.txt','r')
                highscore = x.read()
                print('highscore:',highscore)
                x.close()

                if puntaje > int(highscore):
                    x = open('highscore', 'w')
                    x.write(str(puntaje))
                    x.close()
                main()
                return      

def tablero_guardado(_grid, grid_o, _size, _time, _errors, _dif):
    global grid
    grid = _grid
    global incorrectos
    incorrectos = _errors
    global instanteFinal
    global grid_original
    grid_original = grid_o
    global instanteInicial
    size = _size

    instanteInicial = datetime.now()
    savebutton = boton((76, 138, 245), 325, 510, 200, 40, 'Guardar')
    savebutton.draw(win,(0,0,0))
    pygame.display.update()

    if size == 3:
        for i in range(0,10):
            if(i%size==0):
                pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i , 500), 4)
                pygame.draw.line(win, (0,0,0), (50, + 50*i + 50), (500, 50 + 50*i), 4)
            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i , 500), 2)
            pygame.draw.line(win, (0,0,0), (50, + 50*i + 50), (500, 50 + 50*i), 2)

        myfont = pygame.font.SysFont('Comic Sans MS', 35)
        for i in range(0, len(grid[0])):
            for j in range(0, len(grid[0])):
                if(0<grid[i][j]<10):
                    value = myfont.render(str(grid[i][j]), True, color_valores_por_defecto)
                    win.blit(value, ((j+1)*50 + 15, (i+1)*50))
    else:
        for i in range(0,10):
            if(i%2==0):
                # (surface, color, start_pos, end_pos, width) -> Rect
                pygame.draw.line(win, (0,0,0), (100 + 100*i, 100), (100 + 100*i , 500), 6)
                pygame.draw.line(win, (0,0,0), (100, + 100*i + 100), (500, 100 + 100*i), 6)
            pygame.draw.line(win, (0,0,0), (100 + 100*i, 100), (100 + 100*i , 500), 3)
            pygame.draw.line(win, (0,0,0), (100, + 100*i + 100), (500, 100 + 100*i), 3)

        myfont = pygame.font.SysFont('Comic Sans MS', 70)
        for i in range(0, len(grid[0])):
            for j in range(0, len(grid[0])):
                if(0<grid[i][j]<10):
                    value = myfont.render(str(grid[i][j]), True, color_valores_por_defecto)
                    win.blit(value, ((j+1)*100 + 30, (i+1)*100))                
    pygame.display.update()
    while True:
        savebutton.draw(win,(0,0,0))
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if savebutton.isOver(pos):
                    guardar(size,_dif)
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                if size == 3:
                    insert(win, (pos[0]//50, pos[1]//50), 50)
                else:
                    insert(win, (pos[0]//100, pos[1]//100), 100)

            if event.type == pygame.MOUSEMOTION:
                if savebutton.isOver(pos):
                    savebutton.color = (209, 230, 255)
                else:
                    savebutton.color = (76, 138, 245)

            if juego_ganado == True:
                instanteFinal = datetime.now()
                tiempo = instanteFinal - instanteInicial 
                segundos = tiempo.seconds
                puntaje = 10000-(segundos*2)-incorrectos*100
                if(puntaje < 0):
                    puntaje = 0
                print('puntaje final:', puntaje)

                x = open('highscore.txt','r')
                highscore = x.read()
                print('highscore:',highscore)
                x.close()

                if puntaje > int(highscore):
                    x = open('highscore', 'w')
                    x.write(str(puntaje))
                    x.close()
                main()
                return      

def tiempo_transcurrido(instanteInicial):
    instantefinal = datetime.now()
    transcurrido = instantefinal - instanteInicial
    return transcurrido

def guardar(size, dif):
    f = open('temporal.json','r')
    content = f.read()
    f.close
    #aqui implemento la variable tiempo, la cual almacena el tiempo transcurrido
    tiempo = tiempo_transcurrido(instanteInicial)
    segundos = tiempo.seconds
    
    puntaje = 10000 - (segundos*(dif**-1)) - incorrectos *(100*dif)
    if puntaje <= 0:
        puntaje = 0
    round(puntaje)

    save = {name:{'partida':grid,'grid_original':grid_original,'size':size,'tiempo':56,'errores':incorrectos,'dificultad':dif,'puntaje':puntaje}}
    print(save)
    data = json.dumps(save)
    f = open('temporal.json','w')
    if content != '':
        f.write(content)
        f.write('\n')
    f.write(data)
    f.close
    return 

def partidas_guardadas():
    global name
    global name_txt
    OK = False
    can = True
    p_saved_games = {}
    new_data = []
    max_index = 0
    index = 0
    clear_screen()

    Playbutton = boton((76, 138, 245), 250, 150, 250, 75, 'Jugar')
    Playbutton.draw(win, (0,0,0))

    lbutton = boton('white', 300, 10, 200, 50, 'Tablon')
    lbutton.draw(win, (0,0,0))

    Delbutton = boton((224, 69, 58), 250, 300, 250, 75, 'Eliminar')
    Delbutton.draw(win, (0,0,0))

    ant = boton((255, 255, 255), 50, 450, 200, 50, 'Anterior')
    ant.draw(win, (0,0,0))

    sig = boton((255, 255, 255), 300, 450, 200, 50, 'Siguiente')
    sig.draw(win, (0,0,0))

    pygame.display.update()
    
    while True:
        win.fill((255,255,255))
        Playbutton.draw(win,(0,0,0))
        Delbutton.draw(win,(0,0,0))
        lbutton.draw(win,(0,0,0))
        ant.draw(win,(0,0,0))
        sig.draw(win,(0,0,0))
        font = pygame.font.SysFont('Comic Sans MS', 25)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Playbutton.isOver(pos):
                    if OK == True:
                        clear_screen()
                        tablero_guardado(dc['partida'],dc['grid_original'],dc['size'],dc['tiempo'],dc['errores'],dc['dificultad'])

                if Delbutton.isOver(pos):
                    if OK == True:
                        if p_saved_games != {}:
                            del(p_saved_games[index])

                            for i in p_saved_games:
                                new_data.append(p_saved_games[i])

                            f = open('temporal.json','w')
                            for line in new_data:
                                data = json.dumps(line)
                                f.write(data)
                                f.write('\n')
                                
                            OK == False
                            f.close
                            can = False

                if ant.isOver(pos):
                    if index > 0:
                        index-=1
                        can = True
                        print('index:',index)
                if sig.isOver(pos):
                    if index < max_index:
                        index+=1
                        can = True
                        print('index:',index)
                if lbutton.isOver(pos):
                    clear_screen()
                    leaderboard()
                    return

            if event.type == pygame.MOUSEMOTION:
                if Playbutton.isOver(pos):
                    Playbutton.color = (209, 230, 255)
                else:
                    Playbutton.color = (76, 138, 245)
                if Delbutton.isOver(pos):
                    Delbutton.color = (214, 156, 152)
                else:
                    Delbutton.color = (224, 69, 58)
                if ant.isOver(pos):
                    ant.color = (200,200,200)
                else:
                    ant.color = (255,255,255)
                if sig.isOver(pos):
                    sig.color = (200,200,200)
                else:
                    sig.color = (255,255,255)
                if lbutton.isOver(pos):
                    lbutton.color = (200,200,200)
                else:
                    lbutton.color = (255,255,255)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    index = 0
                    p_saved_games = {}
                    new_data = []
                    name = name_txt
                    can = True
                    
                elif event.key == pygame.K_BACKSPACE:
                    name_txt = name_txt[:-1]
                else:
                    name_txt += event.unicode

        if name != '' and can == True:
            print('Updating data')
            with open('temporal.json') as f:
                new_data = []
                data = [json.loads(line) for line in f]
                i = 0
                for line in data:
                    for key in line.items():
                        if key[0] == name:
                            p_saved_games[i] = line
                            i+=1
                        else:
                            new_data.append(line)
                            
                max_index = len(p_saved_games)-1
                data_dict = {}
                i = 0
                for line in p_saved_games:
                    for key in p_saved_games[line].items():
                        dc = p_saved_games[line][key[0]]
                        data_dict[i] = dc
                    i+=1
            
                font = pygame.font.SysFont('Comic Sans MS', 25)
                if p_saved_games != {}:
                    dc = data_dict[index]
                    _num = font.render(str(index), True, 'black')
                    _tamano = font.render(str(dc['size']), True, 'black')
                    _dificultad = font.render(str(dc['dificultad']), True, 'black')
                    _tiempo = font.render(str(dc['tiempo']), True, 'black')
                    _errores = font.render(str(dc['errores']), True, 'black')
                    _puntaje = font.render(str(dc['puntaje']), True, 'black')
                    OK = True
                can = False
            f.close()
            
        
        num = font.render('Numero:', True, 'black')
        tamano = font.render('Tamano:', True, 'black')
        dificultad = font.render('Dificultad:', True, 'black')
        tiempo = font.render('Tiempo:', True, 'black')
        errores = font.render('Errores:', True, 'black')
        puntaje = font.render('Puntaje:', True, 'black')

        if(OK == True):
            win.blit(_num, [200, 150])
            win.blit(_tamano, [200, 200])
            win.blit(_dificultad, [200, 250])
            win.blit(_tiempo, [200, 300])
            win.blit(_errores, [200, 350])
            win.blit(_puntaje, [200, 400])

        win.blit(num, [50, 150])
        win.blit(tamano, [50, 200])
        win.blit(dificultad, [50, 250])
        win.blit(tiempo, [50, 300])
        win.blit(errores, [50, 350])
        win.blit(puntaje, [50, 400])
        pygame.display.update()

        pygame.draw.rect(win,(0,0,0), input_rect,2)
        text_surface = myfont.render(name_txt,True,(0,0,0))
        win.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)
        pygame.display.flip()
        clock.tick(60)

def leaderboard():
    clear_screen()
    Backbutton = boton((76, 138, 245), 250, 450, 250, 75, 'Atras')
    Backbutton.draw(win, (0,0,0))
    pygame.display.update()
    new_dict = {}

    with open('temporal.json') as f:
        data = [json.loads(line) for line in f]

    for line in data:
        for key in line.items():
            new_dict[key[0]] = {'puntaje':0,'partidas':0}

    for line in data:
        for key in line.items():
            name = key[0]
            dif = line[name]['dificultad']
            segundos = line[name]['tiempo']
            errores = line[name]['errores']
            puntaje = 10000 - (segundos*(dif**-1)) - errores *(100*dif)
            round(puntaje,0)
            #puntaje = puntaje = ((tiempo+dif)*size)
            new_dict[name]['partidas'] += 1
            new_dict[name]['puntaje'] += puntaje

    sorted_dict = sorted(new_dict.items(),key=lambda kv:kv[1]['puntaje'], reverse=True)
    print(sorted_dict)

    x = 0
    for i in range(len(sorted_dict)):
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        strong = str(sorted_dict[i][0]) + ' : ' + str(sorted_dict[i][1])
        txt = myfont.render(strong, True, 'black')
        win.blit(txt,[30, x + 25])
        x+=25
        print(i)

    while True:
        Backbutton.draw(win,(0,0,0))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Backbutton.isOver(pos):
                    clear_screen()
                    partidas_guardadas()

            if event.type == pygame.MOUSEMOTION:
                if Backbutton.isOver(pos):
                    Backbutton.color = (209, 230, 255)
                else:
                    Backbutton.color = (76, 138, 245)
        pygame.display.update()
    return

main()