import pygame
import Classes
import random
#import Main
#import numpy
pygame.init() #Loads the pygame window
screenWidth800 = 800
screenHeight800 = 800
displayWindow = pygame.display.set_mode((screenWidth800,screenHeight800)) #800x800 in size
#pygame.display.set_caption("Main menu")

font = pygame.font.SysFont("freesansbold.ttf", 40)

def draw_text(text, font, colour, surface, x, y):
    textobj = font.render(text, 1, colour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def name_text(text, font, colour, surface, x, y):
    textobj = font.render(text, 1, colour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.colour = (0,0,0)
        self.text = text
        self.txt_surface = font.render(text, True, self.colour)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)



textBox = InputBox(100, 100, 50, 20, 'TextBox')
clock = pygame.time.Clock()
#grid = numpy.zeros((20,20))
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
    draw_text('Game Name', font, (0, 0, 0), displayWindow, 20, 20)
    name_text('Parth', font, (0,0,0), displayWindow, 60,60)
    #gridDisplay(displayWindow,grid)
    pygame.display.update() #updates to new display
    for i in pygame.event.get(): # for every event
            if i.type == pygame.QUIT: #if event is to close pygame
                pygame.quit() #close pygame
    name_text('Parth', font, (0,0,0), displayWindow, 60,60)
    textBox.draw(displayWindow)
    clock.tick(60) #fps
