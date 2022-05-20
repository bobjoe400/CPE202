class Node:
    def __init__(self,item):
        self.data = item
        self.next = None
        pass

class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.length = 0
        self.front = self.back = None
        pass


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        if self.length == 0:
            return True
        else:
            return False


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        if self.length == self.capacity:
            return True
        else:
            return False


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if not self.is_full():
            if self.is_empty(): #create the first node if its empty
                self.front = self.back = Node(item)
                self.length +=1
            else:
                temp = Node(item) #creates the new next node
                self.back.next = temp #sets the back next to the new node
                self.back = temp #sets the new back pointer to the temp node once its been hooked up to the list
                self.length +=1 #increments the length
        else:
            raise IndexError


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if not self.is_empty():
            item = self.front.data #grabs the data to be returned
            temp = self.front.next #makes the new temp head
            self.front = temp #sets the real head as the temp head
            self.length -= 1 #increments length
            return item
        else:
            raise IndexError


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.length
