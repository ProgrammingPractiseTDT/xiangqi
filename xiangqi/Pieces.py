import pygame
from .constrant import SQUARE_SIZE
import os

PADDING = 70
pygame.init()
pygame.display.set_mode()

class advisor:
    def __init__(self, row, col, color):
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        print(PADDING)
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/advisor_red.png')).convert(), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/advisor_black.png')).convert(),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.col)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.row)

    def draw(self, sur):
        sur.blit(self.img, (self.x, self.y))

class chariot:
    def __init__(self, row, col, color):
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/chariot_red.png')).convert(), (PADDING, PADDING))
        if self.color == 'black':
            self.img = pygame.transform.scale( pygame.image.load(os.path.join('Assests/chariot_black.png')).convert() , (PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.col)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.row)

        
    def draw(self, sur):
        sur.blit(self.img, (self.x, self.y))

class cannon:
    def __init__(self, row, col, color):
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/cannon_red.png')).convert(), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/cannon_black.png')).convert(),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.col)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.row)

    def draw(self, sur):
        sur.blit(self.img, (self.x, self.y))

class elephant:
    def __init__(self, row, col, color):
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/elephant_red.png')).convert(), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/elephant_black.png')).convert(),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.col)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.row)

    def draw(self, sur):
        sur.blit(self.img, (self.x, self.y))

class general:
    def __init__(self, row, col, color):
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/general_red.png')).convert(), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/general_black.png')).convert(),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.col)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.row)

    def draw(self, sur):
        sur.blit(self.img, (self.x, self.y))
    
    def possible_moves(self):
        moves = [(self.col -1 , self.row),(self.col + 1 , self.row), (self.col, self.row -1), (self.col, self.row +1)]
        if color == 'black':
            #constraint
            constraint = [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)]
            #vertiacally and #horizontally
        elif color == 'red':
            constraint = [(9,3), (9,4), (9,5), (8,3), (8,4), (8,5), (7,3), (7,4), (7,5)]
        
        return [i for i in moves if i in constraint]
        

class horse:
    def __init__(self, row, col, color):
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/horse_red.png')).convert(), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/horse_black.png')).convert(),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.col)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.row)

    def draw(self, sur):
        sur.blit(self.img, (self.x, self.y))
class soldier:
    def __init__(self, row, col, color):
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/soldier_red.png')).convert(), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/soldier_black.png')).convert(),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.col)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.row)

    def draw(self, sur):
        sur.blit(self.img, (self.x, self.y))