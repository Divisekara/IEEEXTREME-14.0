n, t = list(map(int, input().strip().split()))


L = list(map(int, input().strip().split()))
total = sum(L)
start = L[:]

for a in range(t):
    copy = []

    for i in L:
        j = i+1
        if(j>= t):
            j = j - t
        copy.append(j)

    L = copy[:]

    L.sort()
    if(start == L):
        print(a)
        break

else:
    print(a)

