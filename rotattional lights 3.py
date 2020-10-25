n, t = list(map(int, input().strip().split()))

L = list(map(int, input().strip().split()))

M = [False] * t

for i in L:
    M[i] = True

copy = M[:]

a=0
while True:
    popped = M.pop(-1)
    M.insert(0,popped)
    if(M == copy):
        print (a)
        break
    a+=1





