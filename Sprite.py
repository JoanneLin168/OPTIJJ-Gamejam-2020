import pygame
import pyganim

class EntityType():
    PLAYER = 0
    ENEMY_MELEE = 1
    ENEMY_RANGED = 2
    COMPUTER = 3

moveSprites = [
[(0, 64*8, 64, 64), (64*1, 64*8, 64, 64), (64*2, 64*8, 64, 64), (64*3, 64*8, 64, 64), (64*4, 64*8, 64, 64), (64*5, 64*8, 64, 64), (64*6, 64*8, 64, 64)],
[(0, 64*9, 64, 64), (64*1, 64*9, 64, 64), (64*2, 64*9, 64, 64), (64*3, 64*9, 64, 64), (64*4, 64*9, 64, 64), (64*5, 64*9, 64, 64), (64*6, 64*9, 64, 64)],
[(0, 64*10, 64, 64), (64*1, 64*10, 64, 64), (64*2, 64*10, 64, 64), (64*3, 64*10, 64, 64), (64*4, 64*10, 64, 64), (64*5, 64*10, 64, 64), (64*6, 64*10, 64, 64)],
[(0, 64*11, 64, 64), (64*1, 64*11, 64, 64), (64*2, 64*11, 64, 64), (64*3, 64*11, 64, 64), (64*4, 64*11, 64, 64), (64*5, 64*11, 64, 64), (64*6, 64*11, 64, 64)]]

standSprites = [[(0, 64*8, 64, 64)], [(0, 64*9, 64, 64)], [(0, 64*10, 64, 64)], [(0, 64*11, 64, 64)]]

playerAttackSprites = [
[(0, 64*4, 64, 64), (64*1, 64*4, 64, 64), (64*2, 64*4, 64, 64), (64*3, 64*4, 64, 64), (64*4, 64*4, 64, 64), (64*5, 64*4, 64, 64), (64*6, 64*4, 64, 64), (64*7, 64*4, 64, 64)],
[(0, 64*5, 64, 64), (64*1, 64*5, 64, 64), (64*2, 64*5, 64, 64), (64*3, 64*5, 64, 64), (64*4, 64*5, 64, 64), (64*5, 64*5, 64, 64), (64*6, 64*5, 64, 64), (64*7, 64*5, 64, 64)],
[(0, 64*6, 64, 64), (64*1, 64*6, 64, 64), (64*2, 64*6, 64, 64), (64*3, 64*6, 64, 64), (64*4, 64*6, 64, 64), (64*5, 64*6, 64, 64), (64*6, 64*6, 64, 64), (64*7, 64*5, 64, 64)],
[(0, 64*7, 64, 64), (64*1, 64*7, 64, 64), (64*2, 64*7, 64, 64), (64*3, 64*7, 64, 64), (64*4, 64*7, 64, 64), (64*5, 64*7, 64, 64), (64*6, 64*7, 64, 64), (64*7, 64*5, 64, 64)]]

meleeAttackSprites = [
[(0, 64*12, 64, 64), (64*1, 64*12, 64, 64), (64*2, 64*12, 64, 64), (64*3, 64*12, 64, 64), (64*4, 64*12, 64, 64), (64*5, 64*12, 64, 64), (64*6, 64*12, 64, 64)],
[(0, 64*13, 64, 64), (64*1, 64*13, 64, 64), (64*2, 64*13, 64, 64), (64*3, 64*13, 64, 64), (64*4, 64*13, 64, 64), (64*5, 64*13, 64, 64), (64*6, 64*13, 64, 64)],
[(0, 64*14, 64, 64), (64*1, 64*14, 64, 64), (64*2, 64*14, 64, 64), (64*3, 64*14, 64, 64), (64*4, 64*14, 64, 64), (64*5, 64*14, 64, 64), (64*6, 64*14, 64, 64)],
[(0, 64*15, 64, 64), (64*1, 64*15, 64, 64), (64*2, 64*15, 64, 64), (64*3, 64*15, 64, 64), (64*4, 64*15, 64, 64), (64*5, 64*15, 64, 64), (64*6, 64*15, 64, 64)]]

rangedSprites = [[(0, 0, 64, 64)]]

deathSprites = [[(0, 64*20, 64, 64), (64*1, 64*20, 64, 64), (64*2, 64*20, 64, 64), (64*3, 64*20, 64, 64), (64*4, 64*20, 64, 64), (64*5, 64*20, 64, 64)]]

def makeAnim(entity, i, pathName):
    moveAnim = []
    standAnim = []
    attackAnim = []
    deathAnim = []

    if entity.type == EntityType.ENEMY_RANGED:
        anim = []
        images = pyganim.getImagesFromSpriteSheet('assets/'+pathName+'.png', rects=rangedSprites[0])
        frames = list(zip(images, [100] * len(images)))
        animation = pyganim.PygAnimation(frames)
        animation.play()
        anim.append(animation)
        moveAnim = anim
        standAnim = anim
        attackAnim = anim
        deathAnim = anim

    else:
        for dir in range(len(moveSprites)):
            moveImages = pyganim.getImagesFromSpriteSheet('assets/'+pathName+'.png', rects=moveSprites[dir])
            moveFrames = list(zip(moveImages, [100] * len(moveImages)))
            moveAnimation = pyganim.PygAnimation(moveFrames)
            moveAnimation.play()
            moveAnim.append(moveAnimation)

        for dir in range(len(standSprites)):
            standImages = pyganim.getImagesFromSpriteSheet('assets/'+pathName+'.png', rects=standSprites[dir])
            standFrames = list(zip(standImages, [100] * len(standImages)))
            standAnimation = pyganim.PygAnimation(standFrames)
            standAnimation.play()
            standAnim.append(standAnimation)

        if entity.type == EntityType.PLAYER:
            attackSprites = playerAttackSprites
        elif entity.type == EntityType.ENEMY_MELEE:
            attackSprites = meleeAttackSprites
        elif entity.type == EntityType.ENEMY_RANGED:
            attackSprites = rangedAttackSprites

        for dir in range(len(attackSprites)):
            attackImages = pyganim.getImagesFromSpriteSheet('assets/'+pathName+'.png', rects=attackSprites[dir])
            attackFrames = list(zip(attackImages, [100] * len(attackImages)))
            attackAnimation = pyganim.PygAnimation(attackFrames)
            attackAnimation.play()
            attackAnim.append(attackAnimation)

        for dir in range(len(deathSprites)):
            deathImages = pyganim.getImagesFromSpriteSheet('assets/'+pathName+'.png', rects=deathSprites[dir])
            deathFrames = list(zip(deathImages, [100] * len(deathImages)))
            deathAnimation = pyganim.PygAnimation(deathFrames)
            deathAnimation.play()
            deathAnim.append(deathAnimation)

    return([moveAnim, standAnim, attackAnim, deathAnim])

def newAnim(entity, i, pathName):
    anim = makeAnim(entity, i, pathName)
    entity.moveAnim = anim[0]
    entity.standAnim = anim[1]
    entity.attackAnim = anim[2]
    entity.deathAnim = anim[3]

def initAnim(entities):
    i = 0
    for entity in entities:
        if entity.type == EntityType.PLAYER:
            entityName = "player"
            pathName = (entityName)
        elif entity.type == EntityType.ENEMY_MELEE:
            entityName = "enemyMelee"
            pathName = (entityName)
        elif entity.type == EntityType.ENEMY_RANGED:
            entityName = "enemyRanged"
            pathName = (entityName)
        newAnim(entity, i, pathName)

        i += 1
    return (entities)

def mapX(x):
    x = (x*40) + 20
    return x

def mapY(y):
    y = (y*40)
    return y

def turretMapY(y):
    y = (y*40) + 10
    return y

def playAnim(displayWindow, entity):
    if entity.type != EntityType.ENEMY_RANGED:
        if entity.isWalking:
            entity.moveAnim[entity.direction].blit(displayWindow, (mapX(entity.x),mapY(entity.y)))
        elif entity.isAttacking:
            entity.attackAnim[entity.direction].blit(displayWindow, (mapX(entity.x),mapY(entity.y)))
        elif entity.isDead:
            entity.deathAnim[0].blit(displayWindow, (mapX(entity.x),mapY(entity.y)))
        else:
            entity.standAnim[entity.direction].blit(displayWindow, (mapX(entity.x),mapY(entity.y)))

    else:
        entity.standAnim[0].blit(displayWindow, (mapX(entity.x),turretMapY(entity.y)))
