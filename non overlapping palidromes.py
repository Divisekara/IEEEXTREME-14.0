n = int(input().strip())


def f(x):
    n = len(x)
    dp = [[0]*n for a in range(n)]

    for k in range(1,n):
        for i in range(0, n-k):
            j = i+k

            if(x[i]==x[j]):
                dp[i][j] = 2 + dp[i+1][j-1] 
                print(dp[i][j]) #####3
            else:
                dp[i][j] = max(dp[i][j-1],dp[i+1][j])
                print(dp[i][j])#######

    max_sum = 0

    for i in range(0,n):
        for j in range(0, n-1):
            max_sum = max(max_sum, dp[i][j] + dp[j+1][n-1]) 

    print (dp)
    return max_sum

for b in range(n):
    x = input().strip()
    print(f(x))
