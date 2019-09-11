class Wheel(object):
  def __init__(self,lst = [0,1,2,3,4,5,6,7,8,9],pos = 0):
    self.wheel = lst
    self.position = pos
  
  def scroll_up(self):
    if (self.pos == 9):
      self.pos = 0
    else:
      self.pos += 1

  def scroll_down(self):
    if (self.pos == 0):
      self.pos = 9
    else:
      self.pos -= 1

  def up_count(self,target):
    count = 0
    while (self.wheel[self.pos] != target):
      self.scroll_up()
      count += 1
    return count
   
  def down_count(self,target):
    count = 0
    while (self.wheel[self.pos] != target):
      self.scroll_down()
      count -= 1
    return count

  def find 

    


