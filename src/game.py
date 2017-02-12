# -*-coding:utf-8 -*

import os
from collections import namedtuple

Player = namedtuple("Player", ("name", "mark"))

players = (
  Player(name = "A", mark = "X"),
  Player(name = "B", mark = "O"),
)

current_player = 0

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def show(board):
  """
  Format the list and print it as a board 
  """
  index = 0
  
  while index <= len(board) - 3:
    print("+-+-+-+")
    print("|{}".format(board[index]) + "|{}".format(board[index + 1]) + "|{}".format(board[index + 2]) + "|")
    index += 3

  print("+-+-+-+\n")

def check_game(board, player):
  """
  Determine if the current player is the winner
  """
  check_board = "".join(str(box) for box in board)

  # Define some constants to use as check

  row1 = board[0:3]
  row2 = check_board[3:6]
  row3 = check_board[6:9]
  column1 = check_board[0] + check_board[3] + check_board[6]
  column2 = check_board[1] + check_board[4] + check_board[7]
  column3 = check_board[2] + check_board[5] + check_board[8]
  diagonalA = check_board[0] + check_board[4] + check_board[8]
  diagonalB = check_board[2] + check_board[4] + check_board[6]

  check_mark = 3 * player.mark

  if row1 == check_mark or row2 == check_mark or row3 == check_mark:
    return True
  if column1 == check_mark or column2 == check_mark or column3 == check_mark:
    return True
  if diagonalA == check_mark or diagonalB == check_mark:
    return True
  else:
    return False

def check_full(board):
  """
  Determine if the game is still playable

  When we cannot convert any box into an integer the game is not playable
  """
  for box in board:
    try:
      int(box)
    except ValueError:
      continue
    else:
      return False

  return True   

# Welcome screen

print("TIC TAC TOE")
print("___________\n")
show(board)

run = True    

while run:
  player = players[current_player]

  player_move = input("Player {}: ".format(player.name))

  try:
    position = int(player_move) - 1

    if board[position] == player_move:
      board[position] = player.mark
  except (ValueError, IndexError):
    print("\nEnter a number between 1 and 9\n")
    continue

  show(board)

  if check_game(board, player):
    print("Player {}".format(player.name) + " won !")
    run = False
  elif check_full(board):
    print("Game over !")
    run = False
  
  current_player = (current_player + 1) % len(players)

os.system("pause")