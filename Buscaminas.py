import random

import pygame

import pygame.font
import os


# funcion para eleccion del nivel de juego:
# modifica el tamaño del tablero, las minas y los puntos por mina

def nivel(level):
    if level == 'F':
        fil = 9
        col = 9
        min = 15
        pun = 25
    elif level == 'N':
        fil = 16
        col = 16
        min = 50
        pun = 50
    elif level == 'D':
        fil = 16
        col = 30
        min = 100
        pun = 100
    return (fil, col, min, pun)


# funcion que define el tamaño del tablero segun el nivel elegido
def tamaño_tablero(a):
    if a == 'F':
        largo = 50
        alto = 50
        margen = 5
        dimensionX = 500
        dimensionY = 500
    elif a == 'N':
        largo = 35
        alto = 35
        margen = 5
        dimensionX = 645
        dimensionY = 645
    elif a == 'D':
        largo = 35
        alto = 35
        margen = 5
        dimensionX = 1205
        dimensionY = 645

    return (largo, alto, margen, dimensionX, dimensionY)


# funcion que crea el tablero de juego
def crea_tablero(filas, columnas, valor):
    tablero = []
    for i in range(filas):
        tablero.append([])
        for j in range(columnas):
            tablero[i].append(valor)
    return tablero


# funcion que muestra el tablero de juego
def muestra_tablero(tablero):
    for fil in tablero:
        for elem in fil:
            print(elem, end=" ")
        print()


# funcion que coloca minas de manera aleatoria en un tablero
def colocar_minas(tablero, minas, filas, columnas):
    minas_tablero = []
    mi = 0
    while mi < minas:
        y = random.randint(0, filas - 1)
        x = random.randint(0, columnas - 1)
        if tablero[y][x] != 9:
            tablero[y][x] = 9
            mi += 1
            minas_tablero.append((y, x))
    return tablero


# funcion que calcula el numero de pistas alrededor de las minas colocadas en el tablero
def pistas(tablero, filas, columnas):
    for y in range(filas):
        for x in range(columnas):
            if tablero[y][x] == 9:
                '''if y < filas-1:
                    if tablero[y + 1][x] != 9:
                        tablero[y + 1][x] += 1
                if y > 0:
                    if tablero[y - 1][x] != 9:
                        tablero[y - 1][x] += 1
                if x > 0:
                    if tablero[y][x-1] != 9:
                        tablero[y][x - 1] += 1
                if x < columnas-1:
                    if tablero[y][x+1] != 9:
                        tablero[y][x+1] +=1'''
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= y + i <= filas - 1 and 0 <= x + j <= columnas - 1:
                            if tablero[y + i][x + j] != 9:
                                tablero[y + i][x + j] += 1
    return tablero


# funcion que elige la imagen de la pista en base a la posicion oprimida por el usuario
def pista_imagen(tablero, y, x):
    if tablero[y][x] == 1:
        img = pygame.image.load("uno.jpg").convert_alpha()
        img = pygame.transform.scale(img, (LARGO, ALTO))
    elif tablero[y][x] == 2:
        img = pygame.image.load("dos.jpg").convert()
        img = pygame.transform.scale(img, (LARGO, ALTO))
    elif tablero[y][x] == 3:
        img = pygame.image.load("tres.jpg").convert()
        img = pygame.transform.scale(img, (LARGO, ALTO))
    elif tablero[y][x] == 4:
        img = pygame.image.load("cuatro.jpg").convert()
        img = pygame.transform.scale(img, (LARGO, ALTO))
    elif tablero[y][x] == 5:
        img = pygame.image.load("cinco.jpg").convert()
        img = pygame.transform.scale(img, (LARGO, ALTO))
    elif tablero[y][x] == 6:
        img = pygame.image.load("seis.jpg").convert()
        img = pygame.transform.scale(img, (LARGO, ALTO))
    elif tablero[y][x] == 7:
        img = pygame.image.load("siete.jpg").convert()
        img = pygame.transform.scale(img, (LARGO, ALTO))
    elif tablero[y][x] == 8:
        img = pygame.image.load("ocho.jpg").convert()
        img = pygame.transform.scale(img, (LARGO, ALTO))
    elif tablero[y][x] == 9:
        img = pygame.image.load("mina.png").convert()
        img = pygame.transform.scale(img, (LARGO, ALTO))
    elif tablero[y][x] == 0:
        img = pygame.image.load("cero.png").convert()
        img = pygame.transform.scale(img, (LARGO, ALTO))
    else:
        img = pygame.image.load("bandera.jpg").convert()
        img = pygame.transform.scale(img, (LARGO, ALTO))
    return img


# define la posicion de las imagenes de pistas
def posicion(fila, columna):
    y = 5 + (fila * (ALTO + MARGEN))
    x = 5 + (columna * (LARGO + MARGEN))
    return (x, y)


# muestra el puntaje en la pantalla
def score(score):
    font = pygame.font.Font(None, 30)
    scoretext = font.render("Score:" + str(score), 1, BLANCO)
    introduccion.blit(scoretext, (50, 10))


puntaje = 0

adios = False
while not adios:  # bucle principal del programa

    os.environ['SDL_VIDEO_WINDOW_POS'] = str(500) + "," + str(200) #inicia la ventana en la posicion 500, 200 de la pantalla
    # Inicia el pygame para la introduccion
    pygame.init()

    # LARGO y ALTO de la pantalla
    DIMENSION_VENTANA = [350, 600]
    introduccion = pygame.display.set_mode(DIMENSION_VENTANA)

    # título de la pantalla.
    pygame.display.set_caption("BUSCAMINAS")

    NEGRO = (0, 0, 0)
    BLANCO = (255, 255, 255)
    ROJO = (255, 0, 0)
    GRIS = (66, 66, 66)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255, 50)
    PURPLE = (255, 0, 255)

    introduccion.fill(NEGRO)

    # se dibujan las imagenes de nivel en la pantalla
    facil = pygame.image.load("facil2.png").convert_alpha()
    normal = pygame.image.load("normal2.png").convert_alpha()
    dificil = pygame.image.load("dificil2.png").convert_alpha()
    exit = pygame.image.load("salir2.png").convert_alpha()
    principal = pygame.image.load("principal buscaminas.png").convert_alpha()
    facil = pygame.transform.scale(facil, (150, 45))
    normal = pygame.transform.scale(normal, (150, 45))
    dificil = pygame.transform.scale(dificil, (150, 45))
    exit = pygame.transform.scale(exit, (150, 45))
    principal = pygame.transform.scale(principal, (330, 300))
    introduccion.blit(facil, (110, 350))
    introduccion.blit(normal, (110, 405))
    introduccion.blit(dificil, (110, 455))
    introduccion.blit(exit, (110, 530))
    introduccion.blit(principal, (10, 30))
    score(puntaje)

    lvl = ""
    salir = False
    while not salir:  # ciclo para eleccion de nivel
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salir = True
                pygame.quit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    # El usuario presiona el ratón. Obtiene su posición.
                    pos = pygame.mouse.get_pos()
                    nx = pos[0]
                    ny = pos[1]

                    if (110 <= nx <= 260) and (350 <= ny < 395):
                        lvl = 'F'
                        salir = True
                    elif (110 <= nx <= 260) and (405 <= ny < 450):
                        lvl = 'N'
                        salir = True
                    elif (110 <= nx <= 260) and (455 <= ny < 495):
                        lvl = 'D'
                        salir = True
                    elif (130 <= nx <= 230) and (530 <= ny < 575):
                        pygame.quit()

        # pygame.draw.rect(introduccion, BLUE, [130, 250, 100, 50], 0)
        # pygame.draw.rect(introduccion, PURPLE, [130, 300, 100, 50], 0)
        # pygame.draw.rect(introduccion, GREEN, [155, 355, 40, 40], 0)

        pygame.display.update()

    filas = nivel(lvl)[0]
    columnas = nivel(lvl)[1]
    minas = nivel(lvl)[2]
    puntos = nivel(lvl)[3]
    descubiertas = 0
    puntaje = 0

    visible = crea_tablero(filas, columnas, "-")  # tablero que ve el usuario
    print(muestra_tablero(visible))

    oculto = crea_tablero(filas, columnas, 0)  # tablero oculto sin minas colocadas, todos los elementos son 0
    print(muestra_tablero(oculto))

    con_minas = colocar_minas(oculto, minas, filas,
                              columnas)  # tablero con las minas colocadas al azar, se le asigna valor 9 a las minas
    print(muestra_tablero(con_minas))

    con_pistas = pistas(con_minas, filas, columnas)  # tablero con minas al azar y ademas con las pistas colocadas
    print(muestra_tablero(con_pistas))

    # se declara el LARGO y ALTO de cada celda de la cuadrícula.
    LARGO = tamaño_tablero(lvl)[0]
    ALTO = tamaño_tablero(lvl)[1]

    # declara el margen entre las celdas.
    MARGEN = tamaño_tablero(lvl)[2]

    # se crea una matriz que almacena las casillas que ha elegido el usuario
    grid = []
    for fila in range(filas):
        grid.append([])
        for columna in range(columnas):
            grid[fila].append('-')


    # Inicia el pygame para el juego nueva pantalla
    pygame.init()

    # LARGO y ALTO de la pantalla
    dimen_venta = [tamaño_tablero(lvl)[3], tamaño_tablero(lvl)[4]]
    pantalla = pygame.display.set_mode(dimen_venta)

    # título de la pantalla.
    pygame.display.set_caption("BUSCAMINAS")

    # flujo de juego hasta que el usuario pulse el botón de salir.
    hecho = False

    # refresco de pantalla
    reloj = pygame.time.Clock()

    # -------- ciclo del juego -----------
    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                hecho = True

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    # El usuario presiona el ratón. Obtiene su posición.
                    pos = pygame.mouse.get_pos()
                    # Cambia las coordenadas x/y de la pantalla por coordenadas en la cuadricula
                    columna = pos[0] // (LARGO + MARGEN)
                    fila = pos[1] // (ALTO + MARGEN)

                    posX = columna
                    posY = fila
                    if con_pistas[posY][posX] == 0:
                        grid[fila][columna] = 0
                    elif con_pistas[posY][posX] == 1:
                        grid[fila][columna] = 1
                    elif con_pistas[posY][posX] == 2:
                        grid[fila][columna] = 2
                    elif con_pistas[posY][posX] == 3:
                        grid[fila][columna] = 3
                    elif con_pistas[posY][posX] == 4:
                        grid[fila][columna] = 4
                    elif con_pistas[posY][posX] == 5:
                        grid[fila][columna] = 5
                    elif con_pistas[posY][posX] == 6:
                        grid[fila][columna] = 6
                    elif con_pistas[posY][posX] == 7:
                        grid[fila][columna] = 7
                    elif con_pistas[posY][posX] == 8:
                        grid[fila][columna] = 8
                    elif con_pistas[posY][posX] == 9:
                        grid[fila][columna] = "mina"
                    # print(grid)

                    if visible[posY][posX] == '-':
                        if con_pistas[posY][posX] == 9:
                            visible[posY][posX] = "@"
                        elif con_pistas[posY][posX] != 0:
                            visible[posY][posX] = oculto[posY][posX]
                        elif con_pistas[posY][posX] == 0:
                            visible[posY][posX] = " "

                    print("Click ", pos, "Coordenadas de la cuadrícula: ", fila, columna)
                    print(muestra_tablero(visible))
                    if visible[posY][posX] == "@":
                        print("Has pisado una Mina\nJuego terminado\nSu puntaje es: ", puntaje)
                        hecho = True


                elif evento.button == 3:
                    # El usuario presiona el ratón. Obtiene su posición.
                    pos = pygame.mouse.get_pos()
                    # Cambia las coordenadas x/y de la pantalla por coordenadas de cuadricula
                    columna = pos[0] // (LARGO + MARGEN)
                    fila = pos[1] // (ALTO + MARGEN)
                    grid[fila][columna] = "bandera"

                    posX = columna
                    posY = fila
                    if visible[posY][posX] == '-':
                        if con_pistas[posY][posX] == 9:
                            descubiertas += 1
                            puntaje = puntos * descubiertas
                            visible[posY][posX] = '☼'
                    # print(grid)

                    print("Click ", pos, "Coordenadas de la cuadrícula: ", fila, columna)
                    print(muestra_tablero(visible))
                    print(descubiertas)
                    if descubiertas == minas:
                        print("Felicidades has ganado\nJuego terminado\nSu puntaje es: ", puntaje)
                        hecho = True

        # fondo de pantalla.
        pantalla.fill(GRIS)

        # Dibuja cuadricula
        for fila in range(filas):
            for columna in range(columnas):
                color = BLANCO
                pygame.draw.rect(pantalla,
                                 color,
                                 [(MARGEN + LARGO) * columna + MARGEN,
                                  (MARGEN + ALTO) * fila + MARGEN,
                                  LARGO, ALTO])

                if grid[fila][columna] == 0:
                    color = GRIS
                    img = pista_imagen(con_pistas, fila, columna)
                    x = posicion(fila, columna)[0]
                    y = posicion(fila, columna)[1]
                    pantalla.blit(img, (x, y))

                elif grid[fila][columna] == 1:
                    # color = VERDE
                    img = pista_imagen(con_pistas, fila, columna)
                    x = posicion(fila, columna)[0]
                    y = posicion(fila, columna)[1]
                    pantalla.blit(img, (x, y))

                elif grid[fila][columna] == 2:
                    # color = ROJO
                    img = pista_imagen(con_pistas, fila, columna)
                    x = posicion(fila, columna)[0]
                    y = posicion(fila, columna)[1]
                    pantalla.blit(img, (x, y))

                elif grid[fila][columna] == 3:
                    img = pista_imagen(con_pistas, fila, columna)
                    x = posicion(fila, columna)[0]
                    y = posicion(fila, columna)[1]
                    pantalla.blit(img, (x, y))

                elif grid[fila][columna] == 4:
                    img = pista_imagen(con_pistas, fila, columna)
                    x = posicion(fila, columna)[0]
                    y = posicion(fila, columna)[1]
                    pantalla.blit(img, (x, y))

                elif grid[fila][columna] == 5:
                    img = pista_imagen(con_pistas, fila, columna)
                    x = posicion(fila, columna)[0]
                    y = posicion(fila, columna)[1]
                    pantalla.blit(img, (x, y))

                elif grid[fila][columna] == 6:
                    img = pista_imagen(con_pistas, fila, columna)
                    x = posicion(fila, columna)[0]
                    y = posicion(fila, columna)[1]
                    pantalla.blit(img, (x, y))

                elif grid[fila][columna] == 7:
                    img = pista_imagen(con_pistas, fila, columna)
                    x = posicion(fila, columna)[0]
                    y = posicion(fila, columna)[1]
                    pantalla.blit(img, (x, y))

                elif grid[fila][columna] == 8:
                    img = pista_imagen(con_pistas, fila, columna)
                    x = posicion(fila, columna)[0]
                    y = posicion(fila, columna)[1]
                    pantalla.blit(img, (x, y))

                elif grid[fila][columna] == "bandera":
                    img = pista_imagen(grid, fila, columna)
                    x = posicion(fila, columna)[0]
                    y = posicion(fila, columna)[1]
                    pantalla.blit(img, (x, y))

                elif grid[fila][columna] == "mina":
                    img = pista_imagen(con_pistas, fila, columna)
                    x = posicion(fila, columna)[0]
                    y = posicion(fila, columna)[1]
                    pantalla.blit(img, (x, y))

        pygame.display.update()
    pygame.quit()