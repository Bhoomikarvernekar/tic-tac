# Simple Tic-Tac-Toe Game (Terminal Version)

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for pattern in win_patterns:
        if (board[pattern[0]] == player and
                board[pattern[1]] == player and
                board[pattern[2]] == player):
            return True
    return False


# Initial Board
board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

current_player = "X"
moves = 0

print("=" * 35)
print("      TIC - TAC - TOE")
print("=" * 35)
print("Choose a position from 1 to 9")
print("Type 'q' anytime to quit.\n")

print_board(board)

# Game Loop
while True:

    choice = input(f"Player {current_player}, enter position (1-9) or 'q': ").strip()

    if choice.lower() == "q":
        print("\n👋 Game Quit Successfully!")
        break

    if not choice.isdigit():
        print("❌ Please enter a valid number.")
        continue

    position = int(choice)

    if position < 1 or position > 9:
        print("❌ Position must be between 1 and 9.")
        continue

    if board[position - 1] in ["X", "O"]:
        print("❌ Position already taken. Try another one.")
        continue

    board[position - 1] = current_player
    moves += 1

    # Show current game state after every move
    print_board(board)

    # Check Winner
    if check_winner(board, current_player):
        print(f"🎉 Congratulations! Winner is '{current_player}' 🏆")
        break

    # Check Draw
    if moves == 9:
        print("🤝 It's a Draw!")
        break

    # Switch Player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"