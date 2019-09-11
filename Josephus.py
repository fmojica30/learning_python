#  File: Josephus.py

#  Description:

#  Student Name: Fernando Martinez Mojica

#  Student UT EID: fmm566

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/10/19

#  Date Last Modified: 4/14/19

class Link():
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

class CircularList():
  def __init__(self):
    self.first = None
    self.count = 0

  def insert(self,data):
    new_link = Link(data,self.first) #initialize the link to have the first as the next
    self.count += 1
    #find the last link
    current = self.first
    if (current == None): #if the first link is the one being made make the next itself
      self.first = new_link
      new_link.next = self.first
      return
    for i in range(self.count - 2): #find the last link and make it the next one
      current = current.next
    current.next = new_link

  def find(self,data):
    current = self.first
    if (current == None):
      return None
    for i in range(self.count): #searches through only once 
      if (current.data == data):
        return current
      else:
        current = current.next
    return None

  def delete(self,data):
    previous = self.first
    current = self.first
    if (current == None):
      return None
    if (current.data == data): #if the first one is the one being deleted
      current = current.next
      self.first = current
    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
        current = current.next
    previous.next = current.next
    self.count -= 1
    return 
  
  def delete_after(self,start,n):
    current = self.first
    while (current.data != start):
      current = current.next
    while (self.count >= 1): #goes until there is only one value left
      for i in range(n - 1):
        current = current.next
      delete = current
      print(delete.data) #prints the output
      current = current.next
      self.delete(delete.data)

  def __str__(self):
    string = ''
    current = self.first
    for i in range(self.count):
      dta = current.data
      if (i == 0):
        string += str(dta)
      else:
        string += '  '
        string += str(dta)
      current = current.next
    return string

def read_file():
  inf = open('josephus.txt','r')
  line = inf.readline()
  vals = []
  while line != '':
    vals.append(int(line)) 
    line = inf.readline()
  return vals

def main():
  lst = CircularList()
  nums = read_file()
  for i in range(1,nums[0] + 1):
    lst.insert(i)
  lst.delete_after(nums[1],nums[2])

main()
  
  
    