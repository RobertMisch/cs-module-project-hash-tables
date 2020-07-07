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
        self.head=None
    
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
        n.next = self.head
        self.head = n
    def delete(self, key):
        cur = self.head

        # Special case of deleting the head

        if cur.key == key:  # Are we deleting the head?
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
        bucket = self.table[index]
        if ( bucket != None):
            if(bucket.find(key) == None):
                bucket.insert_at_head(key, value)
            else:
                bucket.find(key).value=value 
        else:
            bucket=HashLinkedList
            bucket.insert_at_head(bucket, key, value)
            self.num_stored+=1



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        temp = self.table[index].delete(key)
        if temp == None:
            print('warning: key not found')
            return
        return temp


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        temp = self.table[index].find(key)
        if temp == None:
            print('warning: key not found')
        else:
            return temp.value 


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



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
