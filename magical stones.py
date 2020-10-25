n = int(input().strip())
L = list(map(int, input().strip().split()))
L_copy = L[:]
answers = []

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

q = int(input().strip())
inputs = []

for j in range(q):
    inputs.append(int(input().strip()))

for k in inputs:
    if k in answers:
        print(answers.index(k)+1)
    else:
        print(-1)



        