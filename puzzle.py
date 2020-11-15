import pygame
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
screenWidth = 900
screenHeight = 600
displayWindow = pygame.display.set_mode((screenWidth,screenHeight), 0, 32)

pygame.display.set_caption("puzzle")

img = pygame.image.load("assets/thermometer1.png")

thermometerX = []
thermometerY = []
thermometers = []
thermometerRects = []
drag = []
rotate = []
for i in range(0, 8):
    if i < 4: # small
        thermometers.append(pygame.transform.scale(img, (img.get_width(), int(img.get_height()/2))))
    else: #big
        thermometers.append(img)

    thermometerRects.append(thermometers[i].get_rect())
    thermometerX.append(50 + 70 * i)
    thermometerY.append(300)
    thermometerRects[i].x = thermometerX[i]
    thermometerRects[i].y = thermometerY[i]
    drag.append(False)
    rotate.append(False)

def displayImg(x, y):
    for i in range(0, 8):
        displayWindow.blit(thermometers[i], (x[i], y[i]))

def overlap(a, b):
    if(a.height > 60): # first is vertical
        if (abs(a.x - b.x) < 40) and (abs((a.y + a.height) - b.y) < 40):
            return True
    else: # first is horizontal
        if abs(a.x + a.width - b.x) < 40 and (abs(a.y - b.y) < 40):
            return True

    return False

def checkComplete(thermometerRects):
    first = thermometerRects[0]
    used = []

    for i in range(1, 4): # finds horizontal top left
        if (thermometerRects[i].x - first.x <= 40 ) and (thermometerRects[i].height < first.height):
            first = thermometerRects[i]

    used.append(first) # used 0
    carryOn = False
    if first.height > 50:
        return False
    #first short is top left horizontal
    latest = thermometerRects[0]
    for i in range(0,4):
        if (thermometerRects[i] != first) and not(thermometerRects[i] in used): #checking for second short vertical
            if (abs(first.x - thermometerRects[i].x) < 40) and (abs(first.y - thermometerRects[i].y) < 40) and thermometerRects[i].height > 50:
                used.append(thermometerRects[i]) # used 1
                carryOn = True
                latest = thermometerRects[i]
                break
    if not(carryOn):
        return False

    carryOn = False

    #first long horizontal which is stored in used 2
    if(overlap(used[1], thermometerRects[4]) and thermometerRects[4].height < 50):
        used.append(thermometerRects[4])
        carryOn = True
    elif(overlap(used[1], thermometerRects[5]) and thermometerRects[5].height < 50):
        used.append(thermometerRects[5])
        carryOn = True
    elif(overlap(used[1], thermometerRects[6]) and thermometerRects[6].height < 50):
        used.append(thermometerRects[6])
        carryOn = True
    elif(overlap(used[1], thermometerRects[7]) and thermometerRects[7].height < 50):
        used.append(thermometerRects[7])
        carryOn = True
    if not(carryOn):
        return False

    carryOn = False

    # second long vertical which is stored in used 3
    if not(thermometerRects[4] in used):
        if(overlap(used[0], thermometerRects[4]) and thermometerRects[4].height > 50):
            used.append(thermometerRects[4])
            carryOn = True
    elif not(thermometerRects[5] in used):
        if(overlap(used[0], thermometerRects[5]) and thermometerRects[5].height > 50):
            used.append(thermometerRects[5])
            carryOn = True
    elif not(thermometerRects[6] in used):
        if(overlap(used[0], thermometerRects[6]) and thermometerRects[6].height > 50):
            used.append(thermometerRects[6])
            carryOn = True
    elif not(thermometerRects[7] in used):
        if(overlap(used[0], thermometerRects[7]) and thermometerRects[7].height > 50):
            used.append(thermometerRects[7])
            carryOn = True
    if not(carryOn):
        return False

    carryOn = False

    #third long horizontal which is stored in used 4
    if not(thermometerRects[4] in used):
        if(overlap(used[3], thermometerRects[4]) and thermometerRects[4].height < 50):
            used.append(thermometerRects[4])
            carryOn = True
    elif not(thermometerRects[5] in used):
        if(overlap(used[3], thermometerRects[5]) and thermometerRects[5].height < 50):
            used.append(thermometerRects[5])
            carryOn = True
    elif not(thermometerRects[6] in used):
        if(overlap(used[3], thermometerRects[6]) and thermometerRects[6].height < 50):
            used.append(thermometerRects[6])
            carryOn = True
    elif not(thermometerRects[7] in used):
        if(overlap(used[3], thermometerRects[7]) and thermometerRects[7].height < 50):
            used.append(thermometerRects[7])
            carryOn = True
    if not(carryOn):
        return False

    carryOn = False

    #fourth long vertical which is stored in used 5
    if not(thermometerRects[4] in used):
        if(overlap(used[2], thermometerRects[4]) and thermometerRects[4].height > 50):
            used.append(thermometerRects[4])
            carryOn = True
    elif not(thermometerRects[5] in used):
        if(overlap(used[2], thermometerRects[5]) and thermometerRects[5].height > 50):
            used.append(thermometerRects[5])
            carryOn = True
    elif not(thermometerRects[6] in used):
        if(overlap(used[2], thermometerRects[6]) and thermometerRects[6].height > 50):
            used.append(thermometerRects[6])
            carryOn = True
    elif not(thermometerRects[7] in used):
        if(overlap(used[2], thermometerRects[7]) and thermometerRects[7].height > 50):
            used.append(thermometerRects[7])
            carryOn = True
    if not(carryOn):
        return False

    carryOn = False
    # third short horizontal and store in used 6
    if not(thermometerRects[0] in used):
        if(overlap(used[5], thermometerRects[0]) and thermometerRects[0].height < 50):
            used.append(thermometerRects[0])
            carryOn = True
    elif not(thermometerRects[1] in used):
        if(overlap(used[5], thermometerRects[1]) and thermometerRects[1].height < 50):
            used.append(thermometerRects[1])
            carryOn = True
    elif not(thermometerRects[2] in used):
        if(overlap(used[5], thermometerRects[2]) and thermometerRects[2].height < 50):
            used.append(thermometerRects[2])
            carryOn = True
    elif not(thermometerRects[3] in used):
        if(overlap(used[5], thermometerRects[3]) and thermometerRects[3].height < 50):
            used.append(thermometerRects[3])
            carryOn = True
    if not(carryOn):
        return False

    carryOn = False

    # fourth short vertical and store in used 7
    if not(thermometerRects[0] in used):
        if(overlap(used[4], thermometerRects[0]) and thermometerRects[0].height > 50):
            used.append(thermometerRects[0])
            carryOn = True
    elif not(thermometerRects[1] in used):
        if(overlap(used[4], thermometerRects[1]) and thermometerRects[1].height > 50):
            used.append(thermometerRects[1])
            carryOn = True
    elif not(thermometerRects[2] in used):
        if(overlap(used[4], thermometerRects[2]) and thermometerRects[2].height > 50):
            used.append(thermometerRects[2])
            carryOn = True
    elif not(thermometerRects[3] in used):
        if(overlap(used[4], thermometerRects[3]) and thermometerRects[3].height > 50):
            used.append(thermometerRects[3])
            carryOn = True

    if not(carryOn):
        return False

    return True


running = True
while running: #gameloop

    displayWindow.fill((0,0,0))
    mx, my = pygame.mouse.get_pos()

    for i in range(0, 8):
        thermometerRects[i] = pygame.Rect(thermometerX[i], thermometerY[i], thermometers[i].get_width(), thermometers[i].get_height())

        rotate[i] = False
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:


            if event.button == 1:
                mx, my = pygame.mouse.get_pos()
                for i in range(0,8):
                    if thermometerRects[i].collidepoint((mx, my)):
                        drag[i] = True
            if event.button == 3:
                for i in range(0,8):
                    mx, my = pygame.mouse.get_pos()
                    if thermometerRects[i].collidepoint((mx, my)):
                        rotate[i] = True

        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                for i in range(0,8):
                    drag[i] = False

    for i in range(0,8):
        if drag[i]:
            mx, my = pygame.mouse.get_pos()
            thermometerRects[i].x = mx - thermometerRects[i].width/2
            thermometerRects[i].y = my - thermometerRects[i].height/2
            thermometerX[i] = thermometerRects[i].x
            thermometerY[i] = thermometerRects[i].y

        if rotate[i]:
            cpyX = thermometerX[i] + (thermometers[i].get_width() - thermometers[i].get_height())/2
            cpyY = thermometerY[i] + (thermometers[i].get_height() - thermometers[i].get_width())/2
            cpyWidth = thermometers[i].get_height()
            cpyHeight = thermometers[i].get_width()
            thermometerCpy = pygame.transform.rotate(thermometers[i], 90)
            thermometerCpyRect = pygame.Rect(cpyX, cpyY, cpyWidth, cpyHeight)
            thermometers[i] = thermometerCpy
            thermometerRects[i] = thermometerCpyRect



    if checkComplete(thermometerRects):
        print("complete")


    displayImg(thermometerX, thermometerY)

    pygame.display.update()
    mainClock.tick(60)


pygame.quit()
