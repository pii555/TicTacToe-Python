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

#Test



#Set up, only initialize once
test_board = ["-","-","-","-","-","-","-","-","-","-"]
display(test_board)
player_name1, player_marker1, player_name2, player_marker2 = playerinput()
move = randomstart()
print(move)