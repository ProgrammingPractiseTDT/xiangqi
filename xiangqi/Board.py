import pygame
from .constrant import SQUARE_SIZE, COLS, ROWS, BROWN, YELLOW, BOARD_SIZE, BLACK
from .Pieces import *
import os, copy
pygame.init()
#heuristic
heuristic = {'general': 100, 'chariot':9, 'horse':4, 'cannon' :6, 'soldier':1, 'elephant': 2, 'advisor':2}
BLACK_POS = []
BLACK_POS.append(chariot('chariot',0,0,'black'))
BLACK_POS.append(horse('horse',0,1,'black'))
BLACK_POS.append(elephant('elephant',0,2,'black'))
BLACK_POS.append(advisor('advisor',0,3,'black'))
BLACK_POS.append(general('general',0,4,'black'))
BLACK_POS.append(advisor('advisor',0,5,'black'))
BLACK_POS.append(elephant('elephant',0,6,'black'))
BLACK_POS.append(horse('horse',0,7,'black'))
BLACK_POS.append(chariot('chariot',0,8,'black'))
BLACK_POS.append(cannon('cannon',2,1,'black'))
BLACK_POS.append(cannon('cannon',2,7,'black'))
for i in range(0,9,2):
    BLACK_POS.append(soldier('soldier',3,i,'black'))


RED_POS = []
RED_POS.append(chariot('chariot',9,8,'red'))
RED_POS.append(horse('horse',9,7,'red'))
RED_POS.append(elephant('elephant',9,6,'red'))
RED_POS.append(advisor('advisor',9,5,'red'))
RED_POS.append(general('general',9,4,'red'))
RED_POS.append(advisor('advisor',9,3,'red'))
RED_POS.append(elephant('elephant',9,2,'red'))
RED_POS.append(horse('horse',9,1,'red'))
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
        self.turn = 1
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
        # self.horse_constraint = [self.board[0][1], self.board[0][7], self.board[9][1], self.board[9][7]]
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
    def draw_circle(self,y,x, sur):
      x = 40 - PADDING//2 + (SQUARE_SIZE * x)
      y = 40 - PADDING//2 + (SQUARE_SIZE * y)

      img  = pygame.transform.scale(pygame.image.load(os.path.join('Assests/circle.png')), (PADDING, PADDING))
      sur.blit(img, (x,y))





#function moving and checking
def unit_move(board, piece, new_row, new_col, capture):
                #prepare calculate score
                if capture == True:
                    captured_piece = board.board[new_row][new_col]
                    if piece.color == 'black':
                       score = -heuristic[captured_piece.name]
                    else:
                       score = heuristic[captured_piece.name]
                
                movable = False
                capturable = False




                row_piece, col_piece = piece.row, piece.col
                if piece.name == 'horse':#check if its a horse capture must follow rule
                    #oke    
                    #check if the horse is blocked
                            for point in cross_of_point(row_piece,col_piece):#check around the horse if there another piece
                                if board.board[point[0]][point[1]] !=None:
                                    if (new_row, new_col)  in diagonal_of_point(point[0], point[1]):
                                        return False
                        
                            else:   
                                    
                                    movable = True
                                    capturable = True


                elif piece.name == 'cannon' or piece.name == 'chariot':
                            count = 0
                            if new_row == row_piece: #if new move space in the same row
                                step = new_col - col_piece
                                if step > 0:
                                    step = 1
                                elif step < 0:
                                    step = -1
                                for i in range(col_piece+step, new_col, step):
                                    if board.board[row_piece][i] !=None:
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
                            elif new_col == col_piece: #if new move space in the same column
                                step = new_row - row_piece
                                if step > 0:
                                    step = 1
                                if step < 0:
                                    step = -1
                                
                                for i in range(row_piece+step, new_row, step):
                                    if board.board[i][col_piece] !=None:
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
                                if board.board[row_piece+ row_b][col_piece + col_b] == None:
                                    
                                    movable = True
                                    capturable = True
                                else:
                                    return False
                else:
                                   #for soldier and adviosr and general
                                   movable = True
                                   capturable = True
                
                if capture == True and capturable == True:
                                    board.board[new_row][new_col] = None
                                    del captured_piece
                                    board.board[new_row][new_col] = piece
                                    board.board[row_piece][col_piece] = None
                                    piece.row = new_row
                                    piece.col = new_col
                                    board.score += score
                                    return True
                if movable == True and capture == False:
                                    #move piece in free space, just change it location
                                    board.board[new_row][new_col] = piece
                                    board.board[row_piece][col_piece] = None
                                    piece.row = new_row
                                    piece.col = new_col
                                    return True
                return False
            
                            
                                  
                    

    
def move(board,piece, new_row, new_col):
        if piece != None:

            if (new_row, new_col) in piece.possible_moves():
                    if board.board[new_row][new_col] == None:
                        return unit_move(board,piece, new_row, new_col, capture = False)

                    if board.board[new_row][new_col].color == piece.color:
                        return False
                    elif board.board[new_row][new_col].color != piece.color:
                        return unit_move(board,piece, new_row, new_col, capture = True)
        
        return False
    


    

    
def is_game_over(board):
        if board.score >= 100:
            return 'Red'
        if board.score <= -100:
            return 'Black'
        
        return False





def next_states(state):
    output = []
    if state.turn == 1:
        
        for piece in state.reds:
            # print('piece', piece.name)
            # print('oka', piece.possible_moves())
            row_piece, col_piece = piece.row, piece.col
            for possible_move in piece.possible_moves():
                new_state = copy.deepcopy(state)
                # print('aka',type(new_state))
                
                if move(new_state , piece , possible_move[0], possible_move[1]) == True:
                    new_state.turn = -1
                    new_state.nextMove = (row_piece, col_piece,possible_move[0], possible_move[1])
                    output.append(new_state)
    if state.turn == -1:
        for piece in state.blacks:
            # print('piece', piece.name)
            row_piece, col_piece = piece.row, piece.col
            for possible_move in piece.possible_moves():
                
                new_state = copy.deepcopy(state)
                # print('aka',type(new_state))
                
                if move(new_state , new_state.board[row_piece][col_piece] , possible_move[0], possible_move[1]) == True:
                    new_state.turn = 1
                    new_state.nextMove = (row_piece, col_piece,possible_move[0], possible_move[1])
                    
                    
                    output.append(new_state)
    # for i in output:
    #    print('score for node: ', i.nextMove,i.score)
    return output

def minimax(state, curr_depth, max_depth, alpha, beta):
             
             #base case: target depth reached
             if curr_depth == max_depth  or is_game_over(state) != False: 
                 return state.score
             
             if state.turn == 1: #maxturn
                 bestVal = -200
                 for next_state in next_states(state):
                    #  new_node = minimax( next_state, curr_depth + 1,  max_depth )
                    #  if new_node > best:
                    #      best = new_node
                    #  L.append(new_node)
                    #  print('L lenght', len(L))
                    value = minimax(next_state, curr_depth+1, max_depth, alpha, beta)
                    bestVal = max(bestVal, value)
                    alpha = max(alpha, bestVal)
                    if beta<= alpha:
                        break
                 return bestVal

    
             
             elif state.turn == -1:#min turn
                 bestVal = 200
                 for next_state in next_states(state):
                    #  new_node = minimax( next_state, curr_depth + 1,  max_depth )
                    #  if new_node > best:
                    #      best = new_node
                    #  L.append(new_node)
                    #  print('L lenght', len(L))
                    value = minimax(next_state, curr_depth+1, max_depth, alpha, beta)
                    bestVal = min(bestVal, value)
                    alpha = min(alpha, bestVal)
                    if beta<= alpha:
                        break
                 return bestVal
def bot_decide(board):
        class h_board:
            def __init__(self):
                self.board = [[None for _ in range(COLS+1) ] for _ in range(ROWS+1) ]
                self.turn = board.turn
                self.score = board.score
                self.nextMove = None
                self.blacks = []
                self.reds = []
                for black_piece in BLACK_POS:
                      
                      new = h_piece(black_piece.name, black_piece.row, black_piece.col, 'black')
                      self.board[black_piece.row][black_piece.col] = new
                      self.blacks.append(new)
                    #   print(new.name, new.possible_moves())
                for red_piece in RED_POS:
                      new  = h_piece(red_piece.name, red_piece.row, red_piece.col, 'red')
                      self.board[red_piece.row][red_piece.col] = new
                      self.reds.append(new)  
                      
        
        
        
        state = h_board()
        best_for_bot = 200
        nextMove = None
        for next_state in next_states(state):
                     hypothesis = minimax(next_state,0, 1, -200, 200)
                     if  hypothesis <= best_for_bot:
                          best_for_bot = hypothesis
                          nextMove = next_state.nextMove
        
        return nextMove

        
        
        



            
             
        


        

