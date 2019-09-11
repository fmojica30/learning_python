#  File: Intervals.py

#  Description:

#  Student Name:Fernando Martinez Mojica

#  Student UT EID: fmm566

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created:2/1/19

#  Date Last Modified:2/4/19

#This function makes a list of tuples out of the values of the file

def makeList():

    inf = open("intervals.txt","r")

    line = inf.readline()

    list_tuples = []

    while line != "":

        nums = line.split()

        nums_list = []

        for i in range(2):

            nums_int = int(nums[i])

            nums_list.append(nums_int)

            nums_tuple = tuple(nums_list)

        list_tuples.append(nums_tuple)

        line = inf.readline()

    return list_tuples

#funciton that collapses down the intervals and seperates the ones that do
#and the ones the do not collapse are left in the list

def seperate(tuples):

    #makes it so i can assign new values to the ranges and move them

    checker = []

    for i in range(len(tuples)):

        x = list(tuples[i])

        checker.append(x)

    #this is the index of the checker that we are on

    index = 0

    #go over it twice to check for any remainders

    for k in range(2):

        #first one in comparison

        for i in checker:

            # is the second one in comparison

            for j in checker:

                if i[0] < j[0] and i[1] > j[0]:

                    if i[0] > j[0]:

                        i[0] = j[0]

                        checker.pop(checker.index(j))

                    elif i[0] < j[0] and i[1] > j[1]:

                        checker.pop(checker.index(j))

                    else:

                        i[1] = j[1]

                        checker.pop(checker.index(j))

                elif  i[1] > j[1] and i[0] < j[1]:

                    if i[0] > j[0]:

                        i[0] = j[0]

                        checker.pop(checker.index(j))

                    elif i[0] < j[0] and i[1] > j[1]:

                        checker.pop(checker.index(j))

                    else:

                        i[1] = j[1]

                        checker.pop(checker.index(j))

                elif i[0] == j[0] and i[1] < j[1]:

                    i[1] = j[1]

                    checker.pop(checker.index(j))

                elif i[1] == j[1] and i[0] < j[0]:

                    i[0] = j[0]

                    checker.pop(checker.index(j))

    return checker

#selection sort to give them an order

def sort(list):

    for i in range(len(list) - 1):

        currentMin = list[i][0]

        currentMinIndex = i

        for j in range(i+1, len(list)):

            if currentMin > list[j][0]:

                currentMin = list[j][0]

                currentMinIndex = j

                #swap them if they are not the same

                if currentMinIndex != i:

                    #to save the value before changing the assignment and making two the same

                    change = list[j]

                    list[currentMinIndex] = list[i]

                    list[i] = change

    return(list)

def sort_size(list):

    for i in range(len(list) - 1):

        currentMin = abs(abs(list[i][1]) - abs(list[i][0]))

        currentMinIndex = i

        for j in range(i+1, len(list)):

            if currentMin > abs(abs(list[j][1]) - abs(list[j][0])):

                currentMin = abs(abs(list[j][1]) - abs(list[j][0]))

                currentMinIndex = j

                #swap them if they are not the same

                if currentMinIndex != i:

                    #to save the value before changing the assignment and making two the same

                    change = list[j]

                    list[currentMinIndex] = list[i]

                    list[i] = change

    return list


def main():

    intervals = makeList()

    list = sort(seperate(intervals))

    tuples = []

    tuplesSize = []

    #converting the list back to tuples

    for i in range(len(list)):

        interval = tuple(list[i])

        tuples.append(interval)

    print("Non-Intersecting Intervals:")

    for i in range(len(tuples)):

        print(tuples[i])

    sizes = sort_size(list)

    for i in range(len(sizes)):

        int = tuple(sizes[i])

        tuplesSize.append(int)

    print("Non-Intersecting Intervals in order of size:")

    for i in range(len(tuplesSize)):

        print(tuplesSize[i])
        
main()
