import pygame
import pyganim

class EntityType():
    PLAYER = 0
    ENEMY_MELEE = 1
    ENEMY_RANGED = 2
    COMPUTER = 3
    BOSS = 4

moveSprites = [
[(0, 64*8, 64, 64), (64*1, 64*8, 64, 64), (64*2, 64*8, 64, 64),  (64*3, 64*8, 64, 64), (64*4, 64*8, 64, 64), (64*5, 64*8, 64, 64), (64*6, 64*8, 64, 64)],
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
[(0, 64*12, 64, 64), (64*1, 64*12, 64, 64), (64*2, 64*12, 64, 64), (64*3, 64*12, 64, 64), (64*4, 64*12, 64, 64), (64*5, 64*12, 64, 64)],
[(0, 64*13, 64, 64), (64*1, 64*13, 64, 64), (64*2, 64*13, 64, 64), (64*3, 64*13, 64, 64), (64*4, 64*13, 64, 64), (64*5, 64*13, 64, 64)],
[(0, 64*14, 64, 64), (64*1, 64*14, 64, 64), (64*2, 64*14, 64, 64), (64*3, 64*14, 64, 64), (64*4, 64*14, 64, 64), (64*5, 64*14, 64, 64)],
[(0, 64*15, 64, 64), (64*1, 64*15, 64, 64), (64*2, 64*15, 64, 64), (64*3, 64*15, 64, 64), (64*4, 64*15, 64, 64), (64*5, 64*15, 64, 64)]]

bossAttackSprites = [
[(0, (64*21)+(192*0), 192, 192), (192*1, (64*21)+(192*0), 192, 192), (192*2, (64*21)+(192*0), 192, 192), (192*3, (64*21)+(192*0), 192, 192), (192*4, (64*21)+(192*0), 192, 192), (192*5, (64*21)+(192*0), 192, 192)],
[(0, (64*21)+(192*1), 192, 192), (192*1, (64*21)+(192*1), 192, 192), (192*2, (64*21)+(192*1), 192, 192), (192*3, (64*21)+(192*1), 192, 192), (192*4, (64*21)+(192*1), 192, 192), (192*5, (64*21)+(192*1), 192, 192)],
[(0, (64*21)+(192*2), 192, 192), (192*1, (64*21)+(192*2), 192, 192), (192*2, (64*21)+(192*2), 192, 192), (192*3, (64*21)+(192*2), 192, 192), (192*4, (64*21)+(192*2), 192, 192), (192*5, (64*21)+(192*2), 192, 192)],
[(0, (64*21)+(192*3), 192, 192), (192*1, (64*21)+(192*3), 192, 192), (192*2, (64*21)+(192*3), 192, 192), (192*3, (64*21)+(192*3), 192, 192), (192*4, (64*21)+(192*3), 192, 192), (192*5, (64*21)+(192*3), 192, 192)]]

rangedSprites = [[(0, 0, 64, 64)]]

deathSprites = [[(0, 64*20, 64, 64), (64*1, 64*20, 64, 64), (64*2, 64*20, 64, 64), (64*3, 64*20, 64, 64), (64*4, 64*20, 64, 64), (64*5, 64*20, 64, 64)]]

obstacleSprites = [[(0, 0, 40, 40)]]

beamSprites = [(0, 0, 40, 800)]


def makeAnim(entity, i, pathName):
    moveAnim = []
    standAnim = []
    attackAnim = []
    deathAnim = []
    obstacleAnim = []
    beamAnim = []

    if entity.type == EntityType.COMPUTER:
        anim = []
        images = pyganim.getImagesFromSpriteSheet('assets/'+pathName+'.png', rects=obstacleSprites[0])
        frames = list(zip(images, [100] * len(images)))
        animation = pyganim.PygAnimation(frames)
        animation.play()
        anim.append(animation)
        moveAnim = anim
        standAnim = anim
        attackAnim = anim
        deathAnim = anim

    elif entity.type == EntityType.ENEMY_RANGED:
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

        if entity.type == EntityType.ENEMY_RANGED:
            images = pyganim.getImagesFromSpriteSheet('assets/beam.png', rects=beamSprites)
            frames = list(zip(images, [100] * len(images)))
            animation = pyganim.PygAnimation(frames)
            animation.play()
            beamAnim.append(animation)

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
        elif entity.type == EntityType.BOSS:
            attackSprites = bossAttackSprites

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


    return([moveAnim, standAnim, attackAnim, deathAnim, beamAnim])

def newAnim(entity, i, pathName):
    anim = makeAnim(entity, i, pathName)
    entity.moveAnim = anim[0]
    entity.standAnim = anim[1]
    entity.attackAnim = anim[2]
    entity.deathAnim = anim[3]
    entity.attackParticles = anim[4]

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
        elif entity.type == EntityType.COMPUTER:
            entityName = "computer"
            pathName = (entityName)
        elif entity.type == EntityType.BOSS:
            entityName = "finalBoss"
            pathName = (entityName)
        newAnim(entity, i, pathName)

        i += 1

def mapX(x):
    x = (x*40) + 20
    return x

def mapY(y):
    y = (y*40)
    return y

def shiftedMapX(x, shift):
    x = (x*40) + shift
    return x

def shiftedMapY(y, shift):
    y = (y*40) + shift
    return y

def playAnim(displayWindow, entity):
    if entity.type == EntityType.ENEMY_RANGED:
        entity.standAnim[0].blit(displayWindow, (mapX(entity.x),shiftedMapY(entity.y, 10)))
        if entity.isAttacking:
                entity.attackParticles[0].blit(displayWindow, (shiftedMapX(entity.x, 32),shiftedMapY(entity.y, 64)))

    elif entity.type == EntityType.COMPUTER:
        entity.standAnim[0].blit(displayWindow, (shiftedMapX(entity.x, 30),shiftedMapY(entity.y, 30)))

    else:
        if entity.isWalking:
            entity.moveAnim[entity.direction].blit(displayWindow, (mapX(entity.x),mapY(entity.y)))
        elif entity.isAttacking:
            if entity.type == EntityType.BOSS:
                entity.attackAnim[entity.direction].blit(displayWindow, (shiftedMapX(entity.x, -45),shiftedMapY(entity.y, -64)))
            else:
                entity.attackAnim[entity.direction].blit(displayWindow, (mapX(entity.x),mapY(entity.y)))
        elif entity.isDead:
            entity.deathAnim[0].blit(displayWindow, (mapX(entity.x),mapY(entity.y)))
        else:
            entity.standAnim[entity.direction].blit(displayWindow, (mapX(entity.x),mapY(entity.y)))
