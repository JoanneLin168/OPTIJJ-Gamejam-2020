import pygame
from pygame.locals import *

def main(displayWindow,clock):
    pygame.display.set_caption("puzzle")

    img = pygame.image.load("assets/thermometer1.png")
    title = "Puzzle:"
    instructions1 = "Arrange the thermometers in a pattern to create three equal squares"
    instructions2 =  " You must use the thermometers in a specific order."
    instructions3 = "The top of the thermometer must be pointing upwards or leftwards."

    font = pygame.font.SysFont("freesansbold.ttf", 30)
    def draw_text(text, font, colour, surface, x, y):
        textobj = font.render(text, 1, colour)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

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
            if (abs(a.x - b.x) < 50) and (abs((a.y + a.height) - b.y) < 50):
                return True
        else: # first is horizontal
            if abs(a.x + a.width - b.x) < 50 and (abs(a.y - b.y) < 50):
                return True

        return False

    def checkComplete(thermometerRects):
        first = thermometerRects[0]
        used = []

        for i in range(1, 4): # finds horizontal top left
            if (thermometerRects[i].x - first.x <= 30 ) and (thermometerRects[i].height < first.height):
                first = thermometerRects[i]


        used.append(first) # used 0
        carryOn = False
        if first.height > 50:
            return False
        #first short is top left horizontal
        latest = thermometerRects[0]
        for i in range(0,4):
            if (thermometerRects[i] != first) and not(thermometerRects[i] in used): #checking for second short vertical
                if (abs(first.x - thermometerRects[i].x) < 50) and (abs(first.y - thermometerRects[i].y) < 50) and thermometerRects[i].height > 50:
                    used.append(thermometerRects[i]) # used 1
                    carryOn = True
                    latest = thermometerRects[i]
                    break
        if not(carryOn):
            used.clear()
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
            used.clear()
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
            used.clear()
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
            used.clear()
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
            used.clear()
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
            used.clear()
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
            used.clear()
            return False

        return True


    def resetDetails():
        global thermometerX
        global thermometerY
        global thermometers
        global thermometerRects
        global drag
        global rotate
        global used
        used = []
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


    running = True
    click = False
    while running: #gameloop

        displayWindow.fill((0,0,0))
        draw_text(title, font, (255, 255, 255), displayWindow, 350, 20)
        draw_text(instructions1, font, (255, 255, 255), displayWindow, 100, 60)
        draw_text(instructions2, font, (255, 255, 255), displayWindow, 92, 100)
        draw_text(instructions3, font, (255, 255, 255), displayWindow, 100, 140)

        butX = 865 - 90
        butY = 865 - 140
        reset = pygame.Rect(butX, butY, 200, 40)
        if reset.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(displayWindow, (200, 200, 200), reset) # grey when hover
            if click:
               resetDetails()
        else:
            pygame.draw.rect(displayWindow, (255, 255, 255), reset) # white when not hover
        draw_text('Reset', font, (0,0,0), displayWindow,  butX + 10, butY + 10)

        mx, my = pygame.mouse.get_pos()

        for i in range(0, 8):
            thermometerRects[i] = pygame.Rect(thermometerX[i], thermometerY[i], thermometers[i].get_width(), thermometers[i].get_height())

            rotate[i] = False
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                click = True

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
            running = False


        displayImg(thermometerX, thermometerY)

        pygame.display.update()
        clock.tick(60)
