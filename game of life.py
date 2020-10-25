empty_cells, live_cells = input().strip().split(';')

empty = list(empty_cells)
live = list(live_cells)

empty_indexes = [empty.index(x) for x in empty if x==1]
live_indexes = [live.index(x) for x in live if x==1]

def elements(L,b,c):
    M = []
    # print(b,c)
    M.append(L[b][c+1])
    M.append(L[b][c-1])
    M.append(L[b+1][c])
    M.append(L[b-1][c])
    
    return M


n, m = list(map(int, input().strip().split()))

L = []

for a in range(n):
    line =  list(map(int, list(input().strip())))
    L.append(line)

# print(left, right)
L_copy = L[:]

L.insert(0,L[-1])
L.insert(-1, L[1])

for i in range(1,n+1):
    left = L[i][-1]
    right = L[i][0]
    L[i] = [left] + L[i] + [right]  

# print(L)


for d in range(m):
    for b in range(1,n+1):
        for c in range(1,n):
            temp = L[b][c]
            M = elements(L,b,c)
            ones = M.count(1)
            
            if(temp==0):
                if(ones in empty_indexes):
                    L_copy[b-1][c-1] = 1

            else:
                if(ones in live_indexes):
                    L_copy[b-1][c-1] = 0


for i in range(n):
    line = "".join(list(map(str, L_copy[i])))
    print(line)
