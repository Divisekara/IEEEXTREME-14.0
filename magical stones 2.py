# T = int(input().strip())
# n = int(input().strip())
# wi = list(map(int, input().strip().split()))
# bi = list(map(int, input().strip().split()))

def purify(L):
    answers = []
    L_copy =L[:]
    final_len = 0
    
    while True:

        temp = sorted(list(set(L)))
        after_first_spell = []

        for i in temp:
            after_first_spell.append(L_copy[i-1])
        
        # print(final_len)
        if(final_len == len(temp)):
            break

        answers.append(len(temp))

        final_len = len(temp)

        L = after_first_spell[:]
    
    return L


n = 4
wi = [2,3,4,1]
bi = [3,3,2,3]

print(purify(wi + bi))








# for i in range(T):
