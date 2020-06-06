board_no=[]
board=[]
def boardSize():
    n=int(input("size --> "))
    for i in range(n**2):
        board_no.append(i)
        board.append(i)
    return n
def drawBoard(n):
    for number in board_no:
        if (number+1)%n == 0 and number<10:
            print(" ",board[number],end="\n")
        elif (number==0 or number%n ==0) and number < 10:
            print("",board[number],end="")
        elif number%n ==0 and number>=10:
            if (board[number] == "X" )or (board[number]== "O"):
                print("",board[number],end="")
            else:
                print(board[number],end="")
        elif number<10:
            print(" ",board[number],end="")
        elif (number+1)%n == 0 and number>=10:
            if (board[number] == "X" )or (board[number]== "O"):
                print(" ",board[number],end="\n")
            else:
                print("",board[number],end="\n")
        else:
            if (board[number] == "X" )or (board[number]== "O"):
                print(" ",board[number],end="")
            else:
                print("",board[number],end="")
def move(n,letter):
    board[n] = letter
def player1(n):
    m=int(input("X--> "))
    letter = "X"
    move(m,letter)
    drawBoard(n)
    if winner(letter,n):
        print("Winner: " + letter)
        exit()
def player2(n):
    m=int(input("O--> "))
    letter = "O"
    move(m,letter)
    drawBoard(n)
    if winner(letter,n):
        print("Winner: " + letter)
        exit()
def winner(le,n):
    for i in range(n):
        if board[i*n:(i+1)*n].count("X") ==n:
            return True
        elif board[i*n:(i+1)*n].count("O") == n:
            return True
        elif board[i:n**2:n].count("X") == n:
            return True
        elif board[i:n**2:n].count("O") == n:
            return True
        elif board[0:n**2:n+1].count("X") == n:
            return True
        elif board[0:n**2:n+1].count("O") == n:
            return True
        elif board[n-1:n**2:n-1].count("X") == n:
            return True
        elif board[n-1:n**2:n-1].count("O") == n:
            return True
def tie(n):
    global x
    for i in board_no:
        if i not in board:
            x+=1
    if x == (((n**2)*((n**2)+1))/2):
        print("Winner: None")
        exit()
n=boardSize()
drawBoard(n) 
x=0
while True:
    player1(n)
    tie(n)
    player2(n)
    tie(n)