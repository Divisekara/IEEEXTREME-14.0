n,m,r,c = list(map(int, input().strip().split()))

L = []
for i in range(r):
    line = list(map(int, input().strip().split()))
    L.append(line)

right_shift = c- 1
down_shift = r - 1

expenses = []

def costing(List,r,c):
    cost = 0
    for i in range(r):
        for j in range(c):
            # print(L, r-1, c-1)
            price = List[i][j]

            num_tiles_down = (n-i)//r
            if((n-i)%r>=i):
                num_tiles_down+=1

            num_tiles_right = (m-j)//c
            if((m-j)%c>=j):
                num_tiles_right += 1
            
            # print(price * num_tiles_down * num_tiles_right, end = ' ')

            cost += price * num_tiles_down * num_tiles_right

    # print('')
    return cost
    

M = L[:]

L_copy= L[:]

for i in range(c):
    for j in range(r):
        # print(L)
        expenses.append(costing(L,r,c))
        L.insert(0,L.pop(-1))
        
    
    for k in range(r):
        line = L[k]
        line.insert(0, line.pop(-1))
        L[k]  = line

print(min(expenses))




