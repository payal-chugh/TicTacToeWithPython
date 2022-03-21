import random
def display(board):
  print(' '+board[0]+' | ' +board[1]+' | ' +board[2])
  print('````````````')
  print(' '+board[3]+' | ' +board[4]+' | ' +board[5])
  print('````````````')
  print(' '+board[6]+' | ' +board[7]+' | ' +board[8])


def marker_input():
  marker = ''
  while marker not in ['X','0']:
    marker = input('Player 1: Do you want to be X or 0 ').upper()
  if marker == 'X':
    return ('X','0')
  else:
    return ('0','X')


def place_marker(board, marker, position):
  board[position] = marker
  return board

def input_position(turn, board):
  position = 'Wrong'
  while position not in range(0,9) or not is_blank(position, board) :
    position = input(turn + ' Please enter position(0 to 8) ')
    if (not position.isdigit()) or (int(position) not in range(0,9)):
      print("Enter a valid position ")
    else:
      return int(position)
    

def is_blank(position, board):
  return board[position] == '-'

def won(board, marker):
  return(
    (board[0] == board[1] == board[2] == marker) or
    (board[3] == board[4] == board[5] == marker) or
    (board[6] == board[7] == board[8] == marker) or
    (board[0] == board[3] == board[6] == marker) or
    (board[1] == board[4] == board[7] == marker) or
    (board[2] == board[5] == board[8] == marker) or
    (board[0] == board[4] == board[8] == marker) or
    (board[2] == board[4] == board[6] == marker)
  )

def first_chance():
  if random.randint(0,1) == 0:
    return 'Player 1'
  else:
    return 'Player 2'

def full_checked(board):
  return '-' not in set(board)
  
print('Welcome to Tic Tac Toe!')
game_on = 'WRONG'
while game_on not in ['Y','N']:
    game_on = input("Are you ready for the game? Press Y or N ").upper()
    if game_on == 'N':
      break
    else:
        board =['-']*9
        display(board)
        marker1, marker2 = marker_input()
        turn = first_chance()
        print(turn+" will go first")
        while not won or not full_checked(board):
          if turn =="Player 1":
            position = input_position(turn, board)
            board = place_marker(board, marker1, position)
            display(board)
            if won(board, marker1):
              print("Congratulation Player 1! You have won the Game")
              break
            elif full_checked(board):
              print("Game DRAW!")
              break
            turn = "Player 2"
          elif turn =="Player 2":
            position = input_position(turn, board)
            board = place_marker(board, marker2, position)
            display(board)
            if won(board, marker1):
              print("Congratulation Player 2! You have won the Game")
              break
            elif full_checked(board):
              print("Game DRAW!")
              break
            turn = "Player 1"
            
          
