#Imports time for setting a delay and random for randomizing player initializing
import random, time

#Creates the initial display of the board and refreshes the board
def display(board):
    print ("\n"* 100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

#1 player game input
def oneplayerinput():
    player_name1 = input("What is your name?: ")
    marker = input("%s, would you like to be X or O: " %player_name1)
    marker = marker.upper()

    #Loops until a valid choice is made
    while marker != "X" and marker != "O":
        marker = input("Invalid input, choose again %s. Would you like to be X or O: " %player_name1)
        marker = marker.upper()
    player_marker_1 = marker
    if player_marker_1 == "X":
        computer_marker = "O"
    else:
        computer_marker = "X"
    return (player_name1,player_marker_1,computer_marker)

#Users inputs their name and the respective piece they would like to play in the game
def twoplayerinput():
    player_name1 = input("What is the name of the 1st player?: ")
    player_name2 = input("What is the name of the 2nd player?: ")
    marker = input("%s, would you like to be X or O: " %player_name1)
    marker = marker.upper()

    #Checks if valid character was inputted
    while marker != "X" and marker != "O":
        marker = input("Invalid input, choose again %s. Would you like to be X or O: " %player_name1)
        marker = marker.upper()
    player_marker1 = marker
    if player_marker1 == "X":
        player_marker2 = "O"
    else:
        player_marker2 = "X"
    return (player_name1,player_marker1,player_name2,player_marker2)


#Randomly decide who goes first
def randomstart(player1,player2):
    print("Randomizing who makes the 1st move...")
    num = random.randint(0,1)
    time.sleep(1)
    if num == 1:
        print ("%s will start the game" %player1)
        return(1)
    else:
        print ("%s will start the game" %player2)
        return(2)

#Checks and returns true if space is free
def freespace(board,move):
    return board[move] == " "

#Lets player type where to place their move
def playermove(board,name):
    move = ""
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not freespace(board, int(move)):
        print("%s, What's your move? (1-9)" %name)
        move = input()
    return int(move)

#Makes the move
def makemove(board,player,move):
    board[move] = player

#Switches player's turn after each move
def switchturn(turn):
    if turn == 1:
        return 2
    else:
        return 1

#Checks horizontal, vertical and diagonal wins from a player
def checkwinner(board,playermarker):
#Checking horizontal
    if ((board[7] == playermarker and board[8] == playermarker and board[9] == playermarker) or
    (board[4] == playermarker and board[5] == playermarker and board[6] == playermarker) or
    (board[1] == playermarker and board[2] == playermarker and board[3] == playermarker) or
#Checking Vertical
    (board[7] == playermarker and board[4] == playermarker and board[1] == playermarker) or
    (board[8] == playermarker and board[5] == playermarker and board[2] == playermarker) or
    (board[9] == playermarker and board[6] == playermarker and board[3] == playermarker) or
#Checking Diagonal
    (board[1] == playermarker and board[5] == playermarker and board[9] == playermarker) or
    (board[7] == playermarker and board[5] == playermarker and board[3] == playermarker)):
        return True
    else:
        pass

#Checks to see if board is full, returns true if it is, false if it isn't
def boardfull(board):
    for i in range(1,10):
        if freespace(board,i):
            return False
    return True

#Asks players if they'd like to play again
def playagain():
    decision = input("Would you like to play again?: " )
    decision = decision.lower()
    if decision == "yes":
        return True
    else:
        return False

#Resets the board of existing values
def newgame(board):
    for i in range(1,10):
        board[i] = " "
    return True

#Allows for choice of facing another player or vs a computer
def selectgametype():
    gamechoice = input("Would you like to play vs a player or a computer? " )
    gamechoice = gamechoice.lower()
    if gamechoice == "player":
        return 1
    elif gamechoice == "computer" or gamechoice == "cpu":
        return 2 

    #Loops until a valid choice is made
    while gamechoice != "cpu" and gamechoice != "computer" and gamechoice != "player":
        gamechoice = input("Invalid input, choose again would you like to play vs a player or a computer? ")
        gamechoice = gamechoice.lower()
        if gamechoice == "player":
            return 1
        elif gamechoice == "computer" or gamechoice == "cpu":
            return 2

#Returns a valid move from the list to the board
def randomcomputermove(board,movelist):
    possibleMoves = []
    for i in movelist:
        if freespace(board,i):
            possibleMoves.append(i)
    
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

#Creates a copy of the board the Computer will use to manage moves. Without, it makes consecutive moves
def copyboard(board):
    copy = []
    for i in board:
        copy.append(i)
    return copy


#Logic for computers move selection
def computermove(board,computer_marker):
    #sets player marker variable to analyze the board
    if computer_marker == "X":
        player_marker = "O"
    else:
        player_marker = "X"

    #ALGORITHM
    
    #Checking first if computer's next move will win the game
    for i in range (1,10):
        copy = copyboard(board)
        if freespace(copy,i):
            makemove(copy,computer_marker,i)
            if checkwinner(copy,computer_marker) == True:
                return i

    #Check if player will win next turn
    for i in range (1,10):
        copy = copyboard(board)
        if freespace(copy, i):
            makemove(copy,player_marker,i)
            if checkwinner(copy, player_marker) == True:
                return i

    #Takes a random available corner square
    move = randomcomputermove(board,[1,3,7,9])
    if move != None:
        return move

    #Take the middle square if available
    if freespace(board,5) == " ":
        return 5

    #Takes a random available side square
    move = randomcomputermove(board,[2,4,6,8])
    if move != None:
        return move


def main():
    #Set up, only initialize once
    board = [" "] * 10
    gamechoice = selectgametype()
    gamestatus = True
    
    #Logic for choosing game type
    if gamechoice == 1:
        player_name1, player_marker1, player_name2, player_marker2 = twoplayerinput()
        turn = randomstart(player_name1,player_name2)
    if gamechoice == 2:
        player_name1, player_marker1, computer_marker = oneplayerinput()
        turn = randomstart(player_name1,"Computer")

    print ("The game will commence!")
    time.sleep(3)

    #Game loops while status is true
    while gamestatus == True:

        #Logic for player 1
        if turn == 1:
            display(board)
            move = playermove(board,player_name1)
            makemove(board,player_marker1,move)
            turn = 2
            if checkwinner(board,player_marker1) == True:
                display(board)
                print("%s has won the game!" %player_name1)
                gamestatus = False

            elif boardfull(board):
                display(board)
                print("The game is a draw")
                gamestatus = False

        #logic for player 2
        elif turn == 2 and gamechoice == 1:
            display(board)
            move = playermove(board,player_name2)
            makemove(board,player_marker2,move)
            turn = 1
            if checkwinner(board,player_marker2) == True:
                display(board)
                print("%s has won the game!" %player_name2)
                gamestatus = False
           
            elif boardfull(board):
                display(board)
                print("The game is a draw")
                gamestatus = False

        #logic for computer turn
        elif turn == 2 and gamechoice == 2:
            display(board)
            move = computermove(board,computer_marker)
            makemove(board,computer_marker,move)
            turn = 1
            if checkwinner(board,computer_marker) == True:
                display(board)
                print("Computer has won the game!" )
                gamestatus = False
           
            elif boardfull(board):
                display(board)
                print("The game is a draw")
                gamestatus = False


        #Checks if game has ended and if the players wanted to play again
        if gamestatus == False and playagain() == True:
            gamestatus = newgame(board)

main()
 


