from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search
import operator

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []

class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        # This method should call add_vertex and add_edge!!!
        file = open(filename)
        self.graph = dict()
        for line in file.readlines():
            vertecies = line.split()
            self.add_vertex(vertecies[0])
            self.add_vertex(vertecies[1])
            self.add_edge(vertecies[0],vertecies[1])
        file.close()

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        # Should be called by init
        if not self.graph.get(key):
            self.graph[key] = Vertex(key)

    def add_edge(self, v1, v2):
        # Should be called by init
        '''v1 and v2 are vertex ID's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.graph.get(v1).adjacent_to.append(v2)
        self.graph.get(v2).adjacent_to.append(v1)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the ID. If ID is not in the graph, return None'''
        return self.graph.get(key)

    def get_vertices(self):
        '''Returns a list of ID's representing the vertices in the graph, in ascending order'''
        return sorted(self.graph.keys())

    def conn_components(self): 
        '''Return a Python list of lists.  For example: if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.'''
        #This method MUST use Depth First Search logic!
        visited = dict()
        components = []
        for key in self.graph.keys():
            visited[key] = False
        for key in self.graph.keys():
            if not visited[key]:
                temp_comp = []
                stack = Stack(len(self.graph))
                stack.push(key)
                while not stack.is_empty():
                    currv = stack.pop()
                    if visited[currv]:
                        continue
                    visited[currv] = True
                    temp_comp.append(currv)
                    adjacents = self.graph.get(currv).adjacent_to
                    for adj in adjacents:
                        if not visited[adj]:
                            stack.push(adj)
                components.append(sorted(temp_comp))
        return sorted(components, key=operator.itemgetter(0))

    def is_bipartite(self):
        '''Return True if the graph is bipartite and False otherwise.'''
        #This method MUST use Breadth First Search logic!
        colors = dict()
        for key in self.graph.keys():
            colors[key] = None
        queue = Queue(len(self.graph.keys()))
        for key in self.graph.keys():
            if colors[key] is None:
                colors[key] = 1
                queue.enqueue(key)
                while not queue.is_empty():
                    vector = queue.dequeue()  
                    for adj in self.graph.get(vector).adjacent_to:
                        if not colors[adj]:
                            colors[adj] = 1-colors.get(vector)
                            queue.enqueue(adj)
                        elif colors[adj] == colors[vector]:
                                return False
        return True
