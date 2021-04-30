import pygame
from .constrant import SQUARE_SIZE, COLS, ROWS, BROWN, YELLOW, BOARD_SIZE, BLACK
from .Pieces import *
pygame.init()

BLACK_POS = []
BLACK_POS.append(chariot(0,0,'black'))
BLACK_POS.append(horse(0,1,'black'))
BLACK_POS.append(elephant(0,2,'black'))
BLACK_POS.append(advisor(0,3,'black'))
BLACK_POS.append(general(0,4,'black'))
BLACK_POS.append(advisor(0,5,'black'))
BLACK_POS.append(elephant(0,6,'black'))
BLACK_POS.append(horse(0,7,'black'))
BLACK_POS.append(chariot(0,8,'black'))
BLACK_POS.append(cannon(2,1,'black'))
BLACK_POS.append(cannon(2,7,'black'))
for i in range(0,9,2):
    BLACK_POS.append(soldier(3,i,'black'))


RED_POS = []
RED_POS.append(chariot(9,8,'red'))
RED_POS.append(horse(9,7,'red'))
RED_POS.append(elephant(9,6,'red'))
RED_POS.append(advisor(9,5,'red'))
RED_POS.append(general(9,4,'red'))
RED_POS.append(advisor(9,3,'red'))
RED_POS.append(elephant(9,2,'red'))
RED_POS.append(horse(9,1,'red'))
RED_POS.append(chariot(9,0,'red'))
RED_POS.append(cannon(7,1,'red'))
RED_POS.append(cannon(7,7,'red'))
for i in range(0,9,2):
    RED_POS.append(soldier(6,i,'red'))


def cross_of_point(row,col):
    return [(row+1,col), (row-1, col), (row, col+1), (row, col-1)]
def diagonal_of_point(row,col):
    return [(row+1, col+1), (row-1, col-1), (row+1, col-1), (row-1, col+1)]
class Board:
    def __init__(self):
        self.board = [[None for _ in range(COLS+1) ] for _ in range(ROWS+1) ]
        self.turn = 0
        self.red_pieces = self.black_pieces = 16
        self.red_super_soldier = self.black_super_soldier = 0

        #create back -end start game position
        for black_piece in BLACK_POS:
            row,col = black_piece.row, black_piece.col
            self.board[row][col] = black_piece
        for red_piece in RED_POS:
            row,col = red_piece.row, red_piece.col
            self.board[row][col] = red_piece
        self.black_general = self.board[0][4]
        self.red_general = self.board[9][4]
        self.hourse_constraint = [self.board[0][1], self.board[0][7], self.board[9][1], self.board[9][7]]
        self.cannon_constraint = [self.board[2][1], self.board[2][7], self.board[7][1], self.board[7][7]]

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
        for i in BLACK_POS:
            i.draw(sur)
        for i in RED_POS:
            i.draw(sur)
    
    def capture(self, piece, new_row, new_col):
                if piece in self.hourse_constraint:#check if its a hourse capture must follow rule
                    row_piece, col_piece = piece.row, piece.col
                    for point in cross_of_point[row_piece][col_piece]:#check around the hourse if there another piece
                        if self.board[point[0]][point[1]] !=None:
                             if (new_row, new_col)  in cross_of_point(point[0], point[1]):
                                return False
                
                    else:   
                            destroy_piece = self.board[new_row][new_col]
                            self.board[piece.row][piece.col] = None #remove current piece position
                            del destroy_piece
                            self.board[new_row][new_col] = piece #move it to new position
                            return True
                    
            
        

    
    def move(self,piece, new_row, new_col):
         if (new_row, new_col) in piece.possible_moves:
                if self.board[new_row][new_col] == None:
                        self.board[piece.row][piece.col] = None #remove current piece position
                        self.board[new_row][new_col] = piece #move it to new position
                        return True
                elif self.board[new_row][new_col].color == piece.color:
                    return False
                elif self.board[new_row][new_col].color != piece.color:
                    return self.capture(piece, new_row, new_col)
