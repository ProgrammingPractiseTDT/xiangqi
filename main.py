import pygame
pygame.init()

from xiangqi.constrant import WINDOW_SIZE
from xiangqi.Board import *
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
    # board.bot_decide()
    
    select = False
    playing = True
    while run:
       
                clock.tick(FPS)
                if board.turn == -1:
                        bot_move = bot_decide(board)
                        print('move succes', bot_move)
                        move(board, board.board[bot_move[0]][bot_move[1]], bot_move[2], bot_move[3])
                        board.draw_board(WIN)
                        board.draw_pieces(WIN)
                        board.turn = 1
                for event in pygame.event.get():
                    
                    
                    if event.type == pygame.QUIT:
                            run = False

                    if event.type == pygame.MOUSEBUTTONUP and select == False and playing == True:
                        
                            mouse_pos = pygame.mouse.get_pos()
                            row,col = mouse_pos[1]//80, mouse_pos[0] // 80
                            print(board.draw_circle(row,col, WIN))
                            
                            if board.turn == 1:
                                if board.board[row][col]!= None and board.board[row][col].color == 'red':
                                    print(row,col)
                                    
                                    print('select',select)
                                    select = True
                            
                            for black in board.blacks:
                                    print(black.color,'-',black.name)
                        # for event in pygame.event.get():
                    # elif event.type == pygame.MOUSEMOTION:
                        
                    #         select = True
                    elif event.type == pygame.MOUSEBUTTONUP and select== True and playing == True:
                        
                            mouse_pos = pygame.mouse.get_pos()
                            end_row,end_col = mouse_pos[1]//80, mouse_pos[0] // 80 
                           
                            if move(board, board.board[row][col],end_row,end_col) == True:
                                    board.turn = -1
                                    print('score',board.score)
                            board.draw_board(WIN)
                            board.draw_pieces(WIN)
                            select = False



                if is_game_over(board) != False:
                    if is_game_over(board) == 'Red':
                        img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/player_win.png')), (90, 90))
                        WIN.blit(img, (350,350))
                    else:
                        img = pygame.transform.scale(pygame.image.load(os.path.join('Assests/player_lose.png')), (90, 90))
                        WIN.blit(img, (350,350))
                    playing = False
                

                pygame.display.update()
    pygame.quit()
main()