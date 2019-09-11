#  File: TopoSort.py

#  Description:

#  Student Name: Fernando Martinez Mojica

#  Student UT EID: fmm566

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/29/19

#  Date Last Modified: 5/3/19

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
    self.in_degrees = None

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

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len(self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # do the depth first search in a graph
  def dfs (self, v, lst):
    # create the Stack
    theStack = Stack()

    # mark the vertex v as visited and push it on the stack
    #(self.Vertices[v]).visited = True
    #lst.append(self.Vertices[v])
    theStack.push (v)

    # visit the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1): 
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        lst.append(self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us reset the flags
    nVert = len(self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

    return lst

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

  def has_cycle(self):
    nVert = len(self.Vertices)
    for i in range(nVert):
      check = self.Vertices[i] 
      lst = self.dfs(i,[])
      for k in range(len(lst)): #if the label if the origin is in the dfs then there is a loop
        if (lst[k].label == check.label):
          return True
    return False

  def get_in_degrees(self):
    nVert = len(self.Vertices)
    degrees = []
    for i in range(nVert):
      count = 0
      for j in range(nVert):
        if (self.adjMat[j][i] != 0): #sums up all of the edges leading to it by going down columns of adjaecncy matrix
          count += 1
      degrees.append(count)
    self.in_degrees = degrees
    return 

  def toposort(self):
    self.get_in_degrees() #get the in degrees to start out with
    if (self.has_cycle() != True): #make sure it does not have a cycle
      nVert = len(self.Vertices)
      theQueue = Queue()
      theList = []
      end_checker = [0 for i in range(nVert)] #how i know there are no more vertices with degrees higher than 0
      if (self.in_degrees == None):
        return
      while (self.in_degrees != end_checker):
        for i in range(nVert): #find all of the vertices with degree 0
          if (self.in_degrees[i] == 0) and (self.Vertices[i].visited == False): 
            theList.append(i)
            self.Vertices[i].visited = True
        for i in theList:
          for j in range(nVert):
            if (self.adjMat[i][j] > 0): #subtract one from the adjacency matrix so the degree drops
              self.adjMat[i][j] -= 1
        theList.sort()
        for i in theList:
          theQueue.enqueue(self.Vertices[i].label) 
        theList = []
        self.get_in_degrees()
    ans = []
    while (theQueue.is_empty() != True):
      ans.append(theQueue.dequeue())
    return ans

      

def insert(list, n): 
  # Searching for the position 
  for i in range(len(list)): 
      if list[i] > n: 
          index = i 
          break
  # Inserting n in the list 
  list = list[:i] + [n] + list[i:] 
  return list

def main():
  inf = open("./topo.txt","r")

  test = Graph()

  nVert = inf.readline()
  nVert = int(nVert.strip())
  for i in range(nVert):
    line = inf.readline()
    line = str(line.strip())
    test.add_vertex(line)
  
  edges = int(inf.readline())

  for i in range(edges):
    new_edge = inf.readline()
    new_edge = new_edge.split()
    start = int(test.get_index(new_edge[0]))
    finish = int(test.get_index(new_edge[1]))
    weight = 1
    test.add_directed_edge(start, finish, weight)
  
  print ("\nAdjacency Matrix")
  for i in range (nVert):
    for j in range (nVert):
      print (test.adjMat[i][j], end = " ")
    print()
  print()
  
  #test.add_directed_edge(7,0,1)

  print("new")
  print ("\nAdjacency Matrix")
  for i in range (nVert):
    for j in range (nVert):
      print (test.adjMat[i][j], end = " ")
    print()
  print()

  test.get_in_degrees()

  #test if a directed graph has a cycle
  print(test.has_cycle())

  print(test.toposort())

main()