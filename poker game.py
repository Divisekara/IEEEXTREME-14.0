# n,k =list(map(int, input().strip().split()))

# L = list(input().strip())
# M = list(input().strip())

n,k =9,2

L = list('AA9Q3776J')
M = list('nyynnnynn')

had = []
not_had =  []

for x in range(n):
    i = M[x]
    card = L[x]
    if(i=='n'):
        not_had.append(card)

    elif(i=='y'):

        if(card not in not_had):
            had.append(card)
            not_had.append(card)

        elif(card in not_had):
            not_had.append(card)
    
possibilities = list()
for a in range(k-len(had)):
    had.append

        


