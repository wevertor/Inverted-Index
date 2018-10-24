
# open file and store his content in a list of string
def fileOpener(path):
    
    # open file
    file = open(path)
    
    # get text in file
    string = file.read()
    
    # all characters must be in lower case
    string = string.lower()
    
    # list with all words
    return string.split()

def removePunctuation(stringList, lim):
    # remover pontuação

    # creates a new empty list
    lista = [None for i in range(len(stringList))]
    
    # for all words
    for i in range(len(stringList)):
        
        # get the only the lowcase letters
        ascii = [ord(j) for j in stringList[i] if ord(j) < 123 and ord(j) > 96]
        letr = [chr(j) for j in ascii]
        
        # store the word at the same position in the empty list
        if len(letr) >= lim:
            lista[i] = ''.join(letr)

    return lista

# returns a list with the words and total of their occurences
def invertedIndex(id, path, limit):
    index = []
    
    lista = fileOpener(path)
    lista = removePunctuation(lista, limit)

    i = 0
    while i<len(lista):
        j = i
        palavra = lista[0]
        count = 0
        while j < len(lista):
            if lista[j] == palavra:
                count += 1

            j+=1
        k = 0
        while k < len(lista):
            if lista[k] == palavra:
                lista.remove(lista[k])
            else:
                k += 1 
        index.append([palavra, count, id])
        # i+=1
    
    for i in index:
        if i[0] == None:
            index.remove(i)

    return index

