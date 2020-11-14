import pygame
import pyganim
import random
import Classes
import Sprite
from pygame import mixer

global levelList
levelList = ["Assets/Tutorial.txt","Assets/Level01.txt","Assets/Level02.txt"]
global levelID
levelID = 0

class Direction():
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

class EntityType():
    PLAYER = 0
    ENEMY = 1

enemies = []
player = Classes.Player(EntityType.PLAYER,64,64,10,19,100,5,Direction.DOWN)
#enemy1 = Classes.Enemy(EntityType.ENEMY,64,64,10,10,100,5,Direction.DOWN)
enemies.append(player)
#enemies.append(enemy1)

#enemy2 = Classes.Enemy(EntityType.ENEMY,64,64,10,0,100,5,Direction.DOWN)
#enemies.append(enemy2)

Sprite.initAnim(enemies)
Sprite.initAnim([player])

def loadLevel(filename):
    array = []
    file = open(filename,"r")
    for line in file:
        lineList = list(line)
        arrayLine = []
        for i in lineList:
            if i != "\n":
                value = int(i)
                arrayLine.append(value)
        array.append(arrayLine)
    file.close()
    return array

def wipeEnemy(): #DUMMY FUNCTION TO REMOVE ENEMIES FROM A LEVEL FOR NOW
    toDelete = []
    for i in enemies:
        if i.type == 1:
            toDelete.append(enemies.index(i))
    modifier = 0
    for i in toDelete:
        enemies.pop((i-modifier))
        modifier += 1


def nextLevel(doorOpen,player):
    global levelID

    doorOpen = False

    wipeEnemy()

    print("Next Level")
    arrayMap = loadLevel(levelList[levelID])
    levelID += 1
    for x in range(0,20):
        for y in range(0,20):
            value = arrayMap[x][y]
            if value == 1:
                #print("Melee Enemy at (",x,",",y,")")
                enemy = Classes.Enemy(EntityType.ENEMY,64,64,x,y,100,5,Direction.DOWN)
                enemies.append(enemy)
                Sprite.initAnim(enemies)
            elif value == 2:
                #print("Range Enemy at (",x,",",y,")")
                pass
            elif value == 3:
                #print("Puzzle Console at (",x,",",y,")")
                pass
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

def floorDisplay(displayWindow):
    floorImage = pygame.image.load('assets/tile.png')
    doorImage = pygame.image.load('assets/door.png')
    openDoor = pygame.image.load('assets/dooro.png')
    black = (0,0,0)
    white = (255,255,255)
    for x in range(0,20):
        for y in range(0,20):
            if y == 0 and x == 10:
                if doorOpen:
                    displayWindow.blit(openDoor,(((x*40)+30),((y*40) + 35)))
                else:
                    displayWindow.blit(doorImage,(((x*40)+30),((y*40) + 35)))
            else:
                displayWindow.blit(floorImage,(((x*40)+30),((y*40) + 35)))
    """
    (0,0)------------ (19,0)
        |            |
        |            |
  (0,19) ------------ (19,19)
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
bg = pygame.image.load('assets/red.png')
while True: #When program runs
    displayWindow.fill((255,255,255)) #background is white
    displayWindow.blit(bg,(0,0))

    #put main display components
    showFps(displayWindow, clock)


    #gridDisplay(displayWindow)
    floorDisplay(displayWindow)

    for enemy in enemies:
        Sprite.playAnim(displayWindow,enemy)
    Sprite.playAnim(displayWindow,player)

    pygame.display.update() #updates to new display
    for i in pygame.event.get(): # for every event
        if i.type == pygame.QUIT: #if event is to close pygame
            pygame.quit() #close pygame

    keys = pygame.key.get_pressed()

    if inputBuffer == 0:
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= 1
            player.direction = Direction.LEFT
            player.isWalking = True
            inputBuffer = inputLag

        elif keys[pygame.K_RIGHT] and player.x < 19:
            player.x += 1
            player.direction = Direction.RIGHT
            player.isWalking = True
            inputBuffer = inputLag

        elif keys[pygame.K_UP] and player.y > 0:
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

        elif keys[pygame.K_z]:
            player.isWalking = False
            player.isAttacking = True

        elif keys[pygame.K_x]:
            player.isWalking = False
            player.isAttacking = False
            player.isDead = True #game should end

        else:
            player.isWalking = False
            player.isAttacking = False
            player.isDead = False

    else:
        inputBuffer -= 1

    #print("player x = ",player.x, "player.y = ", player.y,"input buffer = ",inputBuffer)
    clock.tick(FPS) #fps
