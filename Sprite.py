import pygame
import pyganim

class EntityType():
    PLAYER = 0
    ENEMY = 1

moveSprites = [[(0, 64*8, 64, 64), (64*1, 64*8, 64, 64), (64*2, 64*8, 64, 64), (64*3, 64*8, 64, 64), (64*4, 64*8, 64, 64), (64*5, 64*8, 64, 64), (64*6, 64*8, 64, 64)],
         [(0, 64*9, 64, 64), (64*1, 64*9, 64, 64), (64*2, 64*9, 64, 64), (64*3, 64*9, 64, 64), (64*4, 64*9, 64, 64), (64*5, 64*9, 64, 64), (64*6, 64*9, 64, 64)],
         [(0, 64*10, 64, 64), (64*1, 64*10, 64, 64), (64*2, 64*10, 64, 64), (64*3, 64*10, 64, 64), (64*4, 64*10, 64, 64), (64*5, 64*10, 64, 64), (64*6, 64*10, 64, 64)],
         [(0, 64*11, 64, 64), (64*1, 64*11, 64, 64), (64*2, 64*11, 64, 64), (64*3, 64*11, 64, 64), (64*4, 64*11, 64, 64), (64*5, 64*11, 64, 64), (64*6, 64*11, 64, 64)]]

standSprites = [[(0, 64*8, 64, 64)], [(0, 64*9, 64, 64)], [(0, 64*10, 64, 64)], [(0, 64*11, 64, 64)]]

numOfEntities = 2


moveAnim = []
standAnim = []
animation = [] #[0] = player, [1] = enemy
#animation[x][0] = movAnim, animation[x][1] = standAnim

def makeAnim(entity, i,pathName):
    moveAnim = []
    standAnim = []
    for dir in range(len(moveSprites)):

        moveImages = pyganim.getImagesFromSpriteSheet('assets/'+pathName+'.png', rects=moveSprites[dir])
        moveFrames = list(zip(moveImages, [100] * len(moveImages)))
        moveAnimation = pyganim.PygAnimation(moveFrames)
        moveAnimation.play()
        moveAnim.append(moveAnimation)

        standImages = pyganim.getImagesFromSpriteSheet('assets/'+pathName+'.png', rects=standSprites[dir])
        standFrames = list(zip(standImages, [100] * len(standImages)))
        standAnimation = pyganim.PygAnimation(standFrames)
        standAnimation.play()
        standAnim.append(standAnimation)
    #animation[i].append(moveAnim)
    #animation[i].append(standAnim)
    return([moveAnim,standAnim])

def newAnim(entity, i, pathName):
    anim = makeAnim(entity, i, pathName)
    entity.moveAnim = anim[0]
    entity.standAnim = anim[1]


def initAnim(entities):
    i = 0
    for entity in entities:
        animation.append([])
        if entity.type == EntityType.PLAYER:
            entityName = "player"
            pathName = (entityName)
        elif entity.type == EntityType.ENEMY:
            entityName = "enemy"
            pathName = (entityName)
        else:
            print("Unknown entity")
        #print(pathName)
        newAnim(entity, i, pathName)

        i += 1
    return (entities)

def mapX(x):
    x = (x*40) + 20
    return x

def mapY(y):
    y = (y*40)
    return y

def playAnim(displayWindow, entity):
    if entity.isWalking:
        entity.moveAnim[entity.direction].blit(displayWindow, (mapX(entity.x),mapY(entity.y)))
    else:
        entity.standAnim[entity.direction].blit(displayWindow, (mapX(entity.x),mapY(entity.y)))
