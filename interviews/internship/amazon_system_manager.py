# input: (0,1)
# output: string that shows winner or tie or collects the next input

def tic_tac_toe(input, player):
  # player 1 --> x
  # input_coordinates (0, 0)

  matrix = [["","",""], ["","",""], ["","",""]]
  input_counter = 0
  while game_running:
    if player == "player1":
      play = "X"
    elif player == "player2":
      play = "O"
      
    input_counter += 1
    if input_counter > 9:
      game_running == False
      output = "It was a tie!"
      break

    row = input_coordinates[0]
    column = input_coordinates[1]
    
    matrix[row][column] = play
    no_winner = False
    # looking across a row
    for spot in matrix[row]:
      pass