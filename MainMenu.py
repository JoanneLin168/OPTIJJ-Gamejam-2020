import pygame
import Classes
import random
from pygame import mixer

pygame.init() #Loads the pygame window
screenWidth800 = 800
screenHeight800 = 800
displayWindow = pygame.display.set_mode((screenWidth800,screenHeight800)) #800x800 in size

clock = pygame.time.Clock()
startingScreen = pygame.image.load('assets/startingScreen.png')
credits = pygame.image.load('assets/credits.png')

mixer.music.load("assets/music.wav")
mixer.music.play(-1) # -1 for loop # square

def startScreen(displayWindow):
    isMenu = True
    isCredits = False
    running = True
    while running: #When program runs
        pygame.display.update() #updates to new display
        for i in pygame.event.get(): # for every event
                if i.type == pygame.QUIT: #if event is to close pygame
                    pygame.quit() #close pygame

        mouseX, mouseY = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            """start (340 to 470, 285 to 320)
            introduction (280 to 560, 360 to 400)
            credits (330 to 500, 445 to 480)"""
            if isMenu:
                if (mouseX >= 340 and mouseX <= 470) and (mouseY >= 285 and mouseY <= 320):
                    running = False
                elif (mouseX >= 280 and mouseX <= 560) and (mouseY >= 360 and mouseY <= 400):
                    print("play tegan intro")
                elif (mouseX >= 330 and mouseX <= 500) and (mouseY >= 445 and mouseY <= 480):
                    isCredits = True
                    isMenu = False
            elif isCredits:
                if (mouseX >= 770 and mouseX <= 840) and (mouseY >= 20 and mouseY <= 90):
                    isCredits = False
                    isMenu = True

        displayWindow.fill((255,255,255)) #background is white
        if isMenu:
            displayWindow.blit(startingScreen, (0,0))
        elif isCredits:
            displayWindow.blit(credits, (0,0))
        #else:

        clock.tick(60) #fps
