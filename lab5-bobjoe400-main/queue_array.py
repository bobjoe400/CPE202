
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.queue = [None]*capacity #creates an empty array with size of capacity
        self.front = 0 #sets front index to 0
        self.back = capacity-1 #because its an empty array, we want to sent the back index to just behind the front
        self.length = 0; #use this to track length


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
            self.back = (self.back + 1)%self.capacity #because it is a circular array, we need to be able to wrap around the indecies so we just us modulo to complete this 
            self.queue[self.back] = item #sets the new back index to the item
            self.length = self.length+1 #increments the size of the queue
        else:
            raise IndexError


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if not self.is_empty():
            item = self.queue[self.front] #grabs the item in the front of the queue to be returned
            self.front = (self.front + 1)%self.capacity #increments the front index
            self.length = self.length-1
            return item
        else:
            raise IndexError

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.length

