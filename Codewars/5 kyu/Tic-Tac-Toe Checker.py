def is_solved(board):
    
    if type(board) != type([]):
        
        return -1
    else:
    
        # Verificar si X (1) ganó

        # Horizontal 1
        if board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1:

            return 1
        # Horizontal 2
        elif board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1:

            return 1
        # Horizontal 3
        elif board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1:

            return 1
        # Vertical 1
        elif board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:

            return 1
        # Vertical 2
        elif board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:

            return 1
        # Vertical 3
        elif board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:

            return 1
        # Diagonal 1
        elif board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:

            return 1
        # Diagonal 2
        elif board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:

            return 1



        # Verificar si O (2) ganó

        # Horizontal 1
        if board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2:

            return 2
        # Horizontal 2
        elif board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2:

            return 2
        # Horizontal 3
        elif board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2:

            return 2
        # Vertical 1
        elif board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:

            return 2
        # Vertical 2
        elif board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:

            return 2
        # Vertical 3
        elif board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2:

            return 2
        # Diagonal 1
        elif board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:

            return 2
        # Diagonal 2
        elif board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:

            return 2

        # Verificar si no es un empate

        if 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:

            return 0

        else:

            return -1