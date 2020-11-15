import random
#Class file
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

class Entity():
    def __init__(self,type,w,h,x,y,hp,v,direction):
        self.type = type
        self.x = x
        self.y = y
        self.direction = Direction.DOWN
        self.width = 64
        self.height = 64
        self.vel = v
        self.isWalking = False
        self.isAttacking = False
        self.isDead = False
        self.hp = hp
        self.moveAnim = []
        self.standAnim = []
        self.attackAnim = []
        self.deathAnim = []

    def render(self):
        pass
#Can you see this comment


class Computer(Entity):
    def __init__(self,type,w,h,x,y):
        super().__init__(type,w,h,x,y)

    def unlockDoor():
        return True


class Mob(Entity):
    def __init__(self,type,w,h,x,y,hp,v,direction):
        super().__init__(type,w,h,x,y,hp,v,direction)

class Player(Mob):
    def __init__(self,type,w,h,x,y,hp,v,direction): # width, height, x coord, y coord, health, velocity
        super().__init__(type,w,h,x,y,hp,v,direction)

    def die(self):
        pass

class Enemy(Mob):
    def __init__(self,type,w,h,x,y,hp,v,direction):
        super().__init__(type,w,h,x,y,hp,v,direction)

    def moveEnemy(self):
        pass

class meleeBot(Enemy):
    def __init__(self,type,w,h,x,y,hp,v,direction):
        super().__init__(type,w,h,x,y,hp,v,direction)

    def attack(self):
        print("Stab")

    def moveEnemy(self,player):
        if abs(self.x - player.x) < 2 and self.y == player.y:
            self.attack()
        elif self.x == player.x and abs(self.y - player.y) < 2:
            self.attack()
        else:
            needToMoveX = False
            needToMoveY = False
            direcX = 0
            direcY = 0
            if self.x > player.x:
                needToMoveX = True
                direcX = Direction.LEFT
            elif self.x < player.x:
                needToMoveX = True
                direcX = Direction.RIGHT

            if self.y > player.y:
                needToMoveY = True
                direcY = Direction.UP
            elif self.y < player.y:
                needToMoveY = True
                direcY = Direction.DOWN

            if needToMoveX == True and needToMoveY == True:
                rando = random.choice(["X","Y"])
                if rando == "X":
                    self.direction = direcX
                else:
                    self.direction = direcY
            else:
                if needToMoveX == True:
                    self.direction = direcX
                else:
                    self.direction = direcY

            if self.direction == 0:
                self.y -= 1
            elif self.direction == 1:
                self.x -= 1
            elif self.direction == 2:
                self.y += 1
            else:
                self.x += 1

class rangeBot(Enemy):
    def __init__(self,type,w,h,x,y,hp,v,direction):
        super().__init__(type,w,h,x,y,hp,v,direction)
        self.countdown = 60

    def shoot(self):
        if self.countdown == 0:
            self.countdown = 60
            print("Shoot") #Add code to shoot laser at player here, display a laser and then call a isHit
            return True
        else:
            self.countdown -= 1
            return False

    def checkShoot(self,player):
        shouldShoot = False
        if self.x == player.x:
            shouldShoot = True
        return shouldShoot



class Item(Entity):
    def __init__(self,type,w,h,x,y,hp,v,direction):
        super().__init__(type,w,h,x,y,hp,v,direction)

class Obstacle(Entity):
    def __init__(self,type,w,h,x,y,hp,v,direction):
        super().__init__(type,w,h,x,y,hp,v,direction)


class DragAndDrop():
    def __init__(self, x, y, object):
        self.x = x
        self.y = y
        self.Rect = object.get_rect(center="x,y")
        self.Rect.x = self.x
        self.Rect.y = self.y

    def displayImg(x,y):
        displayWindow.blit(object, (x,y))
