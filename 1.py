board_no=[]
board=[]
def boardSize():
    n=3
    for i in range(n**2):
        board_no.append(i)
        board.append(i)

def drawBoard():
    for number in board_no:
        if (number+1)%3 == 0:
            print(board[number],end="\n")
        else:
            print(board[number],end="")
    

def move(n,letter):
    board[n] = letter

def player1():
    n=int(input("X--> "))
    letter = "X"
    move(n,letter)
    drawBoard()
    if winner(letter):
        print("Winner: " + letter)
        exit()
    
        
    
def player2():
    n=int(input("O--> "))
    letter = "O"
    move(n,letter)
    drawBoard()
    if winner(letter):
        print("Winner: " + letter)
        exit()
    

def winner(le):
    return ((board[0] == le and board[1] == le and board[2] == le) or
            (board[3] == le and board[4] == le and board[5] == le) or
            (board[6] == le and board[7] == le and board[8] == le) or
            (board[0] == le and board[3] == le and board[6] == le) or
            (board[1] == le and board[4] == le and board[7] == le) or
            (board[2] == le and board[5] == le and board[8] == le) or
            (board[0] == le and board[4] == le and board[8] == le) or
            (board[2] == le and board[4] == le and board[6] == le))
def tie():
    global x
    for i in board_no:
        if i not in board:
            x+=1
    if x == 45:
        print("Winner: None")
        exit()
        

boardSize()
drawBoard() 
x=0
while True:
    
    player1()
    tie()
    player2()
    tie()