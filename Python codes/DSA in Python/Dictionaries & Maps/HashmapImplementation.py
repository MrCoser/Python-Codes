# Python program for
# implementation of Hashmaps

# For the class Map, we will be having
# three functions :
# 1)  Insert(key, value)
# 2)  Remove(key)
# 3)  Search(key)


class MapNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



class Map:

    def __init__(self):
        self.bucketSize = 10   # Size of bucket array 
        self.bucket = [None for i in range(self.bucketSize)]       # Bucket array declared
        self.count = 0

    
    def size(self):
        return self.count


    def getBucketIndex(self, hc):
        return (abs(hc) % (self.bucketSize))


    def insert(self, key, value):

        hc = hash(key)
        indx = self.getBucketIndex(hc)
        head = self.bucket[indx]

        while head is not None:
            if head.key == key:
                head.value = value
                return

            head = head.next
        
        head = self.bucket[indx]
        new = MapNode(key, value)
        new.next = head
        self.bucket[indx] = new
        self.count += 1



    def getValue(self, key):
        h = hash(key)
        indx = self.getBucketIndex(h)
        head = self.bucket[indx]

        while head is not None:
            if head.key == key:
                return head.value

            head = head.next


        return None

    def search(self, key):     # To check whether element exists or not
        x = self.getValue(key)
        if (x):
            return True

        else:
            return False

    def remove(self, key):
        hc = hash(key)
        indx = self.getBucketIndex(hc)
        head = self.bucket[indx]

        prev = None

        while head is not None:
            if head.key == key:
                if prev is None:
                    self.bucket[indx] = head.next

                else:
                    prev.next = head.next
                self.count -= 1
                return head.value

            
            prev = head
            head = head.next
        return None



 

m = Map()
m.insert('abc', 2)
m.insert('Rohan', 7)
print(m.size())
print(m.getValue('Rohan'))


