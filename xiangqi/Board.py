import pygame
from .constrant import SQUARE_SIZE, COLS, ROWS, BROWN, YELLOW, BOARD_SIZE, BLACK
from .Pieces import *
import os, copy
pygame.init()
#heuristic
heuristic = {'general': 100, 'chariot':9, 'hourse':5, 'cannon' :4, 'soldier':1, 'elephant': 2, 'advisor':2}
BLACK_POS = []
BLACK_POS.append(chariot('chariot',0,0,'black'))
BLACK_POS.append(horse('hourse',0,1,'black'))
BLACK_POS.append(elephant('elephant',0,2,'black'))
BLACK_POS.append(advisor('advisor',0,3,'black'))
BLACK_POS.append(general('general',0,4,'black'))
BLACK_POS.append(advisor('advisor',0,5,'black'))
BLACK_POS.append(elephant('elephant',0,6,'black'))
BLACK_POS.append(horse('hourse',0,7,'black'))
BLACK_POS.append(chariot('chariot',0,8,'black'))
BLACK_POS.append(cannon('cannon',2,1,'black'))
BLACK_POS.append(cannon('cannon',2,7,'black'))
for i in range(0,9,2):
    BLACK_POS.append(soldier('soldier',3,i,'black'))


RED_POS = []
RED_POS.append(chariot('chariot',9,8,'red'))
RED_POS.append(horse('hourse',9,7,'red'))
RED_POS.append(elephant('elephant',9,6,'red'))
RED_POS.append(advisor('advisor',9,5,'red'))
RED_POS.append(general('general',9,4,'red'))
RED_POS.append(advisor('advisor',9,3,'red'))
RED_POS.append(elephant('elephant',9,2,'red'))
RED_POS.append(horse('hourse',9,1,'red'))
RED_POS.append(chariot('chariot',9,0,'red'))
RED_POS.append(cannon('cannon',7,1,'red'))
RED_POS.append(cannon('cannon',7,7,'red'))
for i in range(0,9,2):
    RED_POS.append(soldier('soldier',6,i,'red'))


def cross_of_point(row,col):
    L =  [(row+1,col), (row-1, col), (row, col+1), (row, col-1)]
    return [ i for i in L if 0<=i[0]<=9 and 0<=i[1]<= 8]
def diagonal_of_point(row,col):
    L = [(row+1, col+1), (row-1, col-1), (row+1, col-1), (row-1, col+1)]
    return [ i for i in L if 0<=i[0]<=9 and 0<=i[1]<= 8]
class Board:
    def __init__(self):
        self.board = [[None for _ in range(COLS+1) ] for _ in range(ROWS+1) ]
        self.turn = 0
        self.red_pieces = self.black_pieces = 16
        self.score = 0


        #create back -end start game position
        for black_piece in BLACK_POS:
            row,col = black_piece.row, black_piece.col
            # print('aka',row,col)
            self.board[row][col] = black_piece
        for red_piece in RED_POS:
            row,col = red_piece.row, red_piece.col
            self.board[row][col] = red_piece
        # self.black_general = self.board[0][4]
        # self.red_general = self.board[9][4]
        # self.hourse_constraint = [self.board[0][1], self.board[0][7], self.board[9][1], self.board[9][7]]
        # self.chariot_cannon_constraint = [self.board[2][1], self.board[2][7], self.board[7][1], self.board[7][7], self.board[0][0], self.board[0][8], self.board[9][0], self.board[9][8]]
        # self.elephant_constrant = [self.board[9][6], self.board[9][2], self.board[0][6], self.board[0][2]]


        # print(self.cannon_constraint)

    def draw_board(self, sur):
        sur.fill(BROWN)
        the_board = pygame.Surface((BOARD_SIZE))
        the_board.fill(YELLOW)
        pygame.draw.rect(the_board, BLACK, (0, 0,SQUARE_SIZE * 8,SQUARE_SIZE * 9), 5)
        for i in range(COLS):
            for j in range(ROWS):
                if j != 4:
                    pygame.draw.rect(the_board,BLACK , (SQUARE_SIZE*i, SQUARE_SIZE*j, SQUARE_SIZE, SQUARE_SIZE),2)
                if (i == 3 and j == 0) or (i == 3 and j == 7):
                    pygame.draw.line(the_board, BLACK, (SQUARE_SIZE * i, SQUARE_SIZE * j), (SQUARE_SIZE * (i + 2), SQUARE_SIZE * (j+2)), 4)
                if (i == 5 and j == 0) or (i == 5 and j == 7):
                    pygame.draw.line(the_board, BLACK, (SQUARE_SIZE * i, SQUARE_SIZE * j), (SQUARE_SIZE * (i-2), SQUARE_SIZE * (j+2)), 4)
        sur.blit(the_board, (40,40))

    def draw_pieces(self, sur):
        for i in range(ROWS+1):
            for j in range(COLS+1):
                if self.board[i][j] != None:
                    self.board[i][j].draw(sur)
    
    def unit_move(self, piece, new_row, new_col, capture):
                #prepare calculate score
                if capture == True:
                    captured_piece = self.board[new_row][new_col]
                    if piece.color == 'black':
                       score = -heuristic[captured_piece.name]
                    else:
                       score = heuristic[captured_piece.name]
                
                movable = False
                capturable = False




                row_piece, col_piece = piece.row, piece.col
                if piece.name == 'hourse':#check if its a hourse capture must follow rule
                    #oke    
                    #check if the hourse is blocked
                            for point in cross_of_point(row_piece,col_piece):#check around the hourse if there another piece
                                if self.board[point[0]][point[1]] !=None:
                                    if (new_row, new_col)  in diagonal_of_point(point[0], point[1]):
                                        return False
                        
                            else:   
                                    
                                    movable = True
                                    capturable = True


                elif piece.name == 'cannon' or piece.name == 'chariot':
                            count = 0
                            if new_row == row_piece:
                                step = new_col - col_piece
                                if step > 0:
                                    step = 1
                                elif step < 0:
                                    step = -1
                                for i in range(col_piece+step, new_col, step):
                                    if self.board[row_piece][i] !=None:
                                                count+=1
                                
                                if count == 0:
                                    movable = True #if there a not any piece on the way to position
                                    if piece.name == 'chariot':
                                        capturable = True
                                elif count ==1:
                                    if piece.name == 'cannon': #cannon can attack if there a piece on the way
                                        capturable = True
                                else:
                                    return False
                            elif new_col == col_piece:
                                step = new_row - row_piece
                                if step > 0:
                                    step = 1
                                if step < 0:
                                    step = -1
                                
                                for i in range(row_piece+step, new_row, step):
                                    if self.board[i][col_piece] !=None:
                                                count+=1
                                if count == 0:
                                    movable = True #if there a not any piece on the way to position
                                    if piece.name == 'chariot':
                                        capturable = True
                                elif count ==1:
                                    if piece.name == 'cannon': #cannon can attack if there a piece on the way
                                        capturable = True
                                else:
                                    return False
                elif piece.name == 'elephant':
                                #get nearest space diagontally on the way to new space
                                (row_b, col_b) = (new_row -  row_piece)//2, (new_col - col_piece)//2
                                if self.board[row_piece+ row_b][col_piece + col_b] == None:
                                    
                                    movable = True
                                    capturable = True
                                else:
                                    return False
                else:
                                   #for soldier and adviosr and general
                                   movable = True
                                   capturable = True
                
                if capture == True and capturable == True:
                                    self.board[new_row][new_col] = None
                                    del captured_piece
                                    self.board[new_row][new_col] = piece
                                    self.board[row_piece][col_piece] = None
                                    piece.row = new_row
                                    piece.col = new_col
                                    self.score += score
                                    return True
                if movable == True:
                                    #move piece in free space, just change it location
                                    self.board[new_row][new_col] = piece
                                    self.board[row_piece][col_piece] = None
                                    piece.row = new_row
                                    piece.col = new_col
                                    return True
                return False
            
                            
                                  
                    

    
    def move(self,piece, new_row, new_col):
        if piece != None:

            if (new_row, new_col) in piece.possible_moves():
                    if self.board[new_row][new_col] == None:
                        return self.unit_move(piece, new_row, new_col, capture = False)

                    if self.board[new_row][new_col].color == piece.color:
                        return False
                    elif self.board[new_row][new_col].color != piece.color:
                        return self.unit_move(piece, new_row, new_col, capture = True)
    


    def draw_circle(self,y,x, sur):
      x = 40 - PADDING//2 + (SQUARE_SIZE * x)
      y = 40 - PADDING//2 + (SQUARE_SIZE * y)

      img  = pygame.transform.scale(pygame.image.load(os.path.join('Assests/circle.png')), (PADDING, PADDING))
      sur.blit(img, (x,y))

    
    def is_game_over(self):
        if self.score >= 100:
            return 'Red'
        if self.score <= -100:
            return 'Black'
        
        return False






def bot_decide(board):
    state = copy.deepcopy(board)
    state.board = None