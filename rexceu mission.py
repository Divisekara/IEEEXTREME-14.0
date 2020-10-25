n = int(input())
S = list(map(int,input().strip().split()))

d = int(input().strip())

answer = 0
gathered = 0

List = []
for i in range(d):
    line = list(map(int, input().strip().split()))
    List.append(line)
    answer += line[-1]


print(answer)


