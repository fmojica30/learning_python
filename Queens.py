#  File: Queens.py

#  Description:

#  Student Name: Fernando Martinez Mojica

#  Student UT EID: fmm566

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 03/28/2019

#  Date Last Modified: 4/1/2019

import copy

class Queens (object):

    # initialize the board

  def __init__ (self, n = 8):

    self.board = []

    self.n = n

    self.solutions = []

    for i in range (self.n):

      row = []

      for j in range (self.n):

        row.append ('*')

      self.board.append (row)

  # print the board

  def get_solutions(self):

    return self.solutions

  def print_board (self):

    for i in range (self.n):

      for j in range (self.n):

        print (self.board[i][j], end = ' ')

      print ()

  # check if no queen captures another
  def is_valid (self, row, col):

    for i in range (self.n):

      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):

        return False

    for i in range (self.n):
      
      for j in range (self.n):

        row_diff = abs (row - i)

        col_diff = abs (col - j)

        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):

          return False

    return True

  # do a recursive backtracking solution
  def recursive_solve (self, col):

    if (col >= self.n):

      return 

    else:

      for i in range (self.n):

        if (self.is_valid(i, col)):

          self.board[i][col] = 'Q'
          #if the board gets to the column where it is at the end then there is a solution and add it to the solutions
          if (col == (self.n - 1)):

            self.add_solution(self.board)
            #backtracking
            self.board[i][col] = '*'

            return

          self.recursive_solve(col + 1)
          #backtracking
          self.board[i][col] = '*'

  def add_solution(self,board): #adding the solutions to the counter

    correct = copy.deepcopy(self.board)

    self.solutions.append(correct)

  def solve (self):

    for i in range (self.n):

      if (self.recursive_solve(i)):
        
        return 

def check_solutions(a,size): #making sure all of the solutions are valid with enough queens in them

  newList = []

  for i in range(len(a)):

    test = True

    for j in range(size):

      if ('Q' in a[i][j]):

        continue

      else:

        test = False

    if test == True:

      newList.append(a[i])

  return newList


def main():
  # create a regular chess board
  n = int(input('Enter the size of the board: '))

  game = Queens (n)

  game.solve()

  solves = game.get_solutions()

  checker = check_solutions(solves,n)

  print('Number of solutions: ',int(len(checker)))

main()

  
