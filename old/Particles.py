import pygame
import pyganim

class EntityType():
    PLAYER = 0
    ENEMY_MELEE = 1
    ENEMY_RANGED = 2
    COMPUTER = 3

beamSprites = [(0, 0, 40, 280), (0, 40*1, 40, 280), (0, 40*2, 40, 280), (0, 40*3, 40, 280), (0, 40*4, 40, 280), (0, 40*5, 40, 280), (0, 40*6, 40, 280)]

def makeAnim(entity, i, pathName):
    anim = []
    if entity.type == EntityType.PLAYER:
        images = pyganim.getImagesFromSpriteSheet('assets/'+pathName+'.png', rects=beamSprites)
        frames = list(zip(images, [100] * len(images)))
        animation = pyganim.PygAnimation(frames)
        animation.play()
        anim.append(animation)
    return(anim)

def newAnim(entity, i, pathName):
    anim = makeAnim(entity, i, pathName)
    entity.attackParticles = anim

def initAnim(entities):
    i = 0
    for entity in entities:
        if entity.type == EntityType.PLAYER:
            pathName = "beam1"
        newAnim(entity, i, pathName)
        i += 1
    return (entities)

def shiftedMapX(x, shift):
    x = (x*40) + shift
    return x

def shiftedMapY(y, shift):
    y = (y*40) + shift
    return y

def playAnim(displayWindow, entity):
    entity.attackParticles[0].blit(displayWindow, (entity.x,entity.y))
