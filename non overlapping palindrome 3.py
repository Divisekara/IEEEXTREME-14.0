n = int(input())

def f(x):
    n = len(x)
    dp = [[0]*(n+1) for a in range(n)]

    for i in range(0, n):
        for j in range(i+1, n+1):
            s = x[i:j]
            if(s == s[::-1]):
                dp[i][j] = len(s)

    max_sum = 0
    for i in range(0,n):
        for j in range(1, n+1):
            for k in range(j,n):
                max_sum = max(max_sum, dp[i][j] + max(dp[k][j+1:n+1]))

    print(max_sum)

for b in range(n):
    string = input().strip()
    f(string)