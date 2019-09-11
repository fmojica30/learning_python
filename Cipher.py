#  File: Cipher.py

#  Description:

#  Student Name: Fernando Martinez Mojica

#  Student UT EID: fmm566

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 2/4/19

#  Date Last Modified: 2/8/19

import math

def encrypt(strng):

    grid = []

    #this is used to check if the length is a perfect square to make the grid

    squared = math.sqrt(len(strng))

    if squared % int(squared) != 0:

        #length of the 2d list as a total

        sizeWanted = (int(squared) + 1) ** 2

        #length that the lists in the 2d list are going to be

        dimension = int(math.sqrt(sizeWanted))

        #how many placeholders to add

        numToAdd = sizeWanted - len(strng)

        #adding the placeholders

        for i in range(numToAdd):

            strng = strng + '*'

        #making the list 2d

        for i in range(dimension):

            grid.append([])

        #adding the characters to the list

        counter = 0

        for j in range(dimension):

            for k in range(dimension):

                grid[j].append(strng[counter])

                counter += 1

        #grid with a transposed message

        transpGrid = [*zip(*grid)]

        #show a transposed grid

        #for i in range(4):

        #   print(transpGrid[i])

        #zip turned it the wrong way but still transposed so now  we fix it

        #make a blank list for storing the transposed list since zip gives us
        #tuples

        transpList = []

        #making tuples into lists

        for i in range(dimension):

            u = list(transpGrid[i])

            transpList.append(u)

        #the zip process makes the transposition a mirror image of what it is
        #supposed to be so here we fix it



        backCount = -1  #need somehow to count backward to reassign positions

        for i in range(dimension):

            backCount = -1 #resetting the backwards counter after each pass

            for j in range(dimension // 2):

                x = transpList[i][j] #saving the next component from the left

                y = transpList[i][backCount] #saving the component its going to switch with

                transpList[i][j] = y #swtiching the components

                transpList[i][backCount] = x

                backCount -=1

        #show a transposed list in the right oreder

        #for i in range(dimension):

        #    print(transpList[i])

        #making the 2d list back into a string

        transpStrng = ''

        for i in range(dimension):

            for j in range(dimension):

                if transpList[i][j] != '*':

                    transpStrng += transpList[i][j]

        return transpStrng

    else:

        #this is copied and pasted from the first if statement
        #without the need to add in the fillers

        dimension = int(math.sqrt(len(strng)))

        for i in range(dimension):

            grid.append([])

        counter = 0

        for j in range(dimension):

            for k in range(dimension):

                grid[j].append(strng[counter])

                counter += 1

        transpGrid = [*zip(*grid)]

        transpList = []

        for i in range(dimension):

            u = list(transpGrid[i])

            transpList.append(u)

        backCount = -1

        for i in range(dimension):

            backCount = -1

            for j in range(dimension // 2):

                x = transpList[i][j]

                y = transpList[i][backCount]

                transpList[i][j] = y

                transpList[i][backCount] = x

                backCount -=1

        transpStrng = ''

        for i in range(dimension):

            for j in range(dimension):

                if transpList[i][j] != '*':

                    transpStrng += transpList[i][j]

        return transpStrng

def decrypt(strng):

    grid = []

    squared = math.sqrt(len(strng))

    dimen = int(squared)

    if squared % dimen != 0:

        #setting the dimensions for the 2d list

        dimension = dimen + 1

        for i in range(dimension):  #making the list

            grid.append([])

        numToAdd = (dimension ** 2) - len(strng) #calculate how many char to add

        spaceStrng = '' #making a string of the amount of chars to add

        for i in range(numToAdd):

            spaceStrng += '*'

        #beginning of counting backwards in the list and seeing how many rows
        #are needed to to fit all of the filler chars

        rowsNeeded = 1 #how many rows we need

        while numToAdd > dimension: #calculating how many rows are needed

            numToAdd -= dimension

            rowsNeeded += 1

        negCounter = -1 #counter used to count backwards for the 2d list

        for i in range(len(spaceStrng)): #loop to append the

            grid[negCounter].append(spaceStrng[i])

            if negCounter == -dimension: #resets the backwards row counter to -1
                                         #whenever it goes past its max
                negCounter = 0

            negCounter -= 1

        #appending the rest of the string to the list in backwards fashion and
        #down e.g start at top right corner and go down the row and then the next
        #row

        counter = 0

        for i in range(dimension):

            if len(grid[i]) < dimension:

                add = dimension - len(grid[i])

                for j in range(add):

                    grid[i].append(strng[counter])

                    counter += 1

        #tester to show the grid

        #for i in range(dimension):

        #    print(grid[i])

        #making the string to return

        decrptStrng = ''

        for j in range(-1,-dimension-1,-1):

                for i in range(dimension):

                    if grid[i][j] != '*':

                        decrptStrng += grid[i][j]

        return decrptStrng

    else:

        dimension = dimen

        for i in range(dimension):

            grid.append([])

        counter = 0

        for i in range(dimension):

            for j in range(dimension):

                grid[i].append(strng[counter])

                counter += 1

        #display grid

        #for i in range(dimension):

        #    print(grid[i])

        decrptStrng = ''

        for i in range(-1,(-dimension - 1),-1):

            for j in range(dimension):

                if grid[j][i] != '*':

                    decrptStrng += grid[j][i]

        return decrptStrng

def main():

    inf = open("encrypt.txt","r")

    loops = int(inf.readline())

    line = inf.readline()

    line = line.strip()

    print("Encryption:")

    for i in range(loops):

        print(encrypt(line))

        line = inf.readline()

        line = line.strip()

    print(" ")

    #decription portion

    infD = open("decrypt.txt","r")

    loopsD = int(infD.readline())

    lineD = infD.readline()

    lineD = lineD.strip()

    print("Decryption:")

    for i in range(loopsD):

        print(decrypt(lineD))

        lineD = infD.readline()

        lineD = lineD.strip()

main()
