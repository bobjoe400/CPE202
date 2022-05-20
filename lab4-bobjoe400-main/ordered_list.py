class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        dummy = Node(None)
        self.head = dummy
        self.head.next = dummy
        self.head.prev = dummy

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        if self.head.next == self.head:
            return True
        else:
            return False

    #almost all of my methods in this file use a recursive function to preform their operations, I found this to be
    #a more fun than using a while loop, and also, in some cases, to be marginally more efficient.
    #In most methods we are accessing each node at most once, pop is the only method that is not like this, because
    #we call the size() method which accesses each value to get the size of the list, where we the continue on with
    #a for loop to pop the item at the index. 

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance.  MUST only use the < operator to compare items'''
        new = Node(item)
        if self.is_empty(): #edge case of an empty list
            new.next = self.head
            new.prev = self.head
            self.head.next = new
            self.head.prev = new
            return True
        else:
            def add_r(curNode):
                if new.item == curNode.item: #if the item is already in the list
                    return False
                elif new.item < curNode.item: #if the new item is less than the current item insert it before
                    new.prev = curNode.prev
                    new.next = curNode
                    curNode.prev.next = new
                    curNode.prev = new
                    return True
                elif curNode.next == self.head: #if we are at the end of the list
                    new.next = self.head
                    new.prev = curNode
                    curNode.next = new
                    self.head.prev = new
                    return True
                else: #if we havent reached the end of the list yet, change our current node
                    return add_r(curNode.next)
            return add_r(self.head.next)

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
           returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        def remove_r(node):
            if node.next == self.head and node.item != item: #if the item isn't in the list. because our search
                                                             #function is O(n), we would have a O(n^2) average case
                                                             #on this method if we included it and since in worst
                                                             #case this method will go through the whole list
                                                             #there is no point running search before this recursive
                                                             #method, so you're only accessing each node of the list
                                                             #once
                return False
            elif item == node.item:
                node.prev.next = node.next
                node.next.prev = node.prev
                return True
            else:
                return remove_r(node.next)
        return remove_r(self.head.next)

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        def index_r(node):
            if node.next == self.head and node.item != item: #same reasoning as above for having this
                return None
            elif item == node.item: #stop if we get to the item
                return 0
            else: #If we dont find the item we get a typeError when we try to add None and an int
                try:
                    return 1 + index_r(node.next)
                except TypeError: #we can take advantage of this here to return None incase of Value not Found
                    return None
        return index_r(self.head.next)

    def pop(self, index): #this method is not recursive because it would be easier to do this non-recursively,
                          #since we are not searching for certain values, just iterating to an index
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if index < 0 or index >= self.size(): #edge case of wrong input
            raise IndexError
        else:
            curNode = self.head.next
            for i in range(0,index):
                curNode = curNode.next
            curNode.prev.next = curNode.next
            curNode.next.prev = curNode.prev
            return curNode.item

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        def search_r(node):
            if node.next == self.head and node.item != item: #if we're at the end of the list and the item isnt there
                return False
            else:
                if item == node.item: #if we find the item
                    return True
                else: #iterate to next node
                    return search_r(node.next)
        return search_r(self.head.next)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        if self.is_empty(): #edge case for empty list
            return []
        def python_list_r(node): #simple list creation for forward travelling on the linked list
            if node.next == self.head:
                return [node.item]
            else:
                return [node.item] + python_list_r(node.next)
        return python_list_r(self.head.next)

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        if self.is_empty(): #edge case of empty list
            return []
        def python_list_reversed_r(node): #simple list creation of a reverse traveling of the list
            if node.prev == self.head:
                return [node.item]
            else:
                return [node.item] + python_list_reversed_r(node.prev)
        return python_list_reversed_r(self.head.prev)

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        def size_r(node): #recursive size method
            if node.next == self.head:
                return 0
            else:
                return 1 + size_r(node.next)
        return size_r(self.head)
