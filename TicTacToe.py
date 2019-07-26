import random

#Creates the initial display of the board and refreshes the board
def display(board):
    print ("\n"* 100)
    print (board[7] + '|' + board[8] + "|" + board[9])
    print (board[4] + '|' + board[5] + "|" + board[6])
    print (board[1] + '|' + board[2] + "|" + board[3])

#Users inputs their name and the respective piece they would like to play in the game
def playerinput():
    player_name1 = input("What is the name of the 1st player?: ")
    player_name2 = input("What is the name of the 2nd player?: ")

    marker = input("%s, would you like to be X or O: " %player_name1)
    marker = marker.upper()
    while marker != "X" and marker != "O":
        marker = input("Invalid input, choose again %s. Would you like to be X or O: " %player_name1)
        marker = marker.upper()
    player_marker_1 = marker
    if player_marker_1 == "X":
        player_marker_2 = "O"
    else:
        player_marker_2 = "X"
    return (player_name1,player_marker_1,player_name2,player_marker_2)


#Randomly decide who goes first
def randomstart():
    print("Randomizing who makes the 1st move...")
    num = random.randint(0,1)
    if num == 1:
        print ("{} will start the game".format(player_name1))
        return(1)
    else:
        print ("{} will start the game".format(player_name2))
        return(0)

#Checks and returns true if space is free
def freespace(board,move):
    return board[move] == " "

#Lets player type where to place their move
def playermove(board):
    move = ""
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not freespace(board, int(move)):
        print("What's your move? (1-9)")
        move = input()
    return int(move)

#Makes the move
def makemove(board,player,move):
    board[move] = player

#Checks horizontal, vertical and diagonal wins from a player
def checkwinner(board,player):
#Checking horizontal
    if ((board[7] == player and board[8] == player and board[9] == player) or
    (board[4] == player and board[5] == player and board[6] == player) or
    (board[1] == player and board[2] == player and board[3] == player) or
#Checking Vertical
    (board[7] == player and board[4] == player and board[1] == player) or
    (board[8] == player and board[5] == player and board[2] == player) or
    (board[9] == player and board[6] == player and board[3] == player) or
#Checking Diagonal
    (board[1] == player and board[5] == player and board[9] == player) or
    (board[7] == player and board[5] == player and board[3] == player)):
        return True
    else:
        pass

#Checks to see if board is full, returns true if it is, false if it isn't
def boardfull(board):
    for i in range(1,10):
        if freespace(board,i):
            return False
    return True





#Set up, only initialize once
board = [" "] * 10
display(board)
player_name1, player_marker1, player_name2, player_marker2 = playerinput()
turn = randomstart()
 



board[1] = player_marker1 
board[5] = player_marker1
board[9] = player_marker1
print(checkwinner(board,player_marker1))

