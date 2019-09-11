#  File: MagicSquare.py

#  Description:

#  Student Name: Fernando Martinez Mojica   

#  Student UT EID: fmm566

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 3/20/2019

#  Date Last Modified: 3/31/2019

from math import sqrt

def permute(a,lo,hi,cons,catcher):

    side = int(sqrt(len(a)))

    if (lo == hi): 

        check = [[],[],[],[]] #making the square 2 dimensional so the checker works

        counter = 0

        for i in range(side):

            for j in range(side):

                check[i].append(a[counter])

                counter += 1

        if (is_magic(check) == True): #appending it to our list if the square is a magic square

            catcher.append(check)

    else:

        for i in range(lo,hi):

            a[i],a[lo] = a[lo],a[i]

            permute(a,lo + 1, hi,cons,catcher)

            a[i],a[lo] = a[lo],a[i]

    return catcher

def is_magic (a): #checks to see if the square is a magic square

    n = len(a)

    canon_sum = n * (n * n + 1) // 2

    for i in range (len(a)):

        sum_row = 0

        for j in range (len(a[i])):

            sum_row += a[i][j]

        if (sum_row != canon_sum):

            return False

    for j in range(len(a)):

        sum_col = 0

        for i in range(len(a)):

            sum_col += a[i][j]

        if (sum_col != canon_sum):

            return False

    sum_lr = 0

    for i in range(len(a)):

        sum_lr += a[i][i]

    if (sum_lr != canon_sum):

        return False

    sum_rl = 0

    for i in range(len(a)):

        sum_rl += a[i][len(a) - 1 - i]

    if (sum_rl != canon_sum):

        return False

    return True

def main():

    answer = int(input('Enter number of magic squares (2 - 20): '))

    constant = 34

    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

    catcher = []

    magicSqrs1 = permute(nums,0,len(nums),constant,catcher)

    for i in range(answer):

        for j in range(len(magicSqrs2[i])):

            print(format(str(magicSqrs1[i][j][0]),'>2s') + '  ' +format(str(magicSqrs1[i][j][1]),'>2s') + '  ' + format(str(magicSqrs1[i][j][2]),'>2s') + '  ' + format(str(magicSqrs1[i][j][3]),'>2s'))

        print('')


main()