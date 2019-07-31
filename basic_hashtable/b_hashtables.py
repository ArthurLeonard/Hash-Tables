

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value



# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# Done
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.hash_table = [None] * capacity
        self.capacity = capacity
        #return hash_table

# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, capacity):
    m = 0
    for i in string:
        m = m + ord(i)
    m = m%capacity
    return m



# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(bht, key, value):
    l = len(bht.hash_table)
    if bht.hash_table[hash(key, l)] == None:
        bht.hash_table[hash(key, l)] = value
    else:
        print("ERROR: overwriting")
        return None


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(bht, key):
    l = len(bht.hash_table)
    if bht.hash_table[hash(key, l)] == None:
        print("ERROR: Value does not exist")
        return None
    else:
        bht.hash_table[hash(key, l)] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(bht, key):
    l = len(bht.hash_table)
    if bht.hash_table[hash(key, l)] == None:
        return None
    else:
        value = bht.hash_table[hash(key, l)] 
        bht.hash_table[hash(key, l)] = None
        return value
def Testing():
    bht = BasicHashTable(16)
    #list = MyLinkedList()
                                                       
    hash_table_insert(bht, "line", "Here today...\n")

    hash_table_remove(bht, "line")

    if hash_table_retrieve(bht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")
 

Testing()
 