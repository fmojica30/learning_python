#  File: Geom.py

#  Description:

#  Student Name:Fernando Martinez Mojica

#  Student UT EID: fmm566

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 2/9/19

#  Date Last Modified: 2/9/19

import math

class Point (object):
  # constructor
  # x and y are floats
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance
  # other is a Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # get a string representation of a Point object
  # takes no arguments
  # returns a string
  def __str__ (self):
    return '(' + str(self.x) + ", " + str(self.y) + ")"

  # test for equality
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    tol = 1.0e-16
    return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
  # constructor
  # x, y, and radius are floats
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute cirumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if a circle is strictly inside this circle
  def circle_inside (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) < self.radius

  # determine if a circle c overlaps this circle (non-zero area of overlap)
  # but neither is completely inside the other
  # the only argument c is a Circle object
  # returns a boolean
  def circle_overlap (self, c):
      dstnc = self.center.dist(c.center)
      return dstnc < (self.radius + c.radius)


  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle
  # the only argument, r, is a rectangle object
  def circle_circumscribe (self, r):
      changeX = (r.lr.x - r.ul.x) / 2
      changeY = (r.ul.y - r.lr.y) / 2
      newX = r.ul.x + changeX
      newY = r.ul.y - changeY
      newCenter = Point(newX,newY)
      newRadius = math.hypot(r.ul.x - newCenter.x,r.ul.y - newCenter.y)
      return Circle(newRadius,newCenter.x,newCenter.y)


  # string representation of a circle
  # takes no arguments and returns a string
  def __str__ (self):
    return "Radius: " + str(self.radius) + ", Center: " + str(self.center)

  # test for equality of radius
  # the only argument, other, is a circle
  # returns a boolean
  def __eq__ (self, other):
    tol = 1.0e-16
    return abs(self.radius - other.radius) < tol

class Rectangle (object):
  # constructor
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

  # determine length of Rectangle (distance along the x axis)
  # takes no arguments, returns a float
  def length (self):
      return self.lr.x - self.ul.x

  # determine width of Rectangle (distance along the y axis)
  # takes no arguments, returns a float
  def width (self):
      return self.ul.y - self.lr.y

  # determine the perimeter
  # takes no arguments, returns a float
  def perimeter (self):
      return (self.length() * 2) + (self.width() * 2)

  # determine the area
  # takes no arguments, returns a float
  def area (self):
      return (self.length() * self.width())

  # determine if a point is strictly inside the Rectangle
  # takes a point object p as an argument, returns a boolean
  def point_inside (self, p):
      if (self.lr.y < p.y <self.ul.y) and (self.ul.x < p.y < self.lr.x):
          return True
      else:
          return False

  # determine if another Rectangle is strictly inside this Rectangle
  # takes a rectangle object r as an argument, returns a boolean
  # should return False if self and r are equal
  def rectangle_inside (self, r):
      if (self.ul.x < r.ul.x) and (self.ul.y > r.ul.y):
          if (self.lr.x > r.lr.x) and (self.lr.y < r.ul.y):
              return True
          else:
              return False
      else:
          return False

  #checks to see if all points of the rectangle are outisde
  def rectangle_outside(self,r):
      r_ur = Point(r.lr.x,r.ul.y)
      r_ll = Point(r.ul.x,r.lr.y)
      if self.point_inside(r.ul) == False:
          if self.point_inside(r.lr) == False:
              if self.point_inside(r_ur) == False:
                  if self.point_inside(r_ll) == False:
                      return True
                  else:
                      return False
              else:
                  return False
          else:
              return False
      else:
         return False

  # determine if two Rectangles overlap (non-zero area of overlap)
  # takes a rectangle object r as an argument returns a boolean
  def rectangle_overlap (self, r):
      if (self.rectangle_inside(r) == False) and (self.rectangle_outside(r) == False):
          return True
      #these two conditions check for rect that have 2 sides between on on the rectangle
      elif (self.ul.x <= r.ul.x <= self.lr.x) == True and (self.ul.x <= r.lr.x <= self.lr.x) == True:
          return True
      elif (self.lr.y <= r.ul.y <= self.ul.y) == True and (self.lr.y <= r.lr.y <= self.ul.y) == True:
          return True
      else:
          return False

  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  # takes a circle object c as input and returns a rectangle object
  def rectangle_circumscribe (self, c):
      ul = Point(c.center.x,c.center.y)
      ul.x = ul.x - c.radius
      ul.y = ul.y + c.radius
      lr = Point(c.center.x,c.center.y)
      lr.x = lr.x + c.radius
      lr.y = lr.y - c.radius
      return Rectangle(ul.x,ul.y,lr.x,lr.y)

  # give string representation of a rectangle
  # takes no arguments, returns a string
  def __str__ (self):
    return "UL: " + str(self.ul) + ", LR: " + str(self.lr)

  # determine if two rectangles have the same length and width
  # takes a rectangle other as argument and returns a boolean
  def __eq__ (self, other):
     return (self.length() == other.length()) and (self.width() == other.width())

def readline(inf):
  line = inf.readline()
  line = line.strip()
  vals = line.split()
  return vals
  
def main():
  # open the file geom.txt
  inf = open("geom.txt",'r')
  # create Point objects P and Q
  vals = readline(inf)
  pX = float(vals[0])
  pY = float(vals[1])
  p = Point(pX,pY)
  vals = readline(inf)
  qX = float(vals[0])
  qY = float(vals[1])
  q = Point(qX,qY)
  # print the coordinates of the points P and Q
  print('Coordinates of P:',p)
  print('Coordinates of Q:',q)
  # find the distance between the points P and Q
  print("Distance between P and Q:",p.dist(q))
  # create two Circle objects C and D
  vals = readline(inf)
  cRadius = float(vals[0])
  cX = float(vals[1])
  cY = float(vals[2])
  c = Circle(cRadius,cX,cY)
  vals = readline(inf)
  dRadius = float(vals[0])
  dX = float(vals[1])
  dY = float(vals[2])
  d = Circle(dRadius,dX,dY)
  # print C and D
  print('Circle C:',c)
  print('Circle D:',d)
  # compute the circumference of C
  print('Circumference of C:',c.circumference())
  # compute the area of D
  print('Area of D:',d.area())
  # determine if P is strictly inside C
  if c.point_inside(p) == True:
    print('P is inside C')
  else:
    print('P is not inside C')
  # determine if C is strictly inside D
  if d.circle_inside(c) == True:
    print('C is inside D')
  else:
    print('C is not inside D')
  # determine if C and D intersect (non zero area of intersection)
  if d.circle_overlap(c) == True:
    print('C does intersect D')
  else:
    print('C does not intersect D')
  # determine if C and D are equal (have the same radius)
  if c == d:
    print('C is equal to D')
  else:
    print('C is not equal to D')
  # create two rectangle objects G and H
  vals = readline(inf)
  g = Rectangle(float(vals[0]),float(vals[1]),float(vals[2]),float(vals[3]))
  vals = readline(inf)
  h = Rectangle(float(vals[0]),float(vals[1]),float(vals[2]),float(vals[3]))
  # print the two rectangles G and H
  print('Rectangle G:',g)
  print('Rectangle H:',h)
  # determine the length of G (distance along x axis)
  print('Length of G:',g.length())
  # determine the width of H (distance along y axis)
  print('Width of H:',h.width())
  # determine the perimeter of G
  print('Perimeter of G:',g.perimeter())
  # determine the area of H
  print('Area of H:',h.area())
  # determine if point P is strictly inside rectangle G
  if g.point_inside(p) == True:
    print('P is inside G')
  else:
    print('P is not inside G')
  # determine if rectangle G is strictly inside rectangle H
  if h.rectangle_inside(g) == True:
    print('G is inside H')
  else:
    print('G is not inside H')
  # determine if rectangles G and H overlap (non-zero area of overlap)
  if g.rectangle_overlap(h) == True:
    print('G does overlap H')
  else:
    print('G does not overlap H')
  # find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle
  c1 = Circle()
  c2 = c1.circle_circumscribe(g)
  print('Circle that circumscribes G:',c2)
  # find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle
  r1 = Rectangle()
  r2 = r1.rectangle_circumscribe(d)
  print('Rectangle that circumscribes D',r2)
  # determine if the two rectangles have the same length and width
  if g == h:
    print('Rectangle G is equal to H')
  else:
    print('Rectangle G is not equal to H')
  # close the file geom.txt
  inf.close()
# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
