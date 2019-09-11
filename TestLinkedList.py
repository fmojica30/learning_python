#  File: TestLinkedList.py

#  Description:

#  Student Name: Fernando Martinez Mojica

#  Student UT EID: fmm566

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/9/2019

#  Date Last Modified: 4/12/2019

from random import randint

class Link():
  def __init__(self, data, next = None):
    self.data = data
    self.next = next
  
  def __str__(self):
    return 'present'

class LinkedList():
  def __init__(self):
    self.first = None
    self.num_links = 0

  #get the number of links
  def get_num_links(self):
    return self.num_links
  
  def insert_first(self, data):
    new_link = Link(data)
    new_link.next = self.first
    self.first = new_link
    self.num_links += 1

  def insert_last(self,data):
    new_link = Link(data)
    #find the last link
    current = self.first
    if (current == None):
      self.first = new_link
      self.num_links += 1
      return
    while (current.next != None):
      current = current.next
    current.next = new_link
    self.num_links += 1

  #insert in order of an ascending list
  def insert_in_order (self, data):
    new_link = Link(data) #make the new link from the data
    current = self.first
    previous = self.first
    if (current == None):
      self.first = new_link
      self.num_links += 1
      return
    if (current.data > data):
      self.insert_first(data)
      self.num_links += 1
      return
    if (self.num_links == 1):
      if (current.data > data):
        self.insert_first(data)
        self.num_links += 1
        return 
      else:
        self.insert_last(data)
        self.num_links += 1
        return
    while ((current != None) and (current.data <= data)): #find where the link goes
      previous = current
      current = current.next
    previous.next = new_link #insert the new link
    new_link.next = current
    self.num_links += 1
    return

  #search in an unordered list
  def find_unordered (self, data): 
    current = self.first
    if (current == None):
      return None
    while (current.data != data): #exhaustive search until we find it 
      if (current.next == None):
        return None
      else:
        current = current.next
    return current

  #Search in an ordered list, return None is not found
  def find_ordered(self,data):
    current = self.first
    if (current == None):
      return None
    while (current != None):
      if (current.data < data):
        current = current.next
      elif (current.data == data):
        return current
      elif (current.data > data): #if the data in the list is higher than the item we want to find then the item is not in it
        return None

  def delete_link(self,data):
    previous = self.first
    current = self.first
    if (current == None):
      return None
    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
        current = current.next
    if (current == self.first):
      self.first = self.first.next
      self.num_links -= 1
    else:
      previous.next = current.next
      self.num_links -= 1
    return current

  #str
  def __str__(self):
    current = self.first
    string = ''
    while (current != None):
      if (current == self.first): #initializes the string with the beginning data
        dat = str(current.data)
        string += dat
        current = current.next
      else: #adds in the data with 2 space between it and the previous one
        dat = '  ' + str(current.data)
        string += dat
        current = current.next
    return string
      
  #copy list
  def copy_list (self):
    new_list = LinkedList() #initialize the new list
    current = self.first
    if (current == None):
      return new_list
    while (current != None):
      dta = current.data 
      new_list.insert_last(dta) #make a new link from the data of the other one
      current = current.next
    return new_list

  #reverse list
  def reverse_list (self):
    new_list = LinkedList()
    current = self.first
    if (current == None):
      return new_list
    while (current != None):
      dta = current.data
      new_list.insert_first(dta) #pushes the data in order it came out of the first list reversing it
      current = current.next
    return new_list

  #sort list
  def sort_list (self):
    new_list = LinkedList()
    current = self.first
    values = []
    while (current != None):
      val = current.data
      values.append(val)
      current = current.next
    for item in values:
      new_list.insert_in_order(item)
    return new_list

  #is sorted
  def is_sorted (self):
    current = self.first
    current = current.next
    previous = self.first
    if (current == None):
      return True
    while (current != None):
      if (current.data >= previous.data): #basic sort move on if they are in order
        previous = current
        current = current.next
      else:
        return False
    return True

  #is empty
  def is_empty(self):
    current = self.first
    if (current == None): #if the list is empty 
      return True
    else:
      return False 

  #merge two sorted lists return new list in ascending order
  def merge_list (self, other):
    new_list = LinkedList()
    current1 = self.first
    current2 = other.first
    #merging in the usual way by comparing and moving it into a new list
    while ((current1 != None) and (current2 != None)):
      if (current1.data < current2.data):
        new_list.insert_last(current1.data)
        current1 = current1.next
      elif (current1.data > current2.data):
        new_list.insert_last(current2.data)
        current2 = current2.next
      else:
        new_list.insert_last(current1.data)
        current1 = current1.next
        current2 = current2.next
    #inserting all of the rest at the end
    if (current1 != None):
      while (current1 != None):
        new_list.insert_last(current1.data)
        current1 = current1.next
    if (current2 != None):
      while (current2 != None):
        new_list.insert_last(current2.data)
        current2 = current2.next
    return new_list
      
  #Test if two lists are equal return True or False
  def is_equal (self, other):
    current1 = self.first
    current2 = other.first
    if ((current1 == None) and (current2 == None)):
      return True
    elif ((current1 == None) and (current2 != None)):
      return False
    elif ((current1 != None) and (current2 == None)):
      return False
    while ((current1 != None)):
      if (current1.data == current2.data):
        current1 = current1.next
        current2 = current2.next
      else:
        return False
    if (current2 != None):
      return False
    return True

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def remove_duplicates (self):
    checker = self.first
    current = self.first
    previous = self.first
    current = current.next
    while(checker != None):
      current = checker
      current = current.next
      previous = checker
      while(current != None):
        if (current.data == checker.data):
          current = current.next
          previous.next = current
        else:
          previous = current
          current = current.next
      checker = checker.next
    return True
    
def random_ordered(n):
 lst = []
 lst.append(randint(1,10))
 for i in range(n):
    num = randint(1,(15 + (10*i)))
    while (num <= lst[i]):
      num = randint(1,(15 + (10*i)))
    lst.append(num)
 return lst

def random_unordered(n):
  lst = []
  lst.append(randint(1,10))
  for i in range(n):
    num = randint(1,(15 + (10*i)))
    lst.append(num)
  return lst

def main():

  linkedList = LinkedList()
  for i in range(4):
    linkedList.insert_first(i)
  for i in range(5,10):
    linkedList.insert_first(i)

  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  print('')
  print('Testing __str__')
  print(linkedList)
  print('')
  print('Testing insert_first')
  linkedList.insert_first(10)
  print('Linked list:',linkedList)

  # Test method insert_last()
  print('')
  print('Testing insert_last')
  linkedList.insert_last(-1)
  print('Linked list:',linkedList)

  # Test method insert_in_order()
  print('')
  print('Testing insert_in_order')
  linkedList13 = LinkedList()
  values = [1,6,9,23,56,78,90,99]
  for i in range(len(values)):
    linkedList13.insert_last(values[i])
  print(linkedList13)
  print('List being used:',linkedList13)
  x = randint(2,100)
  print('Inserting:',x)
  linkedList13.insert_in_order(x)
  print(linkedList13)
  

  # Test method get_num_links()
  print('')
  print('Testing get_num_links')
  num_links = linkedList.get_num_links()
  print('Length of Linked List:',num_links)

  # Test method find_unordered()
  # Consider two cases - data is there, data is not there 
  print('')
  print("Testing method find_unordered")
  linkedList2 = LinkedList()
  for i in range(10):
    num = randint(1,10)
    linkedList2.insert_last(num)
  print('Linked list:',linkedList2)
  print('Result of finding 4 in the list:',linkedList2.find_unordered(4))
  print('Result of finding 13 in the list:',linkedList2.find_unordered(13))

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there
  print('')
  print('Testing find_ordered')
  linkedList4 = LinkedList()
  for i in range(10,8,-1):
    linkedList4.insert_first(i)
  for i in range(7,0,-1):
    linkedList4.insert_first(i)
  print('Linked List:',linkedList4)
  print('Result of find_ordered(4):',linkedList4.find_ordered(4))
  print('Result of find_ordered(8):',linkedList4.find_ordered(8))

  # Test method delete_link()
  # Consider two cases - data is there, data is not there
  print('')
  print('Testing delete_link')
  print('List tested:',linkedList)
  print('Test delete_link(9):',linkedList.delete_link(9))
  print('List result:',linkedList)

  # Test method copy_list()
  print('')
  print('Testing copy method')
  linkedList3 = linkedList.copy_list()
  print('Linked list being copied',linkedList)
  print('Copy of Linked List:',linkedList3)

  # Test method reverse_list()
  print('')
  print('Testing reverse_list method')
  print('List being reversed:',linkedList)
  print(linkedList.reverse_list())

  # Test method sort_list()
  print('')
  print('Testing method sort_list()')
  linkedList12 = LinkedList()
  values = random_unordered(10)
  for i in values:
    linkedList12.insert_first(i)
  print("List being ordered:",linkedList12)
  linkedList14 = linkedList12.sort_list()
  print('Result:',linkedList14)
  


  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  print('')
  linkedList8 = LinkedList()
  for i in range(10,0,-1):
    linkedList8.insert_first(i)
  linkedList9 = LinkedList()
  linkedList9.insert_first(9)
  for i in range(10,5,-1):
    linkedList9.insert_first(i)
  linkedList9.insert_first(4)
  linkedList9.insert_first(5)
  linkedList9.insert_first(3)
  linkedList9.insert_first(1)
  linkedList9.insert_first(2)
  print('Testing is_sorted')
  print('Test when the list is sorted:',linkedList8.is_sorted())
  print('List tested:',linkedList8)
  print('Test when the list is not sorted:',linkedList9.is_sorted())
  print('List tested:',linkedList9)

  # Test method is_empty()
  print('')
  print('Testing is_empty')
  linkedList10 = LinkedList()
  print('Test when the list is empty:',linkedList10.is_empty())
  print('List tested',linkedList10)
  print('Test when list is not empty:',linkedList.is_empty())
  print('List tesed:',linkedList)

  # Test method merge_list()
  print('')
  print('Testing method merge_list')
  linkedList_merge = LinkedList()
  linkedList_merge2 = LinkedList()
  nums1 = random_ordered(5)
  nums2 = random_ordered(5)
  for item in nums1:
    linkedList_merge.insert_last(item)
  for item in nums2:
    linkedList_merge2.insert_last(item)
  print('List one being merged:',linkedList_merge)
  print('List two being merged:',linkedList_merge2)
  mergedList = linkedList_merge.merge_list(linkedList_merge2)
  print('Merged List:',mergedList)


  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  print('')
  print('Testing is_equal')
  linkedList5 = LinkedList()
  linkedList6 = LinkedList()
  linkedList7 = LinkedList()
  for i in range(10):
    linkedList5.insert_first(i)
  for i in range(10):
    linkedList7.insert_first(i)
  for i in range(10):
    num = randint(1,10)
    linkedList6.insert_first(num)
  print('Testing when the lists are equal:',linkedList5.is_equal(linkedList7))
  print('Testing when lists are not equal:',linkedList5.is_equal(linkedList6))
  
  # Test remove_duplicates()
  print('')
  print('Testing remove_duplicates')
  linkedList11 = LinkedList()
  for i in range(10):
    linkedList11.insert_first(randint(1,10))
  print('List tested:',linkedList11)
  linkedList11.remove_duplicates()
  print('Outcome:',linkedList11)
  print('')
  print('')

if __name__ == "__main__":
  main()


