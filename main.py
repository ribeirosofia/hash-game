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