def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def enter_move(board):
    ok = False  
    while not ok:
        move = input("Digite seu movimento: ")
        ok = len(move) == 1 and move >= '1' and move <= '9'
        if not ok:
            print("Má jogada – repita sua entrada!")
            continue
        move = int(move) - 1 	
        row = move // 3 	
        col = move % 3		
        sign = board[row][col]  
        ok = sign not in ['O', 'X']
        if not ok:  
            print("Campo já ocupado – repita sua entrada!")
            continue
    board[row][col] = 'O' 

def make_list_of_free_fields(board):
    free = []
    for row in range(3):  
      for col in range(3): 
           if board[row][col] not in ['O', 'X']:  
                   free.append((row, col))
    return free
    
def victory_for(board, sgn):
    if sgn == "X":  
        who = 'me'  
    elif sgn == "O":  
        who = 'you'  
    else:
        who = None  
    cross1 = cross2 = True
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:  # verifica a linha rc
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:  # verifica a coluna rc
            return who
        if board[rc][rc] != sgn:  
            cross1 = False
        if board[2 - rc][2 - rc] != sgn:  
            cross2 = False
        if cross1 or cross2:
            return who
        return None
