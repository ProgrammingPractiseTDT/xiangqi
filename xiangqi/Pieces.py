import pygame
from .constrant import SQUARE_SIZE
import os

PADDING = 70

class advisor:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(r'D:\ChineseChess\Assests\advisor_red.png'), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(r'D:\ChineseChess\Assests\advisor_black.png'),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.row)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.col)

    def draw(self, sur):
        sur.blit(self.img, (self.x, self.y))

class chariot:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(r'D:\ChineseChess\Assests\chariot_red.png'), (PADDING, PADDING))
        if self.color == 'black':
            self.img = pygame.transform.scale(pygame.image.load(r'D:\ChineseChess\Assests\chariot_black.png'), (PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.row)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.col)

        
    def draw(self, sur):
        sur.blit(self.img, (self.x, self.y))

class cannon:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(r'D:\ChineseChess\Assests\cannon_red.png'), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(r'D:\ChineseChess\Assests\cannon_black.png'),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.row)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.col)

    def draw(self, sur):
        sur.blit(self.img, (self.x, self.y))

class elephant:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(r'D:\ChineseChess\Assests\elephant_red.png'), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(r'D:\ChineseChess\Assests\elephant_black.png'),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.row)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.col)

    def draw(self, sur):
        sur.blit(self.img, (self.x, self.y))

class general:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(r'D:\ChineseChess\Assests\general_red.png'), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(r'D:\ChineseChess\Assests\general_black.png'),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.row)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.col)

    def draw(self, sur):
        sur.blit(self.img, (self.x, self.y))

class horse:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(r'D:\ChineseChess\Assests\horse_red.png'), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(r'D:\ChineseChess\Assests\horse_black.png'),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.row)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.col)

    def draw(self, sur):
        sur.blit(self.img, (self.x, self.y))

class soldier:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(r'D:\ChineseChess\Assests\soldier_red.png'), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(r'D:\ChineseChess\Assests\soldier_black.png'),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.row)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.col)

    def draw(self, sur):
        sur.blit(self.img, (self.x, self.y))