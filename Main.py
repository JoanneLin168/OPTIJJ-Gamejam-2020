import pygame
import pyganim
import random
import Classes
import Sprite
from pygame import mixer

class Direction():
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

def nextLevel(doorOpen,player):
    doorOpen = False
    print("Next Level")
    player.x = 10
    player.y = 19
    return doorOpen

def gridDisplay(displayWindow):

    black = (0,0,0)
    white = (255,255,255)
    for x in range(0,20):
        for y in range(0,20):
            pygame.draw.rect(displayWindow,white,(((x*40) + 40),((y*40) + 40),40,40)) #Black Border
            pygame.draw.rect(displayWindow,black,(((x*40) + 35),((y*40) + 35),35,35))
    """
    (0,0)------------ (20,0)
        |            |
        |            |
  (0,20) ------------ (20,20)
    """

def showFps(displayWindow, clock):
    fps_overlay = FPS_FONT.render(str(int(clock.get_fps())), True, WHITE)
    displayWindow.blit(fps_overlay, (0, 0))

pygame.init() #Loads the pygame window
screenWidth = 865
screenHeight = 865
displayWindow = pygame.display.set_mode((screenWidth,screenHeight)) #800x800 in size
pygame.display.set_caption("Optijj")
clock = pygame.time.Clock()
FPS = 60
FPS_FONT = pygame.font.SysFont("Arial", 20)
WHITE = pygame.Color("white")
GRID_LENGTH = 40

#TURNED MUSIC OFF TEMPORARILY
#mixer.music.load("assets/music.wav")
#mixer.music.play(-1) # -1 for loop # square

player = Classes.Player(64,64,0,0,100,5,Direction.DOWN)
enemy = Classes.Enemy(64,64,10,10,100,5,Direction.DOWN)
Sprite.initAnim(player, enemy)

doorOpen = False # if next level is available

inputBuffer = 0
inputLag = 7 #game can't accept input for 10 frames

#grid = numpy.zeros((20,20))

# player has been cloned?
# Ideas
# Unique Combat
# can move forward right or left
# cant go back into previous room
#top down
#timer for each room - 60 seconds
#puzzles?
#Combat
#weapons

while True: #When program runs
    displayWindow.fill((255,255,255)) #background is white

    #put main display components
    showFps(displayWindow, clock)
    gridDisplay(displayWindow)
    Sprite.playAnim(displayWindow,player,enemy)

    pygame.display.update() #updates to new display
    for i in pygame.event.get(): # for every event
        if i.type == pygame.QUIT: #if event is to close pygame
            pygame.quit() #close pygame

    keys = pygame.key.get_pressed()

    if inputBuffer == 0:

        if keys[pygame.K_LEFT] and player.x > 0:
            #check if UP and DOWN is being pressed as well
            """if keys[pygame.K_UP] and player.y >= 0:
                player.y -= player.vel
                player.direction = Direction.UP
            elif keys[pygame.K_DOWN] and player.y <= screenHeight:
                player.y += player.vel
                player.direction = Direction.DOWN"""

            #player.x -= player.vel
            player.x -= 1
            player.direction = Direction.LEFT
            player.isWalking = True
            inputBuffer = inputLag

        elif keys[pygame.K_RIGHT] and player.x < 19:
            #check if UP and DOWN is being pressed as well
            """if keys[pygame.K_UP] and player.y >= 0:
                player.y -= player.vel
                player.direction = Direction.UP
            elif keys[pygame.K_DOWN] and player.y <= screenHeight:
                player.y += player.vel
                player.direction = Direction.DOWN"""

            #player.x += player.vel
            player.x += 1
            player.direction = Direction.RIGHT
            player.isWalking = True
            inputBuffer = inputLag

        elif keys[pygame.K_UP] and player.y > 0:
            #player.y -= player.vel
            player.y -= 1
            player.direction = Direction.UP
            player.isWalking = True
            inputBuffer = inputLag

        elif keys[pygame.K_UP] and player.y == 0 and player.x == 10 and doorOpen:
            doorOpen = nextLevel(doorOpen,player)
        #comment out if no moving back
        elif keys[pygame.K_DOWN] and player.y < 19:
            #player.y += player.vel
            player.y += 1
            player.direction = Direction.DOWN
            player.isWalking = True
            #player.health = player.health - 1
            doorOpen = True
            inputBuffer = inputLag

        else:
            player.isWalking = False

    else:
        inputBuffer -= 1

    #print("player x = ",player.x, "player.y = ", player.y,"input buffer = ",inputBuffer)
    clock.tick(FPS) #fps
