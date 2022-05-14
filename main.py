# 0.5/0.1  et 100 %
# x c'est 0.1 * 100
# 2% et apres on multiplie case = 64 par 2%

# il me manque l'appel de mes fonction de maniere a ce que ce soit récursif

# sokoman ahahah a+
from cmath import rect
from ctypes.wintypes import RECT, RGB
from turtle import Screen, position
import pygame
import const
from datetime import datetime, timedelta
# from datetime import timedelta


# sql

# import mysql.connector as mysql

# bdd = mysql.connect(user="root", password="",
#                     host='localhost', database="sokoban")


# def insertAndShow(pseudo, timer):

#     cursor = bdd.cursor()

#     query = "INSERT INTO score (pseudo,timer) VALUES (%s,%s)"
#     cursor.execute(query, (pseudo, timer))
#     # sql
#     query = "SELECT * FROM score ORDER BY timer ASC"
#     cursor.execute(query)
#     result = cursor.fetchall()

#     cursor.close()
#     bdd.close()

#     return result


def checkWalls(direction):
    bool = True

    if direction == 'haut':
        wall = position_perso.top - moyenneY
        wall2 = position_perso.left

        # print(len(walls))
        for case in walls:

            if case[1] == wall and case[0] == wall2:
                bool = False

    if direction == 'bas':
        # position = position_perso.top
        wall = position_perso.top + moyenneY
        wall2 = position_perso.left
        for case in walls:
            # print('zlaaaaaaa')
            # print(case)
            # print(case[1])
            # print(case[0])
            # print(wall)
            # print(wall2)
            # print(position_perso)
            if case[1] == wall and case[0] == wall2:
                bool = False

    if direction == 'gauche':
        wall2 = position_perso.top
        # position = position_perso.left
        wall = position_perso.left - moyenneX
        for case in walls:
            if case[0] == wall and case[1] == wall2:
                bool = False

    if direction == 'droite':
        # position = position_perso.left
        wall = position_perso.left + moyenneX
        wall2 = position_perso.top

        for case in walls:
            if case[0] == wall and case[1] == wall2:
                bool = False

    # for case in walls:
    #     print(case, (wall))
    #     if case == position - wall:
    #         bool = False
    # print("bool")
    # print(bool)
    # print("bool")
    return bool


level = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

goal = []
victory = []
walls = []  # ugh

height = 1024
width = 1024

i = 0
for row in level:
    for case in row:
        i += 1
    break

moyenneY = height/len(level)
moyenneX = width/i


pygame.init()
fenetre = pygame.display.set_mode((height, width), pygame.FULLSCREEN)
behelit = pygame.image.load("behelit.png").convert_alpha()
behelit = pygame.transform.scale(behelit, (moyenneX, moyenneY))

espace_vide = pygame.image.load("espace_vide.jpg").convert()
espace_vide = pygame.transform.scale(espace_vide, (moyenneX, moyenneY))

mur = pygame.image.load("mur.png").convert()
mur = pygame.transform.scale(mur, (moyenneX, moyenneY))

perso = pygame.image.load("perso-looking-right.png").convert_alpha()
perso = pygame.transform.scale(perso, (moyenneX, moyenneY))

# Spells
getsuga = pygame.image.load("getsuga.png").convert_alpha()
getsuga = pygame.transform.scale(getsuga, (moyenneX, moyenneY))

explosion1 = pygame.image.load("explosion1.png").convert_alpha()
explosion1 = pygame.transform.scale(explosion1, (moyenneX, moyenneY))

explosion2 = pygame.image.load("explosion2.png").convert_alpha()
explosion2 = pygame.transform.scale(explosion2, (moyenneX, moyenneY))

explosion3 = pygame.image.load("explosion3.png").convert_alpha()
explosion3 = pygame.transform.scale(explosion3, (moyenneX, moyenneY))

explosion4 = pygame.image.load("explosion4.png").convert_alpha()
explosion4 = pygame.transform.scale(explosion4, (moyenneX, moyenneY))


# Si vous souhaitez utiliser une image sans transparence, mais rendre la couleur de fond transparente,
#  vous pouvez utiliser cette la méthode de Surface set_colorkey(),
#   qui prend en paramètre une valeur RGB (Red, Green, Blue), dont les valeurs vont de 0 à 255 :
x = 0
y = 0
for ligne in level:
    for case in ligne:
        if(case == 0):
            fenetre.blit(espace_vide, (x, y))

        elif(case == 1):
            fenetre.blit(mur, (x, y))
            walls.append([int(x), int(y), int(moyenneX), int(moyenneY)])

        elif(case == 6):
            fenetre.blit(espace_vide, (x, y))
            fenetre.blit(behelit, (x, y))
            goal.append([int(x), int(y), int(moyenneX), int(moyenneY)])
            print(goal)

        x += moyenneX
    x = 0
    y += moyenneY
    pygame.display.flip()

# Rafraîchissement de l'écran
pygame.display.flip()


position_perso = perso.get_rect()
position_perso.top = height/2  # position de départ
position_perso.left = width/2  # position de départ
fenetre.blit(perso, position_perso)
pygame.display.flip()


# txt

pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)

text_surface = my_font.render('Relax, enjoy death :)', False, (0, 0, 0))


# txt

# animation rate
# def animationRate(delay):

# current_time

# Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1
# Boucle infinie de jeu
temp = 0  # servira a se souvenir du dernier déplacement
shock_wave_animation = False
startingDate = datetime.now()
while continuer:
    if(shock_wave_animation):
        # print('endDate')
        # print(startingDate)
        # print(endDate)
        # print('endDate')

        start = position_perso.left + (moyenneX/2)
        # start = position_perso.left + moyenneX
        end = position_perso.left + (moyenneX*3)
        delay = 0.5
        case = moyenneX
        total_case = 3
        position_getsuga = position_perso.left + moyenneX

        current_step = 0

        # while(position_getsuga <= end):
        current_date = datetime.now()
        delay_requis = (endDate - start_date).microseconds / \
            1000  # conversion en millisecondes
        # while(case <= 3):
        delay_parcouru = 0
        # delay_requis = datetime.now(timedelta(milliseconds=500))
        # current_step = start

        while(timedelta(milliseconds=datetime.now().microsecond) <= timedelta(milliseconds=endDate.microsecond)):
            # fenetre.blit(
            #     espace_vide, (position_perso.left + moyenneX, position_perso.top))
            # if(timedelta(milliseconds=datetime.now().microsecond) >= timedelta(milliseconds=endDate.microsecond)):
            if delay_parcouru >= (delay_requis - 5):
                shock_wave_animation = False
                print("shock_wave_animation = False")
                # quit()
            # current_step = current_step + step

            delay_parcouru = (datetime.now() - start_date).microseconds/1000

            pourcentage = (delay_parcouru * 100)/delay_requis
            print(pourcentage)
            pourcentage = pourcentage/100
            loop_step = case * pourcentage

            # print("coef_date")
            # print(coef_date)

            # coef_date = (current_date / endDate)
            print("loop_step")
            print(pourcentage)
            print(delay_parcouru)
            print(delay_requis)
            print(loop_step)
            current_step = start + loop_step
            print('position_getsuga')
            print(position_getsuga)
            print(timedelta(milliseconds=endDate.microsecond))
            print(timedelta(milliseconds=datetime.now().microsecond))
            # if delay_parcouru <= delay_requis:

            position_getsuga = fenetre.blit(
                getsuga, (current_step, position_perso.top))

            # if((current_date) % (endDate/delay) == 0):
            # if()

            # case = case + 1

        # print(now)

        # fulldate = datetime.datetime.strptime(date + ' ' + time, "%Y-%m-%d %H:%M:%S.%f")

        # print(now, fulldate)  # :)

        # la date suivante - la date de base + le coefficient pour
        # savoir si on l'a dépassé et si on blit pas une autre img

    for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
        if event.type == pygame.KEYDOWN:  # Si un de ces événements est de type QUIT
            print(event.type)
            if event.key == pygame.K_c:  # la touche c
                shock_wave_animation = True
                start_date = datetime.now()  # param
                endDate = start_date + timedelta(milliseconds=2500)  # param

                print('BAAAAAAAAAAAAAAAS')

                if temp == 'droite':
                    print('BAAAAAAAAAAAAAAAS ENABLED')
                    getsuga.get_rect()
                    position_getsuga = fenetre.blit(getsuga, (position_perso.left +
                                                              moyenneX, position_perso.top))
                    position_getsuga = position_perso.move(
                        moyenneX + moyenneX, moyenneY)

                    position_getsuga = position_perso.move(
                        moyenneX + moyenneX + moyenneX, moyenneY)

                    position_getsuga = position_perso.move(
                        moyenneX + moyenneX + moyenneX + moyenneX, moyenneY)
                # elif temp == 'haut':

                # elif temp == 'gauche':

                # elif temp == 'droite':

            for item in goal:
                if len(victory) == len(goal):
                    fenetre.blit(text_surface, (height/2, width/2))
                if item == position_perso:
                    bool = True
                    for compareGoal in goal:
                        for compareVictory in victory:
                            if position_perso == compareVictory:
                                bool = False
                    if bool:
                        victory.append(item)

            if event.key == pygame.K_ESCAPE:
                continuer = 0  # On arrête la boucle
            elif event.key == pygame.K_DOWN:  # Si "flèche bas"
                couscous = checkWalls('bas')
                # print(couscous)

                if couscous:
                    print('passé dedans')
                    # if position_perso.top < height - (moyenneY*2):
                    position_perso = position_perso.move(0, moyenneY)
                    fenetre.blit(espace_vide, (position_perso.left,
                                               position_perso.top - moyenneY))
                    temp = 'bas'
            elif event.key == pygame.K_UP:  # Si "flèche du haut"
                # if position_perso.top > moyenneY:
                couscous = checkWalls('haut')
                if couscous:
                    print('passé dedans')
                    position_perso = position_perso.move(0, -moyenneY)
                    fenetre.blit(espace_vide, (position_perso.left,
                                               position_perso.top + moyenneY))
                    temp = 'haut'

            elif event.key == pygame.K_LEFT:  # Si "flèche left"
                # if position_perso.left > moyenneX:

                couscous = checkWalls('gauche')
                if couscous:
                    print('passé dedans')
                    position_perso = position_perso.move(-moyenneX, 0)
                    fenetre.blit(espace_vide, (position_perso.left +
                                               moyenneX, position_perso.top))
                    temp = 'gauche'

            elif event.key == pygame.K_RIGHT:  # Si "flèche right"
                # if position_perso.left < width - (moyenneX*2):
                couscous = checkWalls('droite')
                if couscous:
                    print('passé dedans')
                    position_perso = position_perso.move(moyenneX, 0)
                    fenetre.blit(
                        espace_vide, (position_perso.left - moyenneX, position_perso.top))
                    temp = 'droite'

        fenetre.blit(perso, position_perso)
        print(position_perso)
        # Rafraichissement
        pygame.display.update()  # and show it all
        pygame.display.flip()
