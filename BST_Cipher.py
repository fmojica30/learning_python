#  File: BST_Cipher.py

#  Description:

#  Student Name: Fernando Martinez Mojica

#  Student UT EID: fmm566

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/22/2019

#  Date Last Modified: 4/22/2019

class Node():
  def __init__(self,data):
    self.data = data
    self.lchild = None
    self.rchild = None

  def __str__(self):
    lchild = ''
    rchild = ''
    if (self.lchild != None):
      lchild = str(self.lchild.data)
    if (self.rchild != None):
      rchild = str(self.rchild.data)
    return 'lchild:',lchild,'Data:',self.data,'rchild:',rchild

class Tree():

  def __init__(self,encrypt_str):
    self.str = encrypt_str
    self.root = None
    self.str = self.str.strip()
    lst = []
    for i in range(len(self.str)):
      lst.append(self.str[i])
    self.str = lst
    for i in range(len(self.str)):
      new_node = Node(self.str[i])
      if (self.str[i] == ' '):
        continue
      else:
        if (self.root == None):
          self.root = new_node
          continue
        else:
          current = self.root
          parent = self.root
          while (current != None):
            parent = current
            if (new_node.data < current.data):
              current = current.lchild
            else:
              current = current.rchild
          if (new_node.data < parent.data):
            parent.lchild = new_node
          else:
            parent.rchild = new_node
    spaceChecker = self.root #making the space the second left for decryption
    for i in range(2):
      spaceChecker = spaceChecker.lchild
    move = spaceChecker.data
    spaceChecker.data = ' '
    self.insert(move) #what what was in the second space in the tree

  def insert(self,ch):
    new_node = Node(ch)
    if (self.root == None):
        self.root = new_node
        return
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (new_node.data < current.data):
          current = current.lchild
        else:
          current = current.rchild
      if (new_node.data < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  def search(self,ch):
    current = self.root
    enc = ''
    while (current != None) and (current.data != ch):
      if (ch < current.data):
        current = current.lchild
        enc += '<' #moving left
      else:
        current = current.rchild
        enc += '>' #moving right
    if (ch == ' '): #checking for space
      return '<<'
    elif (current == self.root): #root case
      return '*'
    elif (current == None): #none case
      return ''
    else:
      return enc

  def traverse(self,st):
    lst = []
    current = self.root
    if (st == '*'): #root case
      return self.root.data
    for i in range(len(st)):
      lst.append(st[i])
    for i in range(len(lst)):
      if (lst[i] == '>'): #moving right
        current = current.rchild
      else: #moving left
        current = current.lchild
    if (current.data == None):
      return ''
    return current.data

  def encrypt(self,st):
    valid = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    enc = ''
    for i in range(len(st)):
      if (st[i] not in valid): #making sure that the string characters are in the valid characters
        continue
      else:
        add = self.search(st[i])
        enc += add
      enc += '!'
    return enc

  def decrypt(self,st):
    st = st.strip()
    lst = st.split('!')
    dec = ''
    for i in range(len(lst) - 1): #checking the characters one by one
      add = self.traverse(lst[i])
      dec += add
    return dec

def main():
  key = str(input('Enter encryption key: '))
  tree = Tree(key)
  print('')

  enc = str(input('Enter string to be encrypted: '))
  encode = tree.encrypt(enc)
  print('Encrypted string:',encode)
  print('')

  dec = str(input('Enter string to be decrypted: '))
  decode = tree.decrypt(dec)
  print('Decrypted string:',decode)
  print('')

if __name__ == '__main__':
  main()
