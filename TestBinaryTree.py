#  File: TestBinaryTree.py

#  Description:

#  Student Name: Fernando Martinez Mojica

#  Student UT EID: fmm566

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created:

#  Date Last Modified:

class Node():
  def __init__(self,data = None):
    self.data = data
    self.lchild = None
    self.rchild = None
    self.parent = None

class Queue():
  def __init__(self):
    self.queue = []
  def enqueue(self,item):
    self.queue.append(item)
  def dequeue(self):
    return self.queue.pop(0)
  def is_empty(self):
    return (len(self.queue) == 0)
  def size(self):
    return len(self.queue)

class Stack():
  def __init__(self):
    self.stack = []

  #add an item to the top of the stack
  def push (self,item):
    self.stack.append(item)

  #remove an item from the top
  def pop(self):
    return self.stack.pop()

  #check the top of the stack
  def peek(self):
    return self.stack[-1]

  #check if the stack is empty
  def is_empty(self):
    return (len(self.stack) == 0)
  
  #how many elements are in the stack
  def size (self):
    return (len(self.stack))

class Tree():
  def __init__(self):
    self.root = None
    self.numNodes = 0

  def insert(self,data):
    new_node = Node(data)
    self.numNodes += 1
    if (self.root == None):
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (data < current.data):
          current = current.lchild
        else:
          current = current.rchild
      if(data < parent.data):
        parent.lchild = new_node
        new_node.parent = parent
      else:
        parent.rchild = new_node
        new_node.parent = parent

  def num_nodes(self,aNode):
    if (aNode == None):
      return 0
    else:
      lNodes =  1 + self.num_nodes(aNode.lchild)
      rNodes = self.num_nodes(aNode.rchild)
      return (lNodes + rNodes)

  def get_height(self,aNode):
    if (aNode == None):
      return 0
    else:
      lDepth = self.get_height(aNode.lchild) #recursively find the height
      rDepth = self.get_height(aNode.rchild)
      if (lDepth > rDepth):
        return lDepth + 1
      else:
        return rDepth + 1

  #def create_tree(self,a_list):

  def balance_factor(self, aNode):
    lTreeH = self.get_height(aNode.lchild) 
    rTreeH = self.get_height(aNode.rchild)
    return (lTreeH - rTreeH)

  def is_balanced(self,aNode):
    return (self.balance_factor(aNode) == 1) or ((self.balance_factor(aNode) == 0)) or (self.balance_factor(aNode) == -1)

  def print_level(self,aNode):
    if (aNode != None):
      q1 = Queue() #use a queue to traverse the tree save one level
      q2 = Queue() #save the next level
      q1.enqueue(aNode) #intialize the algorithm

      while (q1.size() > 0 or q2.size() > 0):
        s1 = ''
        while (q1.size() > 0):
          val = q1.dequeue()
          s1 += str(val.data) + ' ' #concatenate string
          if (val.lchild != None): #add in children to the other queue in order
            q2.enqueue(val.lchild)
          if (val.rchild != None):
            q2.enqueue(val.rchild)
        print(str(s1))
        s1 = ''

        s2 = ''
        while (q2.size() > 0):
          val = q2.dequeue()
          s2 += str(val.data) + ' '
          if (val.lchild != None):
            q1.enqueue(val.lchild)
          if (val.rchild != None):
            q1.enqueue(val.rchild)
        print(str(s2))
        s2 = ''


def main():
  tree = Tree()
  lst = [1,2,3,4]
  tree.create_tree(lst)
  #lst = [50,30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]
  #for i in range(len(lst)):
  #  tree.insert(lst[i])
  #print(tree.get_height(tree.root))
  #print(tree.num_nodes(tree.root))
  #print(tree.balance_factor(tree.root))
  #print(tree.is_balanced(tree.root))
  tree.print_level(tree.root)

  
if __name__ == '__main__':
  main()
