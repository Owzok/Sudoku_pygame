from math import sqrt
import pygame, sys
from datetime import datetime
pygame.init()

ancho = 550
color_fondo = (255, 255, 255)
color_valores_por_defecto = (52, 31, 151)
buffer = 5
juego_ganado = False
name = ''

h_win = False
v_win = False

clock = pygame.time.Clock()
input_rect = pygame.Rect(100,200,200,50)
name_txt = ''

win = pygame.display.set_mode((ancho, ancho))
pygame.display.set_caption("Sudoku")
win.fill(color_fondo)
myfont = pygame.font.SysFont('Comic Sans MS', 35)
pygame.display.update()

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

    if(i != 0 and j != 0):
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

def Name(size):
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
                    tablero(size, 1)
                elif event.key == pygame.K_BACKSPACE:
                    name_txt = name_txt[:-1]
                else:
                    name_txt += event.unicode
                
        win.fill((255,255,255))

        pygame.draw.rect(win,(0,0,0),input_rect,2)
        text_surface = myfont.render(name_txt,True,(0,0,0))
        win.blit(text_surface,(input_rect.x + 5, input_rect.y  + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)

        pygame.display.flip()
        clock.tick(60) 

def dificultad():
    clear_screen()
    ebutton = boton((76, 138, 245), 150, 100, 250, 75, '2x2')
    ebutton.draw(win, (0,0,0))

    hbutton = boton((76, 138, 245), 150, 250, 250, 75, '3x3')
    hbutton.draw(win, (0,0,0))

    exitButton = boton((76, 138, 245), 175, 400, 200, 75, 'Volver')
    exitButton.draw(win, (0,0,0))
    pygame.display.update()

    while True:
        hbutton.draw(win,(0,0,0))
        ebutton.draw(win,(0,0,0))
        exitButton.draw(win, (0,0,0))
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if hbutton.isOver(pos):
                    #print('clicked')
                    Name(3)

                if ebutton.isOver(pos):
                    #print('clicked')
                    Name(2)

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
                    
                if exitButton.isOver(pos):
                    exitButton.color = (209, 230, 255)
                else:
                    exitButton.color = (76, 138, 245)
    return

def tablero(size, dificultad):
    clear_screen()
    global grid
    global incorrectos
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
    #dificultad 7//10
    empties = squares * (dificultad + 5)//10
    for p in sample(range(squares),empties):
        grid[p//area][p%area] = 0

    global grid_original
    global instanteInicial
    
    grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

    instanteInicial = datetime.now()

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                if size == 3:
                    insert(win, (pos[0]//50, pos[1]//50), 50)
                else:
                    insert(win, (pos[0]//100, pos[1]//100), 100)


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

main()