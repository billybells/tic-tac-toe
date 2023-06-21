import random
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_board():
  print("-------------")
  print(f"| {board[0]} | {board[1]} | {board[2]} |")
  print("-------------")
  print(f"| {board[3]} | {board[4]} | {board[5]} |")
  print("-------------")
  print(f"| {board[6]} | {board[7]} | {board[8]} |")
  print("-------------")

def is_valid(user_move):
  valid = True
  if user_move <= 0 or user_move > 9:
    valid = False
  elif board[user_move - 1] != user_move:
    valid = False
  return valid

def is_winner(side, b):
  winner = False
  if (b[0] == b[1] == b[2] == side) or \
     (b[3] == b[4] == b[5] == side) or \
     (b[6] == b[7] == b[8] == side) or \
     (b[0] == b[3] == b[6] == side) or \
     (b[1] == b[4] == b[7] == side) or \
     (b[2] == b[5] == b[8] == side) or \
     (b[0] == b[4] == b[8] == side) or \
     (b[2] == b[4] == b[6] == side):
       winner = True
  return winner

def reset_board():
  global board
  board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_valid_moves():
  valid_moves = []
  position = 1
  for square in board:
    if square == position:
      valid_moves.append(square)
    position += 1
  return valid_moves

def make_random_ai_move():
  valid_moves = get_valid_moves()
  if len(valid_moves) > 0:
    rand = random.randint(0, len(valid_moves) - 1)
    move = valid_moves[rand]
    board[move - 1] = 'O'
    print(f'O picks {move}.')

def make_smart_ai_move():
  valid_moves = get_valid_moves()
  # if any move will win, let's take it
  for possible_move in valid_moves:
    possible_board = board.copy()
    possible_board[possible_move - 1] = 'O'
    if (is_winner('O', possible_board)):
      board[possible_move -1] = 'O'
      return
  # we don't have a winning move.  Does the player?
  for possible_move in valid_moves:
    possible_board = board.copy()
    possible_board[possible_move - 1] = 'X'
    if (is_winner('X', possible_board)):
      board[possible_move -1] = 'O'
      return
  # no winning moves yet, pick randomly
  make_random_ai_move()

def is_board_full():
  valid_moves = get_valid_moves()
  if len(valid_moves) == 0:
    return True
  else:
    return False


print("Let's play tic tac toe!")
user_input = None
print_board()
while (True):
  print("X: Pick a move (1-9) or enter 'bye' to quit")
  user_input = input()
  if user_input == 'bye':
    print("Goodbye!")
    break
  else:
    # check for integer
    try:
      user_move = int(user_input)
    except ValueError:
      print(f"Invalid input: {user_input}.")
      continue
    if not is_valid(user_move):
      print(f"Invalid move: {user_input}")
      continue
    board[user_move -1] = 'X'
    if is_winner('X', board):
      print_board()
      print("X wins!  Let's go again.")
      reset_board()
    else:
      make_random_ai_move()
      # make_smart_ai_move()
      if is_winner('O', board):
        print_board()
        print("Oh no!  O won.  Let's go again.")
        reset_board()
    if is_board_full():
      print_board()
      print("DRAW!  Let's go again!")
      reset_board()
    print_board()
