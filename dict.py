from hashing import key, h

class Dict:


    # STANDARD METHODS #

    # object constructor
    def __init__(self, size, lim):
        self.values = [[False, None, None] for i in range(size)] # flag control, item and key
        self.keyLen = lim # limit in size of key
        self.size = size # size of hashtable
    
    # object size 
    def __len__(self):
        count = 0
        for i in range(self.size):
            if self.values[i][0] == True:
                count += 1
        return count

    def __str__(self):
        string = '\n'
        for i in self.values:
            if i[0]:
                string += i[1]+ " : " + str(i[2]) + '\n'

        return string

    #   OBJECT METHODS #
    
    # insert element
    def linearInsert(self, chave, item): #item type: string
        k = key(chave, self.keyLen)
        
        # get index #
        i = h(k, self.size)
        while i < self.size and self.values[i][0] == True:
            i += 1
        
        # if index is in range of hashtable #
        if i < self.size:
            self.values[i][0] = True
            self.values[i][1] = chave
            self.values[i][2] = item
        else:

            # get index from beginning#
            i = 0
            while i < self.size and self.values[i][0] == True:
                i += 1
            
            if i < self.size:
                self.values[i][0] = True
                self.values[i][1] = chave
                self.values[i][2] = item
            else:
                print("Erro ao inserir elemento:", chave, "Tabela Hash completa.")


    # return element removing it
    def linearRemove(self, chave):
        k = key(chave, self.keyLen)
        i = h(k, self.size)
        while i < self.size and self.values[i][0] and self.values[i][2] == k: 
            i += 1
        
        if i < self.size:
            self.values[i][0] = False
        else:
            i = 0
            while i < self.size and self.values[i][0] and self.values[i][2] == k: 
                i += 1
            
            if i < self.size:
                self.values[i][0] = False
            else:
                print("Erro ao remover elemento:", chave, "Elemento não encontrado.")
    # returns the element without removing
    def linearGet(self, string):
        k = key(string, self.keyLen)
        
        i = h(k, self.size)
        while i < self.size and self.values[i][0] == False and self.values[i][2] != k: 
            i += 1
        
        if self.values[i][0] == False and self.values[i][2] != k:
            return self.values[i][2]
        else:
            i = 0
            while i < self.size and self.values[i][0] == False and self.values[i][2] != k: 
                i += 1
            
            if self.values[i][0] == False and self.values[i][2] != k:
                return self.values[i][2]
            else:
                return "Elemento não encontrado."


