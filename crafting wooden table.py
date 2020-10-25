import math
c, n, p, w = list(map(int, input().strip().split()))

t = 1

if(w//c<1):
    print(0)


else:
    while True:
        if(w-t*c == 0):
            print(t)
            break

        if(w-t*c < 0):
            print(t-1)
            break
        
        if((math.ceil( (w-t*c)/p ) + t ) > n):
            print(t-1)
            break

        if((math.ceil( (w-t*c)/p ) + t ) == n):
            print(t+1)
            break
        t+=1




