class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#in this my list is a reversed list where the head is the last item added. this is used to keep an O(1) since traversing the list would be a O(n).
class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Linked List'''

    def __init__(self, capacity):
        '''Creates and empty stack with a capacity'''
        self.capacity = capacity
        self.top = None
        self.num_items = 0

    def is_empty(self):
        '''Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance'''
        if self.num_items ==0:
            return True
        else:
            return False

    def is_full(self):
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == self.capacity:
            return True
        else:
            return False

    def push(self, item):
        '''If stack is not full, pushes item on stack. 
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''
        if not self.is_full(): #creates a new node, setting the next value to the current head of the list then sets the current head to the new node
            new = Node(item)
            new.next = self.top
            self.top = new
            self.num_items +=1
        else:
            raise(IndexError)

    def pop(self): 
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''
        if not self.is_empty(): #grabs he data of the head, makes the new head the next node then returns the data
            pop = self.top.data
            self.top = self.top.next
            self.num_items -=1
            return pop
        else:
            raise(IndexError)

    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''
        if not self.is_empty(): #grabs the data of the head node
            return self.top.data
        else:
            raise(IndexError)

    def size(self):
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''
        return self.num_items


