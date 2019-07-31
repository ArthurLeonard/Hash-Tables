

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
        self.count = 0

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

    # def traverse(self, unit):





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
        self.count = 0
        self.temp_hash_table = None
        self.capacity = capacity

    def resize_hash_table(self, multiple):
        print('\n\n#########################################\nIN RESIZE HASH TABLE!!!!!!!!\n\n')
        # sadece salaklik icin
        if multiple == 2:
            self.count += 1
            print(self.count)
        if multiple == 1/2:
            self.count -= 1
            print(self.count)

        if self.count > 0.7 * self.capacity or self.count < 0.2 * self.capacity:

            # copy hash table contents to temporary list
            self.temp_hash_table = self.hash_table   #?
            # record new capacity
            self.capacity = self.capacity * multiple
            # start with a blank slate with twice the size
            self.hash_table = [MyLinkedlist()] * self.capacity

            ############################################################################
            ####          GET EACH NODE FROM OLD TABLE AND PLACE IN NEW TABLE    #######
            ############################################################################

            # STEP 1 - Get to linked list level 
            for linkedlist in self.temp_hash_table:
                node = linkedlist.head
                # STEP 2 - Get to node level
                while node != None: #?
                    #
                    # for each node, rehash and place in appropriate place in new hash table
                    # STEP 2 a: rehash
                    index = hash(node.key, self.capacity) 
                    # STEP 2 b: place in appropriate place in new hash table
                    hash_table_insert(self.hash_table, node.key, node.value)
                    # keep moving on to get all nodes in linked list
                    node = node.next 
            
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
    print(type(bht))
    print('capacity is ',bht.capacity)
    bht.resize_hash_table(2)
    # # Check whether the hash table needs to be doubled in size
    #
    # if self.count > 0.7 * len(bht)
    #     resize_hash_table()

    index = hash(key, len(bht.hash_table))
    bht.hash_table[index].insert(key, value)
    # self.count += 1
    for linkedlist in bht.hash_table:
        print('linkedlist')
        linkedlist.printlist()
    print('------------------------------------------')


def hash_table_remove(bht, key):
    bht.resize_hash_table(1/2)
    index = hash(key, len(bht.hash_table))
    # self.count -= 1
    return bht.hash_table[index].remove(key)


def hash_table_retrieve(bht, key):
    index = hash(key, len(bht.hash_table))
    return bht.hash_table[index].search(key)

# # '''
# def resize_hash_table(hash_table, multiple):
#     # copy hash table contents to temporary list
#     self.temp_hash_table = self.hash_table   #?
#     # start with a blank slate with twice the size
#     self.hash_table = [MyLinkedlist()] * len(hash_table) * multiple

#     ############################################################################
#     ####          GET EACH NODE FROM OLD TABLE AND PLACE IN NEW TABLE    #######
#     ############################################################################

#     # STEP 1 - Get to linked list level 
#     for linkedlist in range(len(hash_table)):
#         node = linkedlist.head
#         # STEP 2 - Get to node level
#         while node != None: #?
#             #
#             # for each node, rehash and place in appropriate place in new hash table
#             # STEP 2 a: rehash
#             index = hash(node.key, len(new_hash_table)) 
#             # STEP 2 b: place in appropriate place in new hash table
#             hash_table_insert(self.hash_table, node.key, node.value)
#             # keep moving on to get all nodes in linked list
#             node = node.next 


def Testing():
    bht = HashTable(2)
    
    hash_table_insert(bht, "line_1", "Tiny hash table")
    hash_table_insert(bht, "line_2", "Everything is groovy")
    hash_table_insert(bht, "line_3", "Linked list saves the day!")
    
    # hash_table_remove(bht, "line_1")
    # hash_table_insert(bht, "line_4", "It puts the lotion on its skin")
    # hash_table_remove(bht, "line_4")
    # hash_table_insert(bht, "line_5", "OR ELSE IT GETS THE HOSE AGAIN")
    # print(hash_table_retrieve(bht, "line_1"))
    # print(hash_table_retrieve(bht, "line_2"))
    # print(hash_table_retrieve(bht, "line_3"))
    # print(hash_table_retrieve(bht, "line_4"))
    # print(hash_table_retrieve(bht, "line_5"))

    # old_capacity = len(bht.hash_table)
    # bht = bht.resize_hash_table(2)
    # new_capacity = len(bht.hash_table)    

    # print("Resized hash table from " + str(old_capacity)
    #       + " to " + str(new_capacity) + ".")


Testing()

  