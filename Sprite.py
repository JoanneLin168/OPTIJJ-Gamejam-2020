import pygame
import pyganim
moveSprites = [[(0, 64*8, 64, 64), (64*1, 64*8, 64, 64), (64*2, 64*8, 64, 64), (64*3, 64*8, 64, 64), (64*4, 64*8, 64, 64), (64*5, 64*8, 64, 64), (64*6, 64*8, 64, 64)],
         [(0, 64*9, 64, 64), (64*1, 64*9, 64, 64), (64*2, 64*9, 64, 64), (64*3, 64*9, 64, 64), (64*4, 64*9, 64, 64), (64*5, 64*9, 64, 64), (64*6, 64*9, 64, 64)],
         [(0, 64*10, 64, 64), (64*1, 64*10, 64, 64), (64*2, 64*10, 64, 64), (64*3, 64*10, 64, 64), (64*4, 64*10, 64, 64), (64*5, 64*10, 64, 64), (64*6, 64*10, 64, 64)],
         [(0, 64*11, 64, 64), (64*1, 64*11, 64, 64), (64*2, 64*11, 64, 64), (64*3, 64*11, 64, 64), (64*4, 64*11, 64, 64), (64*5, 64*11, 64, 64), (64*6, 64*11, 64, 64)]]

standSprites = [[(0, 64*8, 64, 64)], [(0, 64*9, 64, 64)], [(0, 64*10, 64, 64)], [(0, 64*11, 64, 64)]]

numOfEntities = 2

pathNames = ['player', 'enemy1']

moveAnim = []
standAnim = []
animation = [[],[]] #[0] = player, [1] = enemy
#animation[x][0] = movAnim, animation[x][1] = standAnim

for path in range(len(pathNames)):
    for dir in range(len(moveSprites)):
        moveImages = pyganim.getImagesFromSpriteSheet('assets/'+pathNames[path]+'.png', rects=moveSprites[dir])
        moveFrames = list(zip(moveImages, [100] * len(moveImages)))
        moveAnimation = pyganim.PygAnimation(moveFrames)
        moveAnimation.play()
        moveAnim.append(moveAnimation)

        standImages = pyganim.getImagesFromSpriteSheet('assets/'+pathNames[path]+'.png', rects=standSprites[dir])
        standFrames = list(zip(standImages, [100] * len(standImages)))
        standAnimation = pyganim.PygAnimation(standFrames)
        standAnimation.play()
        standAnim.append(standAnimation)
    animation[path].append(moveAnim)
    animation[path].append(standAnim)
    moveAnim = []
    standAnim = []

def initAnim(player, enemy):
    player.moveAnim = animation[0][0]
    player.standAnim = animation[0][1]
    enemy.moveAnim = animation[1][0]
    enemy.standAnim = animation[1][1]


def mapX(x):
    x = (x*40) + 20
    return x

def mapY(y):
    y = (y*40)
    return y

def playAnim(displayWindow, player, enemy):
    if player.isWalking:
        player.moveAnim[player.direction].blit(displayWindow, (mapX(player.x),mapY(player.y)))
    else:
        player.standAnim[player.direction].blit(displayWindow, (mapX(player.x),mapY(player.y)))

    if enemy.isWalking:
        enemy.moveAnim[enemy.direction].blit(displayWindow, (mapX(enemy.x),mapY(enemy.y)))
    else:
        enemy.standAnim[enemy.direction].blit(displayWindow, (mapX(enemy.x),mapY(enemy.y)))
