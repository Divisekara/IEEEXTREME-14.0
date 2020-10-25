import math
n, cb, cp = list(map(int, input().strip().split()))

blacks, pinks = 0,0
for i in range(n):
    b, p = list(map(int, input().strip().split()))
    
    blacks +=b
    pinks += p

money = math.ceil(blacks/10)*cb + math.ceil(pinks/10)*cp

print(money)

