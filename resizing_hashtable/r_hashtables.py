

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

        def chingadera():
            pass

class MyLinkedlist:
    def __init__(self):
        self.size = 0
        self.head = None

    def insert(self, key, value):
        new_node = LinkedPair(key, value)
        # new_node.key
        # new_node.next
        # new_node.chingadera()

        if self.size == 0:
            self.head = new_node
        else:
            node = self.head
            while node.next != None:
                # print(node.value)
                node = node.next
                
            node.next = new_node
            
        self.size += 1
        #for( i = 0 ; i < self.size ; i = i+2)
    def printlist(self):
        node = self.head
        while node.next != None:
            print(node.key, node.value)
            node = node.next
        print(node.key, node.value)

    def remove(self, key):
        node = self.head
        # node with key is head
        if node.key == key:
            self.head = node.next
        else:
            while node.next.key != key and node.next != None:
                #print(node.key)
                node = node.next
            if node.next.key == key:
                node.next = node.next.next
                return 1
            else:
                print(key, " not found")
                return 0


    def search(self, key):
        node = self.head
        if node.key == key:
            return node.value
        while node.key != key and node.next != None:
            print('ESSSSEKKKKK')
            node = node.next
            if node.key == key:
                return node.value
        return 0

    def traverse(self, unit):
        node = unit.head
        while node != None:
            print(node)
            node = node.next




# my_list = MyLinkedlist()
# my_list.insert('mickey', 'mouse')
# my_list.insert('donald', 'duck')
# my_list.insert('Brian', 'Illes')
# my_list.insert('Brian', 'doyle')
# my_list.insert('gokce', 'charis')
# my_list.printlist()
# print(my_list.search('Brian'))
# print(my_list.search('quack'))
# print('\n\n')
# my_list.remove('mickey' )
# my_list.printlist()
        



# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.hash_table = [MyLinkedlist()] * capacity
        self.capacity = capacity
        

# '''
# Research and implement the djb2 hash function
# '''
def hash(string, capacity):
    m = 0
    for i in string:
        m = m + ord(i)
    m = m%capacity
    return m
def hash_table_insert(bht, key, value):
    index = hash(key, len(bht.hash_table))
    bht.hash_table[index].insert(key, value)
    for linkedlist in bht.hash_table:
        print('linkedlist')
        linkedlist.printlist()
    print('------------------------------------------')


def hash_table_remove(bht, key):
    index = hash(key, len(bht.hash_table))
    return bht.hash_table[index].remove(key)

def hash_table_retrieve(bht, key):
    index = hash(key, len(bht.hash_table))
    return bht.hash_table[index].search(key)

# '''
def hash_table_resize(hash_table):
    new_hash_table = [MyLinkedlist()] * len(hash_table)*2
    for i in range(len(hash_table)):
        pass 


def Testing():
    bht = HashTable(2)
    
    hash_table_insert(bht, "line_1", "Tiny hash table")
    hash_table_insert(bht, "line_2", "Filled beyond capacity")
    hash_table_insert(bht, "line_3", "Linked list saves the day!")
    
    hash_table_remove(bht, "line_1")
    hash_table_insert(bht, "line_4", "It puts the lotion on its skin")
    hash_table_remove(bht, "line_4")
    hash_table_insert(bht, "line_5", "OR ELSE IT GETS THE HOSE AGAIN")
    print(hash_table_retrieve(bht, "line_1"))
    print(hash_table_retrieve(bht, "line_2"))
    print(hash_table_retrieve(bht, "line_3"))
    print(hash_table_retrieve(bht, "line_4"))
    print(hash_table_retrieve(bht, "line_5"))

    # old_capacity = len(bht.hash_table)
    # bht = hash_table_resize(bht)
    # new_capacity = len(bht.hash_table)

    # print("Resized hash table from " + str(old_capacity)
    #       + " to " + str(new_capacity) + ".")


Testing()

  