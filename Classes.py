#Class file
class Direction():
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

class EntityType():
    PLAYER = 0
    ENEMY = 1

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
        self.health = hp
        self.moveAnim = []
        self.standAnim = []
        self.attackAnim = []
        self.deathAnim = []

    def render(self):
        pass
#Can you see this comment
class Mob(Entity):
    def __init__(self,type,w,h,x,y,hp,v,direction):
        super().__init__(type,w,h,x,y,hp,v,direction)

class Player(Mob):
    def __init__(self,type,w,h,x,y,hp,v,direction): # width, height, x coord, y coord, health, velocity
        super().__init__(type,w,h,x,y,hp,v,direction)

    def movePlayer(self,input):
        pass

    def attack(self):
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
        pass

    def move(self):
        pass

class rangeBot(Enemy):
    def __init__(self,type,w,h,x,y,hp,v,direction):
        super().__init__(type,w,h,x,y,hp,v,direction)

    def shoot(self):
        pass

    def move(self):
        if player.x > self.x:
            self.dir = Direction.RIGHT
            self.x += self.vel
        elif player.x < self.x:
            self.dir = Direction.LEFT
            self.x -= self.vel
        else:
            self.dir = Direction.DOWN
            self.shoot()

class Item(Entity):
    def __init__(self,type,w,h,x,y,hp,v,direction):
        super().__init__(type,w,h,x,y,hp,v,direction)

class Obstacle(Entity):
    def __init__(self,type,w,h,x,y,hp,v,direction):
        super().__init__(type,w,h,x,y,hp,v,direction)
