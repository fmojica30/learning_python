#  File: Spiral.py

#  Description:

#  Student Name: Fernando Martinez Mojica

#  Student UT EID: fmm566

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created:1/29/19

#  Date Last Modified:1/31/19

def grid(n):

    len = [0] * n

    grid = [[0] * n for i in range(n)]

    return grid

def main():

    inf = open("spiral.txt","r")

    n = int(inf.readline())

    cap = n ** 2

    mid = int((n / 2) - .5)

    count = 1

    sq = grid(n)

    sq[mid][mid] = count

    #creating the base of the grid up to 7

    count += 1

    step = 1

    sq[mid][mid + step] = count

    count += 1

    sq[mid + step][mid + step] = count

    count += 1

    sq[mid + step][mid] = count

    count += 1

    sq[mid + step][mid - step] = count

    count += 1

    sq[mid][mid - step] = count

    count += 1

    sq[mid - 1][mid - 1] = count

    count += 1

    step = 3

    #posX is sublist

    posX = mid - 1

    #posY is position in the sublist

    posY = mid - 1

    while step != n:

        if step % 2 != 0:

            for i in range(step):

                posY += 1

                sq[posX][posY] = count

                count += 1

            for i in range(step):

                posX += 1

                sq[posX][posY] = count

                count += 1

            step += 1

        else:

            for i in range(step):

                posY -= 1

                sq[posX][posY] = count

                count += 1

            for i in range(step):

                posX -= 1

                sq[posX][posY] = count

                count += 1

            step += 1

    for i in range(n - 1):

        posY += 1

        sq[posX][posY] = count

        count += 1

    # Code to print the spiral in output

    #for i in range(n):

    #    print("\n")

    #    for j in range(n):

    #        print(format(sq[i][j],"4d").center(5),end = "")

    #print("")

    #Beginning of the summation portion

    sumBase = inf.readline()

    while sumBase != "":

        #convert to int after reading to make loop itterable

        sumB = int(sumBase)

        for i in range(n):

            for j in range(n):

                if sq[i][j] == sumB:

                    # coordinates on how to find our wanted value

                    x = i

                    y = j

        #edge is to determine the movement is outside of the range of the list

        edge = n - 1

        # variables are the positions of the number in relation to the original u = up l = left

        # d = down r = right

        u = x - 1

        d = x + 1

        r = y + 1

        l = y - 1

        total = 0

        #summing four cardinal directions

        for i in [u,d]:

            if i <= edge and i >= 0:

                total += sq[i][y]

            else:

                continue

        for i in [r,l]:

            if i <= edge and i >= 0:

                total += sq[x][i]

            else:

                continue

        # summing the diagonals

        for i in [u,d]:

            for j in [l,r]:

                if i <= edge and i >= 0:

                    if j <= edge and j >= 0:

                        total += sq[i][j]

                else:

                    continue

        print(total)

        sumBase = inf.readline()

main()
