import math

# Constants for players
HUMAN = "X"
AI = "O"
EMPTY = " "

# Function to initialize the board
def create_board():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if the board is full
def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Function to check for a winner
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None

# Minimax function with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == AI:
        return 10 - depth
    elif winner == HUMAN:
        return depth - 10
    elif is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for AI
def best_move(board):
    best_val = -math.inf
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_val = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = EMPTY

                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)

    return move

# Function to play the game
def play_game():
    board = create_board()
    print("Tic-Tac-Toe: You (X) vs AI (O)")
    print_board(board)

    while True:
        # Human player's move
        row, col = map(int, input("Enter your move (row and column: 0 1 2): ").split())
        if board[row][col] != EMPTY:
            print("Invalid move. Try again.")
            continue
        board[row][col] = HUMAN

        print_board(board)
        if check_winner(board):
            print("You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        # AI's move
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = AI

        print("AI's move:")
        print_board(board)

        if check_winner(board):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
