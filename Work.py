#  File: Work.py

#  Description:

#  Student Name: Fernando Martinez Mojica

#  Student UT EID: fmm566

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 3/1/19

#  Date Last Modified: 3/4/19

def list_line_ints(inf): #reads the line and makes a list of values for easy assignment

    line = inf.readline()

    line = line.strip()

    list = line.split()

    num_list = []

    for i in list:

        num_list.append(int(i))

    return num_list

def create_list(n): #creating a list of possible values for v
                    #since it has to be less than n
    list = []

    for i in range(n+1):

        list.append(int(i))

    return list

def lines_written(v,k): #returns the number of lines written

    count = v

    p = 1 #exponent counter

    formula = v // (k ** p) #calculating how many line each iteration makes

    while True: #loop so it will continue until we are adding less than 1

        if formula >= 1:

            count += formula #counting the lines total

            p += 1 #increasing the exponent

            formula = v // (k ** p)

        else:

            break #exiting and returning when the number of lines is < 0

    return count


def main():

    inf = open('work.txt','r')

    number = list_line_ints(inf)

    testCases = number[0]

    nK = list_line_ints(inf)

    for i in range(testCases): #replace 1 with test cases

        n = nK[0]

        k = nK[1]

        nums = create_list(n)

        hi = len(nums) - 1

        lo = 0

        while (lo <= hi):

            mid = (hi + lo) // 2

            x = lines_written(nums[mid],k)

            if (x > n):

                hi = mid - 1

            elif (x < n):

                lo = mid + 1

            else:

                break

        #the following statements are to make sure we are printing the correct
        #value, if the amount is too small go with the one above it since or too
        #big go below it

        if x < n:

            print(mid + 1)

        elif x > n:

            print(mid - 1)

        else:

            print(mid)

        nK = list_line_ints(inf) #moving on to the next line

main()
