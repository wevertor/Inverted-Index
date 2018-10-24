from analizing import invertedIndex
from dict import Dict
from sys import argv

# get input #
limite = int(argv[1])
path = [argv[i+2] for i in range(len(argv)-2)]

# list for words #
words = []

print("Arquivos =", path)

# get the inverted index from files #
for i in range(len(path)):
    words.append(invertedIndex(i+1, path[i], limite))

dictionary = Dict(13, limite)
words2 = []

for i in range(len(words)):
    for j in range(len(words[i])):
        # creates a list with all occurences of same word #
        lista = [words[i][j][0]]
        
        for k in range(len(words)):
            for l in range(len(words[k])):
                # compares the words #
                if words[i][j][0] == words[k][l][0]:
                    lista.append([words[k][l][1], words[k][l][2]])
        
        words2.append(lista)

# remove the repeted occurences #
i = 0
while i<len(words2):
    j = i+1
    while j<len(words2):
        if words2[i] == words2[j]:
            words2[j] = None
        j +=1
    i += 1

i = 0
while i < len(words2):
    if words2[i] == None:
        words2.remove(words2[i])
        i = 0
    else:
        i += 1

for i in words2:
    dictionary.linearInsert(i[0], [i[j] for j in range(len(i)) if j > 0])

print(dictionary)

