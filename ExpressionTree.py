#  File: ExpressionTree.py

#  Description:

#  Student's Name: Fernando Martinez Mojica 

#  Student's UT EID: fmm566

#  Course Name: CS 313E 

#  Unique Number: 50725

#  Date Created: 4/15/19

#  Date Last Modified: 4/15/19

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

class Node():
  def __init__(self,data = None):
    self.data = data
    self.lchild = None
    self.rchild = None
    self.parent = None

class Tree():
  def __init__(self):
    self.root = Node()
    self.num_nodes = 0

  #insert the data
  def create_tree (self,expr):
    ops = ['+','-','*','/','//','%','**']
    vals = expr.split()
    current = self.root
    for item in vals:
      new_node = Node()
      if (item == '('):
        new_node.parent = current
        current.lchild = new_node
        current = current.lchild
      elif (item == ')'):
        current = current.parent
      elif (item in ops):
        current.data = item
        new_node.parent = current
        current.rchild = new_node
        current = current.rchild
      else:
        current.data = item
        current = current.parent
    return 
  
  def evaluate(self,aNode):
    exp = self.post_order(aNode,[])
    exp = exp.strip()
    solution = rpn(exp)
    return solution * -1

  def pre_order (self,aNode,lst):
    if (aNode != None):
      lst.append(aNode.data)
      self.pre_order(aNode.lchild,lst)
      self.pre_order(aNode.rchild,lst)
    s = ''
    for i in range(len(lst)):
      s = s + ' ' + lst[i]
    return s

  def post_order(self,aNode,lst):
    if (aNode != None):
      self.post_order(aNode.lchild,lst)
      self.post_order(aNode.rchild,lst)
      lst.append(aNode.data)
    s = ''
    for i in range(len(lst)):
      s = s + ' ' + lst[i]
    return s

  def in_order(self,aNode,lst):
    if (aNode != None):
      self.in_order(aNode.lchild,lst)
      lst.append(aNode.data)
      self.in_order(aNode.rchild,lst)
    s = ''
    for i in range(len(lst)):
      s = s + ' ' + lst[i]
    return s
  
def rpn(s):
  theStack = Stack()
  operators = ['+','-','*','/','//','%','**']
  tokens = s.split()
  for item in tokens:
    if (item in operators):
      oper1 = theStack.pop()
      oper2 = theStack.pop()
      theStack.push(operate(oper1,oper2,item))
    else:
      theStack.push(float(item))
  return theStack.pop()

def operate(oper1,oper2,token):
  if (token == '+'):
    return oper1 + oper2 
  elif (token == '-'):
    return oper1 - oper2
  elif (token == '*'):
    return oper1 * oper2
  elif (token == '/'):
    return oper1 / oper2
  elif (token == '//'):
    return oper1 // oper2
  elif (token == '%'):
    return oper1 % oper2
  elif (token == '**'):
    return oper1 ** oper2
    
def main():
  inf = open('expression.txt', 'r')
  line = inf.readline()
  expr = line
  inf.close()
  expr = expr.strip()
  expressionTree = Tree()
  expressionTree.create_tree(expr)
  print(expr,'=',expressionTree.evaluate(expressionTree.root))
  print('Prefix Expression:',expressionTree.pre_order(expressionTree.root,[]))
  print('Postfix Expression:',expressionTree.post_order(expressionTree.root,[]))

if __name__ == '__main__':
  main()



    






