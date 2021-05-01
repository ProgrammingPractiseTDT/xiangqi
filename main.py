import pygame
pygame.init()

from xiangqi.constrant import WINDOW_SIZE
from xiangqi.Board import Board
from xiangqi.Pieces import *
FPS = 60
WIN = pygame.display.set_mode((WINDOW_SIZE))


def main():
    run = True
    clock = pygame.time.Clock()
    event = pygame.event.get()
    board = Board()
    # black_advisor = advisor(0, 0, 'black')
    # board.board[1][4].draw(WIN)
    board.draw_board(WIN)
        # black_advisor.draw(WIN)
    board.draw_pieces(WIN)
    # bot_decide(board)
    
    select = False
    playing = True
    while run:
       
                clock.tick(FPS)
                for event in pygame.event.get():
                    
                    if event.type == pygame.QUIT:
                            run = False

                    if event.type == pygame.MOUSEBUTTONUP and select == False and playing == True:
                        
                            mouse_pos = pygame.mouse.get_pos()
                            row,col = mouse_pos[1]//80, mouse_pos[0] // 80
                            print(row,col)
                            print(board.draw_circle(row,col, WIN))
                            print('select',select)
                            select = True
                        
                        # for event in pygame.event.get():
                    # elif event.type == pygame.MOUSEMOTION:
                        
                    #         select = True
                    elif event.type == pygame.MOUSEBUTTONUP and select== True and playing == True:
                        
                            mouse_pos = pygame.mouse.get_pos()
                            end_row,end_col = mouse_pos[1]//80, mouse_pos[0] // 80 
                            board.move(board.board[row][col],end_row,end_col)
                            print('score',board.score)
                            board.draw_board(WIN)
                            board.draw_pieces(WIN)
                            select = False
                if board.is_game_over() != False:
                    if board.is_game_over() == 'Red':
                        img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/player_win.png')), (90, 90))
                        WIN.blit(img, (350,350))
                    else:
                        img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/player_lose.png')), (90, 90))
                        WIN.blit(img, (350,350))
                    playing = False
                pygame.display.update()
    pygame.display.set_allow_screensaver(True)
    pygame.quit()
main()