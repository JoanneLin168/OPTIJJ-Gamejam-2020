import pygame
mainClock = pygame.time.Clock()
from pygame.locals import *
import random
import math
pygame.init()
screenWidth = 800
screenHeight = 600
displayWindow = pygame.display.set_mode((screenWidth,screenHeight), 0, 32)
bg = pygame.image.load("assets/puzzleBackground.png")

pygame.display.set_caption("drapdrop")

shape1 = pygame.image.load('assets/Shape1.png')
shape2 = pygame.image.load('assets/Shape2.png')
shape3 = pygame.image.load('assets/Shape3.png')
shape4 = pygame.image.load('assets/Shape4.png')
shape5 = pygame.image.load('assets/Shape5.png')


shapeRect = [shape1.get_rect(),shape2.get_rect(),shape3.get_rect(),shape4.get_rect(),shape5.get_rect()]

shapeX1 = [random.randint(150,500),random.randint(150,500),random.randint(150,500),random.randint(150,500),random.randint(150,500)]
shapeY1 = [random.randint(150,500),random.randint(150,500),random.randint(150,500),random.randint(150,500),random.randint(150,500)]

shapeRect[0].x, shapeRect[0].y = shapeX1[0] , shapeY1[0]
shapeRect[1].x, shapeRect[1].y = shapeX1[1] , shapeY1[1]
shapeRect[2].x, shapeRect[2].y = shapeX1[2] , shapeY1[2]
shapeRect[3].x, shapeRect[3].y = shapeX1[3] , shapeY1[3]
shapeRect[4].x, shapeRect[4].y = shapeX1[4] , shapeY1[4]

correct_PositionsX = [200,300,400,400,300]
correct_PositionsY = [150,150,150,300,300]

def displayImg(shape, x, y):
    displayWindow.blit(shape, (x, y))

def check_result():
    for b in range(0,5):
        if (abs(shapeRect[b].x - correct_PositionsX[b])) <= 10:
            if (abs(shapeRect[b].y - correct_PositionsY[b])) <= 10:
                pass
        else:
            return False
    return True

click = [False,False,False,False,False,False]
global click_Number
click_Number = 0
while True: #game loop

    displayWindow.blit(bg,(0,0))
    #themometerRect1 = pygame.Rect(themometerX1[0], themometerY1[0], themometer1.get_width(), themometer1.get_height())

    mx, my = pygame.mouse.get_pos()


    for event in pygame.event.get():
        if event.type ==  QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = pygame.mouse.get_pos()

                if ((mx > 699) & (my < 150)):
                    if check_result() == True:
                        print("FUCKING DONE WITH THE TASK")
                    else:
                        print("Not quite there")
                for a in range (0,5):
                    if shapeRect[a].collidepoint((mx, my)):
                        click_Number = a
                        click[a] = True
                        break


        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                click[click_Number] = False

    if click[click_Number]:
        mx, my = pygame.mouse.get_pos()
        shapeX1[click_Number] = mx - shapeRect[click_Number].width/2
        shapeY1[click_Number] = my - shapeRect[click_Number].height/2
        shapeRect[click_Number].x, shapeRect[click_Number].y = shapeX1[click_Number] , shapeY1[click_Number]

    displayImg(shape1,shapeX1[0], shapeY1[0])
    displayImg(shape2,shapeX1[1], shapeY1[1])
    displayImg(shape3,shapeX1[2], shapeY1[2])
    displayImg(shape4,shapeX1[3], shapeY1[3])
    displayImg(shape5,shapeX1[4], shapeY1[4])
    pygame.draw.rect(displayWindow,(0,255,0), (700,0,100,50))

    pygame.draw.rect(displayWindow, (0,0,255), (200,150,400,300),7)


    pygame.display.update()
    mainClock.tick(60)
