from copy import copy, deepcopy


def elements(L,b,c):
    M = []
    # print(b,c)
    M.append(L[b][c+1])
    M.append(L[b][c-1])
    M.append(L[b+1][c])
    M.append(L[b-1][c])
    
    return M

zeroRuler, oneRuler = input().split(";")
n, turns = map(int,input().split())

#################################


# print(left, right)
board = []
newBoard = []
for tt in range(n):
    if tt == 0:
        board.append(['0']*(n+2))
    
    row = list(input())
    row = [row[-1]] + row + [row[0]]
    board.append(row)

    if tt == n-1:
        board.append(['0']*(n+2))

board[0] = board[-2]
board[-1] = board[1]
# print(L)

########################################


zeroRule__ = []
oneRule__ = []
newBoard = deepcopy(board)
for i in range(5):
    if zeroRuler[i] == '1':
        zeroRule__.append(i)
    if oneRuler[i] == '1':
        oneRule__.append(i)

for turn in range(turns):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if board[i][j] == '0':
                neighbours = int(board[i-1][j]) + int(board[i+1][j]) + int(board[i][j-1]) + int(board[i][j+1])
                if neighbours in zeroRule__:
                    newBoard[i][j] = '1'
            if board[i][j] == '1':
                neighbours = int(board[i-1][j]) + int(board[i+1][j]) + int(board[i][j-1]) + int(board[i][j+1])
                if neighbours not in oneRule__:
                    newBoard[i][j] = '0'
        newBoard[i][0] = newBoard[i][-2]
        newBoard[i][-1] = newBoard[i][1]
    newBoard[0] = newBoard[-2]
    newBoard[-1] = newBoard[1]
    board = deepcopy(newBoard)




for i in range(1,n+1):
    k = board[i][1:-1]
    print ("".join(k)) 