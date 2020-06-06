board_no=[]
board=[]
coordinate=[]
final=[]
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
def automated():
    n=['0','1','2','3','4','5','6','7','8','9']
    co=input()#.split(')->(')
    for i in co:
        if i in n:
            coordinate.append(int(i))
    for k in range(0,len(coordinate),2):
        q=(coordinate[k:k+2])
        final.append(q)
    #[coordinate[k:k+2] for k in range(0,len(coordinate),2)]
    
def move(n,letter):
    board[n] = letter

def player1(y):
    n=rnc(y)
    print("X--> ",n)
    letter = "X"
    move(n,letter)
    drawBoard()
    if winner(letter):
        print("Winner: " + letter)
        exit()
def rnc(y):
    row=final[y][0]
    column=final[y][1]
    a=ccc(row,column)
    return int(a)
def ccc(row,column):
    
    if row==0 and column==0:
        n=board[0]
    if row==0 and column==1:
        n=board[1]
    if row==0 and column==2:
        n=board[2]
    if row==1 and column==0:
        n=board[3]
    if row==1 and column==1:
        n=board[4]
    if row==1 and column==2:
        n=board[5]
    if row==2 and column==0:
        n=board[6]
    if row==2 and column==1:
        n=board[7]
    if row==2 and column==2:
        n=board[8] 
    return n
def player2(y):
    n=rnc(y)
    print("O--> ",n)
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

automated()
boardSize()
drawBoard() 
x=0
y=0
while True:
    
    player1(y)
    tie()
    y+=1
    player2(y)
    tie()
    y+=1