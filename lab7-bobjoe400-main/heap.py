class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.heap = (capacity+1)*[None]
        self.size = 0
        self.capacity = capacity

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other
           items using the < operator'''
        # checks if the list is full or not, then adds the item to the bottom and percolates it up
        if self.is_full():
            return False
        else:
            self.size+=1
            self.heap[self.size] = item
            self.perc_up(self.size)
            return True

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        return self.heap[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        # checks if the list is empty by storing the value at the front of the list and storing it
        # then checking if the stored value is None
        val = self.heap[1]
        if val:
            # swaping of the last element and the first, replacing the last with None,
            #r edoing the list, and lowering the size by 1
            self.heap[1], self.heap[self.size] = self.heap[self.size], None
            self.size -=1
            self.perc_down(1)
        return val

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        # the heap is in order, so we just need to return the valid values in the list
        content = []
        for i in self.heap:
            if i:
                content.append(i)
        return content


    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from
        the items in alist using the bottom-up construction method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to accommodate
        exactly the number of items in alist'''
        # checks if the capacity is less than the length, then sets the new size of the heap
        # creates an empty heap with the current capacity, either the same or the new one
        # iterates through the data in list making an improper heap
        # starting at the last parent (size//2), iterates though the parents sorting the values below them
        if self.capacity < len(alist):
            self.capacity = len(alist)
        self.size = len(alist)
        self.heap = (self.capacity+1)*[None]
        index = 1
        for i in alist:
            self.heap[index] = i
            index +=1
        i = self.size//2
        while i != 0:
            self.perc_down(i)
            i-=1

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return self.size == 0

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.size == self.capacity

    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.capacity

    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.size

    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        # check if we called an invalid index
        # reccursive, end conditions of either the selected index being greater than the size or
        # the current node is a leaf
        # Algorithm:
        #   1. Try to get left and right values if they exist
        #   2. Compare the left nodes and right nodes (if possible) with the current node and making swaps if needed
        #   3. Break the recursion if the node is a leaf
        #   4. Continue onto the next parent and repeat
        if i>self.size:
            return
        try:
            left = self.heap[2*i]
        except:
            left = None
        try:
            right = self.heap[2*i+1]
        except:
            right = None
        curr = self.heap[i]
        if left and right:
            if curr < left or curr < right:
                maximum = max(left,right) #because we are swapping with the max of the two values
                self.heap[i] = maximum
                if left == maximum: #logic for chosing which value to swap (2*i) being left and (2*i+1) for right
                    self.heap[2*i] = curr
                else:
                    self.heap[2*i+1] = curr
        elif left and not right:
            if curr < left:
                self.heap[i] = left
                self.heap[2*i] = curr
        else:
            return
        self.perc_down(i+1)

    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        #recursivly iterate backwards through the list, swapping values as we go up, until we cant go up anymore
        if i <= 1:
            return
        elif self.heap[i] > self.heap[i//2]:
            self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2] #cool little one line swap i found
            self.perc_up(i//2)

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        #since dequeue sorts the list after every call, we can get the returned list by just dequeuing
        #from the heap and putting each value in the list starting at the end and going backward
        self.build_heap(alist)
        index = len(alist)-1
        while not self.is_empty():
            alist[index] = self.dequeue()
            index-=1
