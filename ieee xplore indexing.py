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



while True:
    try:
        line = input()

    except:
        break
    lines.append(line)
    

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

title_final = title.split(" ")
abstract_final = abstract.split(" ")
body_final = body.split(" ")

for i in index_terms:
    for j in title_final:
    d[i] += title_final.count(i) * 5
    d[i] += abstract_final.count(i) * 3
    d[i] += body_final.count(i) * 1


for i in stop_words:
    title = title.replace(i, '')
    abstract = abstract.replace(i, '')
    body = body.replace(i, '')

title = title.replace("n't", '')
abstract = abstract.replace("n't", '')
body = body.replace("n't", '')

# title = title.replace(",", '')
# abstract = abstract.replace(",", '')
# body = body.replace(",", '')

# title = title.replace(".", '')
# abstract = abstract.replace(".", '')
# body = body.replace(".", '')

# title = title.replace("?", '')
# abstract = abstract.replace("?", '')
# body = body.replace("?", '')

# title = title.replace("!", '')
# abstract = abstract.replace("!", '')
# body = body.replace("!", '')

body = body.replace("<sec>", '')
body = body.replace("<label>", '')
body = body.replace("<p>", '')
body = body.replace("<fig>", '')
body = body.replace("<caption>", '')

body = body.replace("</label>", '')
body = body.replace("</sec>", '')
body = body.replace("</p>", '')
body = body.replace("</fig>", '')
body = body.replace("</caption>", '')

title_2 = title[::]
title_2 = title.split()

abstract_2 = abstract[::]
abstract_2 = abstract_2.split()

body_2 = body[::]
body_2 = body_2.split()


L = 0 

for k in title_2:
    if(len(k)>=4):
        L+=1
for m in abstract_2:
    if(len(m)>=4):
        L+=1

for n in body_2:
    if(len(n)>=4):
        L +=1


for z in d.keys():
    d[z] = (d[z]/L * 100)

printing(d)
    
