from sys import argv
from typing import List
from stack_array import *

def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * one vertex per line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''

    class Vertex:
        def __init__(self, adjacent = []):
            self.in_degree = 0
            self.adjacent = adjacent

        def get_adjacent_vals(self):
            return self.adjacent

        def add_adjacent(self,value):
            self.adjacent.extend(value)
        
        def get_degree(self):
            return self.in_degree
        
        def change_degree(self, change):
            self.in_degree += change
            if self.in_degree == 0:
                return False
            return True

    if len(vertices) == 0:
        raise ValueError("input contains no edges")
    if len(vertices)%2 !=0:
        raise ValueError("input contains an odd number of tokens")

    adjacencyList = dict()
    for i in range(0,len(vertices),+2):
        d1 = vertices[i]
        d2 = vertices[i+1]
        v1 = Vertex([d2])
        v2 = Vertex([d1])
        v2.change_degree(1)
        for data in ([d1,v1],[d2,v2]):
            if not adjacencyList.get(data[0]):
                adjacencyList[data[0]] = data[1]
            else:
                adjacencyList.get(data[0]).change_degree(data[1].get_degree())
                adjacencyList.get(data[0]).add_adjacent(data[1].get_adjacent_vals())

    sort_stack = Stack(len(vertices))
    for key, value in adjacencyList.items():
        if value.get_degree() == 0:
            sort_stack.push(key)
    
    retString = ""
    checked = 0
    while not sort_stack.is_empty():
        checked += 1
        vertex = sort_stack.pop()
        retString += str(vertex) + "\n"
        for i in adjacencyList.get(vertex).get_adjacent_vals():
            if not adjacencyList.get(i).change_degree(-1):
                sort_stack.push(i)

    if checked != len(adjacencyList):
        raise ValueError("input contains a cycle")
    
    return retString.rstrip('\n')

# 100% Code coverage NOT required
def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()
    
    vertices = []
    for line in f:
        vertices += line.split()
       
    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)
    
if __name__ == '__main__': 
    main()
