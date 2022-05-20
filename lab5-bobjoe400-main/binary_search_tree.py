from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self):
        # Returns empty BST
        self.root = None

    def is_empty(self):
        # returns True if tree is empty, else False
        return self.root is None

    def search(self, key):
        # returns True if key is in a node of the tree, else False
        def search_r(node):
            if node is None:
                return None
            if node.key == key:
                return node
            if node.key < key:
                return search_r(node.right)
            return search_r(node.left)
        return search_r(self.root) is not None

    def insert(self, key, data=None):
        # inserts new node w/ key and data
        # If an item with the given key is already in the BST,
        # the data in the tree will be replaced with the new data
        new = TreeNode(key,data)
        def insert_r(node):
            if node is None:
                return new
            if node.key < key:
                node.right = insert_r(node.right)
            if node.key > key:
                node.left = insert_r(node.left)
            if node.key == key:
                node.data = new.data
            return node
        self.root = insert_r(self.root)

    def find_min(self):
        # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        def find_min_r(node):
            if node is None:
                return None
            if node.left is None:
                return (node.key,node.data)
            return find_min_r(node.left)
        return find_min_r(self.root)

    def find_max(self):
        # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        def find_max_r(node):
            if node is None:
                return None
            if node.right is None:
                return (node.key,node.data)
            return find_max_r(node.right)
        return find_max_r(self.root)

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.is_empty():
            return None
        def tree_height_r(node):
            if node is None:
                return 0
            return max(tree_height_r(node.left),tree_height_r(node.right)) + 1
        return tree_height_r(self.root)-1

    def inorder_list(self):
        # return Python list of BST keys representing in-order traversal of BST
        # DON'T use a default list parameter
        def inorder_list_r(node):
            if node is None:
                return []
            return inorder_list_r(node.left) + [node.key] + inorder_list_r(node.right)
        return inorder_list_r(self.root)

    def preorder_list(self):
        # return Python list of BST keys representing pre-order traversal of BST
        # DON'T use a default list parameter
        def preorder_list_r(node):
            if  node is None:
                return []
            return [node.key] +  preorder_list_r(node.left) + preorder_list_r(node.right)
        return preorder_list_r(self.root)

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        # DON'T attempt to use recursion
        #import pdb; pdb.set_trace()
        q = Queue(25000) # Don't change this!
        if self.is_empty():
            return []
        q.enqueue(self.root)
        list = []
        while q.size() > 0:
            current = q.dequeue()
            list.append(current.key)
            if current.left is not None:
                q.enqueue(current.left)
            if current.right is not None:
                q.enqueue(current.right)
        return list

