signs = ("X","O")
grid = {"tleft":0, "tcenter":1, "tright":2,"mleft":3, "mcenter":4, "mright":5,"bleft":6, "bcenter":7, "bright":8}
positions = ["tleft", "tcenter", "tright", "mleft", "mcenter", "mright", "bleft", "bcenter", "bright"]
win_O = ["O","O","O"]
win_X = ["X","X","X"]

def display_table(t):
    """a simple function to display a tic tac toe table"""
    print(str(" | ".join(t[0:3])))
    print(str(" | ".join(t[3:6])))
    print(str(" | ".join(t[6:])))

def picker(sign, table):
    '''
    function takes a sign and a tic tac toe table as arguments
    and alters the position choosen by user
    '''
    while True:
        pos = str(input("Choose a position: "))
        change = grid[pos]
        if table[change] == ".":
            table[change] = str(sign)
            return
        else:
            print('Chosen position is already taken')

def checker(table):
    '''
    !!!UNFINISHED!!!

    function takes a tic tac toe table as an argument and checks for winning combinations
    '''
    for i in range(3):          #a loop to check horizontal winning combinations
            if table[i*3:i*3+3] == win_X:
                print("X's won!!!\n")
                display_table(table)
                return True
            elif table[i*3:i*3+3] == win_O:
                print("O's won!!!\n")
                display_table(table)
                return True

    for i in range(3):          #a loop to check the vertical winning combinations
        if table[i::3] == win_X:
            print("X's won!!!\n")
            display_table(table)
            return True
        elif table[i::3] == win_O:
            print("O's won!!!\n")
            display_table(table)
            return True

    if table[2:7:2] == win_X:
        print("X's won!!!\n")
        display_table(table)
        return True
    elif table[2:7:2] == win_O:
        print("X's won!!!\n")
        display_table(table)
        return True

    if table[0:9:4] == win_X:
        print("X's won!!!\n")
        display_table(table)
        return True
    elif table[0:9:4] == win_O:
        print("X's won!!!\n")
        display_table(table)
        return True

def mainloop():
    '''main function of the tic tac toe game'''
    table = [".",".",".",".",".",".",".",".","."]   #list representation of tic tac toe table
    win = False
    print('You can use any of given names to place your next move.\n')
    display_table(positions)
    print('\n')
    print('Who moves first, X or O? \n')
    first = str(input()).upper()
    print(first)
    print("First move is by " + first + "'s\n")
    move = 1               #assigns the starting move for rotation between signs
    if first == 'X':
        second = 'O'
    elif first == 'O':
        second = 'X'
    else:
        raise ValueError('THERE IS NO OPTION FOR THAT SIGN')

    while win == False: #loop runs till checker function returns True
        display_table(table)
        print('\n')
        if move%2 == 0:
            print("It's " + second + "'s move\n")
            picker(second, table)
            move += 1
            if checker(table) == True:
                win = True
        else:
            print("It's " + first + "'s move\n")
            picker(first, table)
            move += 1
            if checker(table) == True:
                win = True

mainloop()