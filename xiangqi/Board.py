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
for i in range(0,9,2):
    RED_POS.append(soldier(5,i,'red'))


class Board:
    def __init__(self):
        self.board = []
        self.turn = 0
        self.red_pieces = self.black_pieces = 16
        self.red_super_soldier = self.black_super_soldier = 0

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
