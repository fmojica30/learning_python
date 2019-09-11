#  File: Triangle.py

#  Description:

#  Student's Name: Fernando Martinez Mojica

#  Student's UT EID: fmm566

#  Course Name: CS 313E 

#  Unique Number: 50725

#  Date Created: 4/5/2019

#  Date Last Modified: 4/9/2019

from timeit import timeit

def paths(a,lo,pos,sum,catcher): #makes all the paths and sees their sum
  if (lo == (len(a) - 1)): 
    catcher.append(sum)
  else:
    paths(a,lo + 1,pos,sum + a[lo + 1][pos],catcher)
    paths(a,lo + 1,pos + 1,sum + a[lo + 1][pos + 1],catcher)
  return catcher

def paths2(a,lo,pos,sum):
  if (lo == (len(a)- 1)):
    sum += a[lo][pos]
    return 
  else:
    path1 = paths2(a,lo + 1,pos,sum + a[lo + 1][pos])
    path2 = paths2(a,lo + 1,pos + 1,sum + a[lo + 1][pos + 1])
    return max(path1,path2)
    

#returns the greatest path sum using exhaustive search
def brute_force(grid):
  firstVal = grid[0][0] #initializes the sum as beginning with the first value
  catcher = []
  vals = paths(grid,0,0,firstVal,catcher)
  maxNum = max(vals)
  return maxNum

#returns the greatest path sum using the greedy approach
def greedy(grid):
  total = 0
  position = 0 #set the initial position to 0 

  for i in range(len(grid)):
    if (len(grid[i]) == 1): #if you are at the top just add it 
        total += grid[i][0]
        continue
    else:
      #set and compare the two options that would be under the position
      opt1 = grid[i][position] 
      opt2 = grid[i][position + 1]
      if (opt1 > opt2):
        total += opt1 #if it is the same keep the position
      elif (opt1 < opt2):
        total += opt2
        position = position + 1 #change the position if you go with the one next to it
      else:
        total += opt1 #if they are the same number add the easiest one

  return total 

#returns the greatest path sum using divide and conquer (recursive) 
#def divide_conquer(grid):
#  ans = paths2(grid,0,0,0)
#  return ans

#returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
  for i in reversed(range(len(grid) - 1)): #goes from the bottom of the grid to the top
    for j in range(len(grid[i])):
      grid[i][j] += max(grid[i + 1][j], grid[i + 1][j + 1]) #compares the sums that follow and picks the maximum
  return str(grid[0][0])

#reads the file and returns a 2-D list that represents the triangle
def read_file():
  inf = open('triangle.txt','r')
  line = inf.readline()
  line = inf.readline()
  grid = []

  while line != '':
    list = line.split()
    list2 = []
    for i in range(len(list)):
      a = int(list[i])
      list2.append(a)
    grid.append(list2)
    line = inf.readline()
  return grid

def main ():
  # read triangular grid from file
  grid = read_file()
  # output greatest path from exhaustive search
  bruteTotal = brute_force(grid)
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  #print time taken using exhaustive search
  print('The greates path sum through the exhaustive search is',str(bruteTotal)+'.')
  print('The time taken for the exhaustive search is',times,'seconds.')

  # output greatest path from greedy approach
  greedyTotal = greedy(grid)
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  #print time taken using the greedy approach
  print('The greates path sum through the greedy search is',str(greedyTotal)+'.')
  print('The time taken for the greedy approach is',times,'seconds.')

  # output greatest path from divide-and-conquer approach
  #divideTotal = divide_conquer(grid)
  #times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  #times = times / 10
  #print time taken using divide-and-conquer approach
  print('The greates path sum through divide and conquer is','none'+'.')
  print('The time taken for divide and conquer is','none','seconds.')

  # output greatest path from dynamic programming 
  dynamicTotal = dynamic_prog(grid)
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming
  print('The greates path sum through dynamic programming is',str(dynamicTotal)+'.')
  print('The time taken for dynamic programming is',times,'seconds.')
  
if __name__ == "__main__":
  main()

  