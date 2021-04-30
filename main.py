import pygame
pygame.init()

from xiangqi.constrant import WINDOW_SIZE
from xiangqi.Board import Board
from xiangqi.Pieces import *

FPS = 60
WIN = pygame.display.set_mode(WINDOW_SIZE)

running = True


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    # black_advisor = advisor(0, 0, 'black')
    while run:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()
        rowcol = (mouse_pos[1]//80, mouse_pos[0] // 80 )
        
        #print(rowcol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        board.draw_board(WIN)
        # black_advisor.draw(WIN)
        board.draw_pieces(WIN)
        pygame.display.update()
    pygame.quit()
main()