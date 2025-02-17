import math

# Initialize empty board
def create_board():
    return [['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']]

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
    print("\n")

# Function to check if moves are left
def is_moves_left(board):
    for row in board:
        if '_' in row:
            return True
    return False

# Function to evaluate board state
def evaluate(board):
    # Check rows and columns for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '_':
            return 10 if board[i][0] == 'X' else -10
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '_':
            return 10 if board[0][i] == 'X' else -10

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        return 10 if board[0][0] == 'X' else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        return 10 if board[0][2] == 'X' else -10

    return 0  # No winner yet

# Minimax function to find best move
def minimax(board, depth, is_max):
    score = evaluate(board)

    # Return the score if terminal state is reached
    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0  # Draw

    if is_max:  # Maximizing Player (AI)
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'  # AI Move
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = '_'  # Undo move
        return best

    else:  # Minimizing Player (Human)
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'  # Human Move
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = '_'  # Undo move
        return best

# Function to find the best move for AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'  # AI Move
                move_val = minimax(board, 0, False)
                board[i][j] = '_'  # Undo move

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

# Function to check if the game is over
def check_game_over(board):
    score = evaluate(board)
    if score == 10:
        print("AI (X) Wins! 🎉")
        return True
    elif score == -10:
        print("Human (O) Wins! 🎉")
        return True
    elif not is_moves_left(board):
        print("It's a Draw! 🤝")
        return True
    return False

# Function to play the game
def play_tic_tac_toe():
    board = create_board()
    print("Welcome to Tic-Tac-Toe! You are 'O', AI is 'X'")
    print_board(board)

    while True:
        # Human player's move
        row, col = -1, -1
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column, 0-2): ").split())
                if board[row][col] == '_':
                    board[row][col] = 'O'
                    break
                else:
                    print("Cell is already occupied! Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Enter row and column between 0 and 2.")

        print_board(board)
        if check_game_over(board):
            break

        # AI's move
        print("AI is making a move...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'
        print_board(board)

        if check_game_over(board):
            break

# Start the game
play_tic_tac_toe()
