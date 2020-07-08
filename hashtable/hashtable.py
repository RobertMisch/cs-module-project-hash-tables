class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashLinkedList:
    def __init__(self):
        self.head = None
    
    def find(self, key):
        cur = self.head
        while cur is not None:
            if cur.key == key:
                return cur
            cur = cur.next
        return None  # we didn't find it

    def insert_at_head(self, key, value):
        n = HashTableEntry(key, value)
        if self.head == None:
            self.head=n
            return 
        n.next = self.head
        self.head = n

    def delete(self, key):
        cur = self.head

        # Special case of deleting the head

        if cur.key == key:  # Are we deleting the head?
            self.print()
            self.head = self.head.next
            cur.next = None
            return cur

        # General case

        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.key == key:
                prev.next = cur.next  # cuts out the node
                cur.next = None
                return cur
            else:
                prev = prev.next
                cur = cur.next

        return None


    def append(self, value):
        # TODO
        pass
    
    def print(self):
        cur=self.head
        while cur != None:
            print(cur.value)
            cur=cur.next 
        return
    def all_values(self):
        cur=self.head
        result=[]
        while cur != None:
            result.append([cur.key, cur.value])
            cur=cur.next 
        return result
# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity= capacity
        if(self.capacity< MIN_CAPACITY):
            self.capacity= MIN_CAPACITY

        self.num_stored=0
        self.table= [None] * self.capacity

    def __str__(self):
        return f"{self.table}"


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        if(self.capacity>0):
            return self.num_stored/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        myhash = 14695981039346656037 #fnv 64bit offset
        mychars=key.encode()
        for i in mychars:
            myhash = myhash * 1099511628211 #fnv 64 bit prime
            myhash = myhash ^ i
        return myhash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        if self.table[index] == None:
            self.table[index]=HashLinkedList()
            self.table[index].insert_at_head(key, value)
            self.num_stored+=1
            if(self.get_load_factor()>=0.7):
                self.resize(self.capacity*2)
            # self.table[index].print()
        else:
            exists = self.table[index].find(key)
            if(exists != None):
                exists.value=value
            else:
                self.table[index].insert_at_head(key, value)
                self.num_stored+=1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        # temp = self.table[index]
        if self.table[index] == None:
            print('warning: key not found')
            return None
        else:
            exists = self.table[index].find(key)
            if(exists != None):
                self.table[index].delete(key)
            else:
                print('warning: key not found')
                return None



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        temp = self.table[index]
        if temp == None:
            print('warning: key(index) not found')
            print(self)
        else:
            node = temp.find(key)
            if node == None:
                print('warning: key(node) not found')
            else:
                return node.value



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        #double capacity
        # self.capacity= self.capacity * 2
        self.capacity = new_capacity
        #loop self.table
        prev_table=self.table.copy()
        self.table= [None] * self.capacity
        for bucket in prev_table:
        #for each bucket go through it's linked list
            if bucket == None:
                continue
            cur=bucket.head
            while cur != None:
                self.put(cur.key, cur.value)
                cur=cur.next 
        #make the new table with all none's #self.table= [None] * self.capacity
        #rehash the big array of stored stuff
        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    # print(ht.table)
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    # print(ht.table)
    ht.put("line_3", "All mimsy were the borogoves,")
    # print(ht.table)
    ht.put("line_4", "And the mome raths outgrabe.")
    # print(ht.table)
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    # print(ht.table)
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    # print(ht.table)
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    # print(ht.table)
    ht.put("line_8", 'The frumious Bandersnatch!"')
    # print(ht.table)
    ht.put("line_9", "He took his vorpal sword in hand;")
    # print(ht.table)
    ht.put("line_10", "Long time the manxome foe he sought--")
    # print(ht.table)
    ht.put("line_11", "So rested he by the Tumtum tree")
    # print(ht.table)
    ht.put("line_12", "And stood awhile in thought.")
    # print(ht.table)

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
