import pygame
import pyganim
import random
import Classes
import Sprite
import MainMenu
from pygame import mixer
import ParthWorkingPuzzle
import puzzle
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

global levelList
levelList = ["Assets/Tutorial.txt","Assets/Level01.txt","Assets/Level02.txt","Assets/Level03.txt","Assets/Level04.txt","Assets/Level05.txt","Assets/boss.txt"]
global levelID
levelID = 0
global roomAudio
roomAudio = ["Assets/OPTIJJ.wav","Assets/OnceStarted.wav","X","X","X","Assets/DuringPuzzleRoom.wav","Assets/IMRANBossFight.wav","X"]
global aBadlyProgrammedVariable
aBadlyProgrammedVariable = False

class Direction():
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

class EntityType():
    PLAYER = 0
    ENEMY_MELEE = 1
    ENEMY_RANGED = 2
    COMPUTER = 3
    BOSS = 4

enemies = []
turrets = []
turretChecks = []
computers = []
player = Classes.Player(EntityType.PLAYER,64,64,10,19,100,5,Direction.UP)
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
    toDelete = []
    for i in turrets:
        if i.type == 2:
            toDelete.append(turrets.index(i))
    modifier = 0
    for i in toDelete:
        turrets.pop((i-modifier))
        modifier += 1
    toDelete = []
    for i in computers:
        if i.type == 3:
            toDelete.append(computers.index(i))
    modifier = 0
    for i in toDelete:
        computers.pop((i-modifier))
        modifier += 1


def nextLevel(doorOpen,player):
    global levelID
    global aBadlyProgrammedVariable
    global roomAudio


    doorOpen = False

    wipeEnemy()

    #print("Next Level")
    try:

        arrayMap = loadLevel(levelList[levelID])
        levelID += 1
        #print(levelID)
        #print(arrayMap)

        if levelID == 7:
            aBadlyProgrammedVariable = True
            #print("should run")

        if roomAudio[levelID] != "X":
            music = pygame.mixer.music.load(roomAudio[levelID])
            pygame.mixer.music.play()


        for x in range(0,20):
            for y in range(0,20):
                value = arrayMap[x][y]

                if value == 1:
                    #print("Melee Enemy at (",x,",",y,")")
                    enemy = Classes.meleeBot(EntityType.ENEMY_MELEE,64,64,x,y,100,5,Direction.DOWN)
                    enemies.append(enemy)
                elif value == 2:
                    #print("Range Enemy at (",x,",",y,")")
                    turret = Classes.rangeBot(EntityType.ENEMY_RANGED,64,64,x,y,100,5,Direction.DOWN)
                    turrets.append(turret)
                    turretChecks.append(False)
                elif value == 3:
                    #print("Puzzle Console at (",x,",",y,")")
                    computer = Classes.Computer(EntityType.COMPUTER,64,64,x,y,100,5,Direction.DOWN)
                    computers.append(computer)
                    pass
                elif value == 4:
                    wolatile = Classes.meleeBot(EntityType.BOSS,64,64,x,y,100,5,Direction.DOWN)
                    enemies.append(wolatile)

        Sprite.initAnim(enemies)
        Sprite.initAnim(turrets)
        Sprite.initAnim(computers)
        player.x = 10
        player.y = 19
        return 0,doorOpen
    except IndexError:
        print("Thanks")
        #pygame.quit()
        return -1,doorOpen

"""
def saveState(arrayMap):
    file = open("Assets/SaveState.txt","w")
    for i in arrayMap:
        for j in i:
            file.write(str(j))
        file.write("\n")
    file.close()

def recoverState():
    file = open("Assets/Savestate.txt","r")
    arrayMap = []
    for line in file:
        lineArray = list(line)
        arraySlice = []
        for i in range(0,len(lineArray)):
            if i != "\n":
                arraySlice.append(int(lineArray[i]))
        arrayMap.append(arraySlice)
    file.close()
    return arrayMap
"""

def floorDisplay(displayWindow,doorOpen):
    floorImage = pygame.image.load('assets/tile.png')
    closed = pygame.image.load('assets/wallclosed.png')
    open = pygame.image.load('assets/wallopen.png')
    if doorOpen:
        displayWindow.blit(open,(0,0))
    else:
        displayWindow.blit(closed,(0,0))

    for x in range(0,20):
        for y in range(0,20):
            displayWindow.blit(floorImage,(((x*40)+30),((y*40) + 35)))

    """
    (0,0)------------ (19,0)
        |            |
        |            |
  (0,19) ------------ (19,19)
    """

def showFps(displayWindow, clock):
    fps_overlay = FPS_FONT.render('FPS: '+str(int(clock.get_fps())), True, WHITE)
    displayWindow.blit(fps_overlay, (10, 5))

def showDeathAnim():
    deathLag = 20
    while (deathLag != 0):
        deathLag -= 1
        clock.tick(60)

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
inputLag = 7  #game can't accept input for 7 frames
enemyBuffer = 0
enemyLag = 14

status = 0


isMenu = True
isCredits = False
gameOver = False
running = MainMenu.renderMenu(displayWindow,isMenu,isCredits,gameOver,status)

#running = True
if running == True:
    isCredits = False
    isMenu = False

while running: #When program runs


    if aBadlyProgrammedVariable:
        #print("123")
        ParthWorkingPuzzle.main(displayWindow,clock)
        aBadlyProgrammedVariable = False
        puzzle.main(displayWindow,clock)

    isdoorOpen = True
    for i in range(0,len(computers)):

        #print("Pc is " + str(computers[i].x) + " , " + str(computers[i].y))
        if player.x == computers[i].x and player.y == computers[i].y:
            computers[i].unlocked = True
            #print(computers[i].unlocked)
        if computers[i].unlocked == False:
            isdoorOpen = False
    if isdoorOpen:
        doorOpen = True


    displayWindow.fill((255,255,255)) #background is white
    floorDisplay(displayWindow,doorOpen)

    #put main display components
    showFps(displayWindow, clock)

    if enemyBuffer == 0:
        for i in range(1,len(enemies)):  # move first
            enemies[i].moveEnemy(player)
        if int(clock.get_fps()) > 10: # crashed or loading
            enemyBuffer = (enemyLag * (int(clock.get_fps()) * (1/60))) // 1
        else:
            enemyBuffer = enemyLag
    else:
        enemyBuffer -= 1

    if doorOpen == False:
        for i in range(0,len(turrets)):
            if turretChecks[i]:
                shot = turrets[i].shoot(player)
                if shot:
                    turretChecks[i] = False
            turretChecks[i] = turrets[i].checkShoot(player)

    for computer in computers:
        Sprite.playAnim(displayWindow,computer)

    toDelete = []
    for enemy in enemies: # then render
        Sprite.playAnim(displayWindow,enemy)
        if enemy.isDead == True:
            toDelete.append(enemies.index(enemy))
    modi = 0
    for i in toDelete:
        enemies.pop(i-modi)
        modi += 1

    for turret in turrets:
        Sprite.playAnim(displayWindow,turret)

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
            inputBuffer = (inputLag * (int(clock.get_fps()) * (1/60))) // 1

        elif keys[pygame.K_RIGHT] and player.x < 19:
            player.x += 1
            player.direction = Direction.RIGHT
            player.isWalking = True
            inputBuffer = (inputLag * (int(clock.get_fps()) * (1/60))) // 1

        elif keys[pygame.K_UP] and player.y > 0:
            player.y -= 1
            player.direction = Direction.UP
            player.isWalking = True
            inputBuffer = (inputLag * (int(clock.get_fps()) * (1/60))) // 1

        elif keys[pygame.K_UP] and player.y == 0 and player.x == 10 and doorOpen:

            status,doorOpen = nextLevel(doorOpen,player)
        #comment out if no moving back
        #elif keys[pygame.K_DOWN] and player.y < 19:
        #    #player.y += player.vel
        #    player.y += 1
        #    player.direction = Direction.DOWN
        #    player.isWalking = True
            #player.health = player.health - 1

            inputBuffer = inputLag

        else:
            player.isWalking = False
            player.isAttacking = False

        if player.isDead:
            levelID = 0
            gameOver = True
            showDeathAnim()
            running = MainMenu.renderMenu(displayWindow,isMenu,isCredits,gameOver,status)
            player.isDead = False
            gameOVer = False
            player.x = 10
            player.y = 19
            status, doorOpen = nextLevel(doorOpen,player)


    else:
        inputBuffer -= 1

    #print("player x = ",player.x, "player.y = ", player.y,"input buffer = ",inputBuffer)
    clock.tick(FPS) #fps

#for game over, goes back to MainMenu
