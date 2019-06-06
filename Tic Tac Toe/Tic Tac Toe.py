#TaskOne
import time
import os
def printBoard() :
    os.system('cls||clear')
    print("Tic Tac Toe")
    print( '\n -----')
    print( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print( ' -----')
    print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print( ' -----')
    print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print( ' -----\n')
Play=True
while(Play):
    choices = []*9
    for x in range (0, 9) :
        choices.append(str(x + 1))
    p1turn = True
    winner = False
    while (not winner):
        printBoard()
        if p1turn :
            print( "Player 1:")
        else :
            print( "Player 2:")
        try:
            choice = int(input("Enter A Choice:"))
        except:
            print("Please Re-Enter Choice!")
            continue
        if(choice<0 or choice>10):
            print("Please Enter a Valid Position")
            continue
        if (choices[choice - 1] == 'X' or choices [choice-1] == 'O'):
            print("Pre-Occupied Position")
            continue
        if p1turn :
            choices[choice - 1] = 'X'
        else :
            choices[choice - 1] = 'O'
        p1turn = not p1turn

        for x in range (0, 3) :
            y = x * 3
            if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
                winner = True
                printBoard()
            if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
                winner = True
                printBoard()

        if((choices[0] == choices[4] and choices[0] == choices[8]) or 
           (choices[2] == choices[4] and choices[4] == choices[6])) :
            winner = True
            printBoard()
    if(winner is True):
            print ("Player " + str(int(p1turn + 1)) + " Wins!\n")
    else:
            print("Draw!")
    c=1
    time.sleep(0.5)
    while(c):
        Playd=input("Do You Want to Play Anymore?(Y/N):")
        if(Playd is 'Y' or Playd is 'y'):
            c=0
            os.system('cls||clear')
        elif (Playd is 'N' or Playd is 'n'):
            c=0
            Play=False
        else:
            print("Error:Re-Enter the choice!")
    
