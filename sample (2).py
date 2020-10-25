def printing(d):

    keys = []
    values = []
    for i in d.keys():
        keys.append(i)
        values.append(d[i])

    M  = list(set(values[::]))
    M.sort()
    M.reverse()

    answer_keys = []

    tempo = 0
    for i in range(len(M)):
        temp_keys = []

        tempo += 1

        x=M[i]
        while(x in values):
            indexing = values.index(x)
            key = keys[indexing]
            temp_keys.append(key)
            values.pop(indexing)
            keys.pop(indexing)

        temp_keys.sort()
        answer_keys.append(temp_keys)

        if(tempo==3):
            break

    for j in answer_keys:
        for k in j:
            print(k + ": " + str(d[k]))

###################################################################

stop_words = input().strip().split(';')
index_terms = input().strip().split(';')

lines = []

d = {}

for i in index_terms:
    d[i] = 0


'''
while True:
    try:
        line = input()

    except:
        break
    lines.append(line)
'''

while True:
    line = input()

    if line:
        lines.append(line)
    else:
        break


doc = " ".join(lines)


title_start = doc.find('<title>')
title_end = doc.find('</title>')
title = doc[title_start + 7 : title_end]
abstract_start = doc.find('<abstract>')
abstract_end = doc.find('</abstract>')
abstract = doc[abstract_start + 10 : abstract_end]
body_start = doc.find('<body>')
body_end = doc.find('</body>')
body = doc[body_start + 6 : body_end]


title = title.lower()
abstract = abstract.lower()
body = body.lower()

#########################################################

title = title.replace('!', '')
title = title.replace(',', '')
title = title.replace('.', '')
title = title.replace('?', '')
title = title.replace('<', ' ')
title = title.replace('>', ' ')

title = title.split()
#######################

abstract = abstract.replace('!', '')
abstract = abstract.replace(',', '')
abstract = abstract.replace('.', '')
abstract = abstract.replace('?', '')
abstract = abstract.replace('<', ' ')
abstract = abstract.replace('>', ' ')

abstract = abstract.split()
##########################

body = body.replace('!', '')
body = body.replace(',', '')
body = body.replace('.', '')
body = body.replace('?', '')
body = body.replace('<', ' ')
body = body.replace('>', ' ')

body = body.split()
##########################


for i in index_terms:
    d[i] += title.count(i) *5
    d[i] += abstract.count(i) *3
    d[i] += body.count(i) *1


################################################################


title_copy = title[::]
abstract_copy = abstract[::]
body_copy = body[::]

for b in title_copy:
    if('>' in b):
        title.remove(b)
    if('<' in b):
        title.remove(b)

for b in abstract_copy:
    if('>' in b):
        abstract.remove(b)
    if('<' in b):
        abstract.remove(b)

for b in body_copy:
    if('>' in b):
        body.remove(b)
    if('<' in b):
        body.remove(b)

for c in stop_words:
    while(c in title):
        title.remove(c)

    while(c in abstract):
        abstract.remove(c)

    while(c in body):
        body.remove(c)

L = len(title) + len(abstract) + len(body) 


for z in d.keys():
    d[z] = (d[z]/L * 100)

printing(d)
    
