import pygame
from .constrant import SQUARE_SIZE
import os

PADDING = 70
pygame.init()
pygame.display.set_mode()

class advisor:
    def __init__(self,name, row, col, color):
        self.name = name
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        print(PADDING)
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/advisor_red.png')), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/advisor_black.png')),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.col)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.row)

    def draw(self, sur):
        self.calculate_pos()
        sur.blit(self.img, (self.x, self.y))
    def possible_moves(self):
        moves = [(self.row -1 , self.col-1),(self.row + 1 , self.col+1), (self.row+1, self.col -1), (self.row-1, self.col +1)]
        if self.color == 'black':
            #constraint
            constraint = [(0,3), (0,4), (0,5), (1,4),  (2,3), (2,4), (2,5)]
            #vertiacally and #horizontally
        elif self.color == 'red':
            constraint = [(9,3), (9,4), (9,5),  (8,4),  (7,3), (7,4), (7,5)]
        
        return [ move for move in moves if move in constraint]

class chariot:
    def __init__(self,name, row, col, color):
        self.name = name
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/chariot_red.png')), (PADDING, PADDING))
        if self.color == 'black':
            self.img = pygame.transform.scale( pygame.image.load(os.path.join('Assests/chariot_black.png')) , (PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.col)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.row)

        
    def draw(self, sur):
        self.calculate_pos()
        sur.blit(self.img, (self.x, self.y))
    
    def possible_moves(self):
        moves = [(row,self.col) for row in range(10) if row != self.row]
        for col in range(9):
            if col != self.col:
                moves.append((self.row, col))
        return moves


class cannon:
    def __init__(self,name, row, col, color):
        self.name = name
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/cannon_red.png')), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/cannon_black.png')),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.col)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.row)

    def draw(self, sur):
        self.calculate_pos()
        sur.blit(self.img, (self.x, self.y))
    
    def possible_moves(self):
        moves = [(row,self.col) for row in range(10) if row != self.row]
        for col in range(9):
            if col != self.col:
                moves.append((self.row, col))
        return moves

class elephant:
    def __init__(self,name, row, col, color):
        self.name = name
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/elephant_red.png')), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/elephant_black.png')),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.col)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.row)

    def draw(self, sur):
        self.calculate_pos()
        sur.blit(self.img, (self.x, self.y))
    
    def possible_moves(self):
        #move  2 space diagonally but can not crossover the river
        moves = [(self.row+2, self.col+2), (self.row-2, self.col-2), (self.row+2, self.col-2), (self.row-2, self.col+2)] 
        if self.color == 'black':
            return [ move for move in moves if 0<=move[0]<=4 and 0<=move[1]<=8]
        if self.color == 'red':
            return [ move for move in moves if 5<=move[0]<=9 and 0<=move[1]<=8]


class general:
    def __init__(self,name, row, col, color):
        self.name = name
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/general_red.png')), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/general_black.png')),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.col)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.row)

    def draw(self, sur):
        self.calculate_pos()
        sur.blit(self.img, (self.x, self.y))
    
    def possible_moves(self):
        moves = [(self.row -1 , self.col),(self.row + 1 , self.col), (self.row, self.col -1), (self.row, self.col +1)]
        if self.color == 'black':
            #constraint
            constraint = [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)]
            #vertiacally and #horizontally
        elif self.color == 'red':
            constraint = [(9,3), (9,4), (9,5), (8,3), (8,4), (8,5), (7,3), (7,4), (7,5)]
        
        return [ move for move in moves if move in constraint]
        

class horse:
    def __init__(self,name, row, col, color):
        self.name = name
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/horse_red.png')), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/horse_black.png')),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.col)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.row)

    def draw(self, sur):
        self.calculate_pos()
        sur.blit(self.img, (self.x, self.y))

    def possible_moves(self):
            moves = []
            #add one more horizontally space move
            move= (self.row, self.col +1)#right
               
            moves.append( (move[0]+1, move[1]+1))
            moves.append( (move[0]-1, move[1]+1))
            move = (self.row+1, self.col)#bottom
            moves.append( (move[0]+1, move[1]+1))
            moves.append((move[0]+1, move[1]-1))
            move = (self.row, self.col -1)#left
            moves.append( (move[0]-1, move[1] -1))
            moves.append( (move[0]+1, move[1] -1))
            move = (self.row-1, self.col)#above
            moves.append( (move[0]-1, move[1] -1))
            moves.append( (move[0]-1, move[1] +1))
            
            return [ move for move in moves if 0<=move[0]<=9 and 0<=move[1]<=8] #move with constraint
               
               

class soldier:
    def __init__(self,name, row, col, color):
        self.name = name
        self.col = col
        self.row = row
        self.color = color
        self.y = 0
        self.x = 0
        self.calculate_pos()
        if self.color == 'red':
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/soldier_red.png')), (PADDING, PADDING))
        if self.color == "black":
            self.img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/soldier_black.png')),(PADDING, PADDING))

    def calculate_pos(self):
        self.x = 40 - PADDING//2 + (SQUARE_SIZE * self.col)
        self.y = 40 - PADDING//2 + (SQUARE_SIZE * self.row)

    def draw(self, sur):
        self.calculate_pos()
        sur.blit(self.img, (self.x, self.y))
    

    def possible_moves(self):
        if self.color == 'black':
            if self.row ==9:
                moves = [(self.row, self.col-1), (self.row, self.col+1)]
            else:
                    moves = [ (self.row +1 , self.col )]
                    if self.row > 4:
                        moves.append( (self.row , self.col-1))
                        moves.append( (self.row, self.col +1))
                    
                        
        elif self.color == 'red':
            if self.row ==0:
                moves = [(self.row, self.col-1), (self.row, self.col+1)]
            else:
                    moves = [ (self.row -1 , self.col)]
                    if self.row < 5:
                        moves.append( (self.row , self.col-1))
                        moves.append( (self.row, self.col +1))
    
        return [ move for move in moves if 0<=move[0]<=9 and 0<=move[1]<=8] #move with constraint







        #hypothesis piece
class h_piece:
    def __init__(self,name, row, col, color):
        self.name = name
        self.col = col
        self.row = row
        self.color = color
    
    def possible_moves(self):
        if self.name ==  'advisor':
                        moves = [(self.row -1 , self.col-1),(self.row + 1 , self.col+1), (self.row+1, self.col -1), (self.row-1, self.col +1)]
                        if self.color == 'black':
                            #constraint
                            constraint = [(0,3), (0,4), (0,5), (1,4),  (2,3), (2,4), (2,5)]
                            #vertiacally and #horizontally
                        elif self.color == 'red':
                            constraint = [(9,3), (9,4), (9,5),  (8,4),  (7,3), (7,4), (7,5)]
                        
                        return [ move for move in moves if move in constraint]
        
        elif self.name ==  'soldier':
                    #
                    if self.color == 'black':
                        if self.row ==9:
                            moves = [(self.row, self.col-1), (self.row, self.col+1)]
                        else:
                            moves = [ (self.row +1 , self.col )]
                            if self.row > 4:
                                moves.append( (self.row , self.col-1))
                                moves.append( (self.row, self.col +1))
                            
                                
                    elif self.color == 'red':
                                if self.row ==0:
                                    moves = [(self.row, self.col-1), (self.row, self.col+1)]
                                else:
                                        moves = [ (self.row -1 , self.col)]
                                        if self.row < 5:
                                            moves.append( (self.row , self.col-1))
                                            moves.append( (self.row, self.col +1))
        
                    return [ move for move in moves if 0<=move[0]<=9 and 0<=move[1]<=8] #move with constraint
            # 
        elif self.name == 'general':
                        moves = [(self.row -1 , self.col),(self.row + 1 , self.col), (self.row, self.col -1), (self.row, self.col +1)]
                        if self.color == 'black':
                            #constraint
                            constraint = [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)]
                            #vertiacally and #horizontally
                        elif self.color == 'red':
                            constraint = [(9,3), (9,4), (9,5), (8,3), (8,4), (8,5), (7,3), (7,4), (7,5)]
                        
                        return [ move for move in moves if move in constraint]


        elif self.name == 'horse':
                    moves = []
                    #add one more horizontally space move
                    move= (self.row, self.col +1)#right
                    
                    moves.append( (move[0]+1, move[1]+1))
                    moves.append( (move[0]-1, move[1]+1))
                    move = (self.row+1, self.col)#bottom
                    moves.append( (move[0]+1, move[1]+1))
                    moves.append((move[0]+1, move[1]-1))
                    move = (self.row, self.col -1)#left
                    moves.append( (move[0]-1, move[1] -1))
                    moves.append( (move[0]+1, move[1] -1))
                    move = (self.row-1, self.col)#above
                    moves.append( (move[0]-1, move[1] -1))
                    moves.append( (move[0]-1, move[1] +1))
                    
                    return [ move for move in moves if 0<=move[0]<=9 and 0<=move[1]<=8] #move with constraint


        elif self.name == 'chariot':
                    moves = [(row,self.col) for row in range(10) if row != self.row]
                    for col in range(9):
                        if col != self.col:
                            moves.append((self.row, col))
                    return moves



        elif self.name == 'cannon':
                    moves = [(row,self.col) for row in range(10) if row != self.row]
                    for col in range(9):
                        if col != self.col:
                            moves.append((self.row, col))
                    return moves
        
        elif self.name == 'elephant':
                    #move  2 space diagonally but can not crossover the river
                    moves = [(self.row+2, self.col+2), (self.row-2, self.col-2), (self.row+2, self.col-2), (self.row-2, self.col+2)] 
                    if self.color == 'black':
                        return [ move for move in moves if 0<=move[0]<=4 and 0<=move[1]<=8]
                    if self.color == 'red':
                        return [ move for move in moves if 5<=move[0]<=9 and 0<=move[1]<=8]

