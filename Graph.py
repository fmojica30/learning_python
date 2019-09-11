#  File: Graph.py

#  Description:

#  Student Name: Fernando Martinez Mojica 

#  Student UT EID: fmm566

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/28/19

#  Date Last Modified: 4/28/19

import copy

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack is empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))


class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)


class Graph (object):
  def __init__ (self):
    self.Vertices = []      # list of Vertex objects
    self.adjMat = []        # adjacency matrix

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given a label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if (not self.has_vertex(label)):
      self.Vertices.append (Vertex (label))
      
      # add a new column in the adjacency matrix
      nVert = len (self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append(0)

      # add a new row for the new Vertex
      new_row = []
      for i in range (nVert):
        new_row.append (0)
      self.adjMat.append (new_row)
  
  def get_edge_weight(self,fromVertexLabel, toVertexLabel):
    #find from index
    for i in range(len(self.Vertices)):
      if ((self.Vertices[i]).label == fromVertexLabel):
        from_index = i
    #find to index
    for i in range(len(self.Vertices)): 
      if ((self.Vertices[i].label) == toVertexLabel):
        to_index = i
    #get from to edge weight
    if (self.adjMat[from_index][to_index] > 0):
      return self.adjMat[from_index][to_index]
    #get to from edge weight
    if (self.adjMat[to_index][from_index] > 0):
      return self.adjMat[to_index][from_index]
    return -1

  def get_neighbors(self, vertexLabel):
    neighbor_index = []
    neighbors = []
    #get index
    for i in range(len(self.Vertices)):
      if ((self.Vertices[i].label) == vertexLabel):
        vertex_index = i
    #find the indeces of all the neighbors
    for i in range(len(self.Vertices)):
      if (self.adjMat[vertex_index][i] > 0):
        neighbor_index.append(i)
    #find the labels of all the neighbors
    for item in neighbor_index:
      neighbors.append(self.Vertices[item])
    return neighbors

  def get_vertices(self):
    return copy.deepcopy(self.Vertices)

  def delete_edge(self,fromVertexLabel, toVertexLabel):
    #find index of from 
    for i in range(len(self.Vertices)):
      if ((self.Vertices[i]).label == fromVertexLabel):
        from_index = i
    #find index of to 
    for i in range(len(self.Vertices)): 
      if ((self.Vertices[i].label) == toVertexLabel):
        to_index = i
    #delete from to direction
    if (self.adjMat[from_index][to_index] != 0):
      self.adjMat[from_index][to_index] = 0
    #delete to from direction
    if (self.adjMat[to_index][from_index] != 0):
      self.adjMat[to_index][from_index] = 0

    return
  
  def delete_vertex(self, vertexLabel):
    #find index
    for i in range(len(self.Vertices)):
      if ((self.Vertices[i]).label == vertexLabel):
        vert_index = i
    #delete all edges to the vertex
    for i in range(len(self.adjMat)):
      self.adjMat[i].pop(vert_index)
    self.adjMat.pop(vert_index) #delete all edges from the vertex
    self.Vertices.pop(vert_index) #delete vertex from the graph
    
  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len(self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # do the depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack()

    # mark the vertex v as visited and push it on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1): 
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us reset the flags
    nVert = len(self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do the breadth first search in a graph
  def bfs (self, v):
    # create the Queue
    theQueue = Queue()
    current = self.Vertices[v]
    current.visited = True
    theQueue.enqueue(current)
    c_index = self.get_index(current.label)
    print(current.label)
    while (not(theQueue.is_empty())):
      #visit the next unvisited vertex and add it to the queue
      for i in range(len(self.Vertices)):
        if (self.adjMat[c_index][i] != 0) and (self.Vertices[i].visited != True):
          self.Vertices[i].visited = True
          print(self.Vertices[i].label)
          theQueue.enqueue(self.Vertices[i])
      #set new vertex to look from after finishing the other search
      current = theQueue.dequeue()
      c_index = self.get_index(current.label)

    nVert = len(self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

    return


def main():
  # create the Graph object
  cities = Graph()

  # open the file for reading
  in_file = open ("./graph.txt", "r")

  # read the number of Vertices
  num_vertices = int((in_file.readline()).strip())
  #print (num_vertices)

  # add the vertices to the list
  for i in range (num_vertices):
    city = (in_file.readline()).strip()
    #print (city)
    cities.add_vertex (city)

  # read the edges and add them to the adjacency matrix
  num_edges = int ((in_file.readline()).strip())
  #print (num_edges)

  for i in range (num_edges):
    edge = (in_file.readline()).strip()
    #print (edge)
    edge = edge.split()
    start = int(edge[0])
    finish = int(edge[1])
    weight = int(edge[2])

    cities.add_directed_edge (start, finish, weight)
  
  # read the starting vertex for dfs and bfs
  start_vertex = (in_file.readline()).strip()
  #print ("Start Vertex:",start_vertex)

  # get the index of the starting vertex
  start_index = cities.get_index (start_vertex)
  #print (start_index)

  # do the depth first search
  print ("\nDepth First Search from " + start_vertex)
  cities.dfs (start_index)
  print()

  # do the breadth first search
  print ("\nBreadth First Search from " + start_vertex)
  cities.bfs (start_index)
  print()

  print("Deletion of an Edge from " + start_vertex + " " + "Miami")
  cities.delete_edge("Houston","Miami")

  # print the adjacency matrix
  print ("\nAdjacency Matrix")
  for i in range (num_vertices):
    for j in range (num_vertices):
      print (cities.adjMat[i][j], end = " ")
    print()
  print()

  print("Deletion of a Vertex " + "Seattle")
  cities.delete_vertex("Seattle")
  print()
  print("List of Vertices")
  print()
  for i in range(len(cities.Vertices)):
    print(cities.Vertices[i])
  print()
  num_vertices = len(cities.Vertices)
  print("Adjacency Matrix")
  for i in range (num_vertices):
    for j in range (num_vertices):
      print (cities.adjMat[i][j], end = " ")
    print()

  #close the file
  in_file.close()


main()