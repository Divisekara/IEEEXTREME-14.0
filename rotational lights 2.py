n, t = list(map(int, input().strip().split()))


L = list(map(int, input().strip().split()))


start = L[:]

a = 0

while True:
    L = [(x+1)%t for x in L]

    L.sort()

    if(start == L):
        print(a)
        break
    a +=1

else:
    print(a)

