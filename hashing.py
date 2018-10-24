
# generates the key used in hash function
def key(string, lim):
    # if size of string are greater then lim
    if len(string)>=lim:
        # create a list with all ASCII values in string

         # get character ascii value for every character in string if it's a valid value
        lista = [ord(i) for i in string if ord(i) < 123 and ord(i) > 96]
        # only the first lim values will be used in key
        lista = lista[:lim] 
        
        # sum all ASCII values with some random number
        k = 0
        for i in range(len(lista)):
            k += lista[i]*128^(len(lista)-1)
        return k

# transformation function
def h(k, tam):
    return k%tam
