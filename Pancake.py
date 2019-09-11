# File: Pancake.py

# Description:

# Student's Name: Fernando Martinez Mojica

# Student's UT EID: fmm566

# Course Name: CS 313E

# Unique Number: 50725

# Date Created: 3/5/18

# Date Last Modified: 3/8/18

def list_line_ints(inf): #reads the line and makes a list of values for easy assignment

    line = inf.readline()

    line = line.strip()

    list = line.split()

    num_list = []

    for i in list:

        num_list.append(int(i))

    return num_list

def flip(n,stack):

    if n == 1: #case where the max value is already at the top and going to flip

        stack.reverse()

        return stack

    else: #flips the list above the specified value and keeps the other part static

        user = n * -1

        listToFlip = stack[:user +1]

        restOfList = stack[user + 1:]

        listToFlip.reverse()

        for i in restOfList:

            listToFlip.append(i)

        return listToFlip


def sorted(a): #determine of the array is sorted

    for i in range(len(a) - 1):

        if a[i] > a[i + 1]:

            return False

    return True

def main():

    inf = open('pancake.txt','r')

    stack = list_line_ints(inf)

    while stack != []:

        stackStr = ''

        for i in range(len(stack)): #making the array a string for output

            stackStr = stackStr + str(stack[i]) + ' '

        print(stackStr)

        moves = [] #made to keep track of the moves

        spot = len(stack) #used to calculate the spot where the flip occurs

        negCounter = 0 #counts backwards in order to keep track of the pancakes
        #already sorted
        for i in range(len(stack)):

            if sorted(stack) == True: #breaks whenever the stack is sorted

                moves.append('0')

                break

            if negCounter == 0: #the first move to be made

                maxIndex = stack.index(max(stack))

                if maxIndex == 0:

                    moves.append('1')

                    stack = flip(1,stack)

                    negCounter -= 1

                else: #moving the max value to the top and then to the next potition on the bottom

                    flipSpot = spot - maxIndex

                    #print(flipSpot)

                    moves.append(str(flipSpot))

                    stack = flip(flipSpot,stack)

                    moves.append('1')

                    stack = flip(1,stack)

                    negCounter -= 1

            else:

                maxIndex = stack.index(max(stack[:negCounter]))

                if maxIndex == 0:
                    #checks to see if the last two numbers are in order to prevent unnecessary moves
                    if negCounter == (-len(stack) + 1):

                        if sorted(stack) == True:

                            moves.append('0')

                            break

                        else: #moves them arround if necessary

                            moves.append(str((-len(stack) + 1) * -1))

                            move = (-len(stack) + 1) * -1

                            stack = flip(move,stack)

                            moves.append('0')

                            break

                    else:

                        move = (negCounter * -1) + 1

                        moves.append(str(move))

                        stack = flip(move,stack)

                        negCounter -= 1

                else: #moves the max to the top and then to the next bottom position

                    bottom = (negCounter * -1) + 1

                    flipSpot = spot - maxIndex

                    moves.append(str(flipSpot))

                    stack = flip(flipSpot,stack)

                    moves.append(str(bottom))

                    stack = flip(bottom,stack)

                    negCounter -= 1

        moveStr = ''

        for i in range(len(moves)):

            moveStr += moves[i] + ' '

        print(moveStr)

        stack = list_line_ints(inf)

main()
