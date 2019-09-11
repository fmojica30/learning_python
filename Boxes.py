#  File: Boxes.py

#  Description:

#  Student Name: Fernando Martinez Mojica

#  Student UT EID: fmm566

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 3/15/19

#  Date Last Modified: 3/18/19

def list_line_intsSort(inf): #reads the line and makes a list of values for easy reading

    line = inf.readline()

    line = line.strip()

    list = line.split()

    num_list = []

    for i in list:

        num_list.append(int(i))

    num_list.sort()

    return num_list

def does_box_fit(box1,box2): #box one is the smaller one and box 2 is the larger one

    return (box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])

def subsets(a,b,idx,catcher): #creates and stores all the possible subets if the list and returns catcher which is a list of combinations

    if (idx >= len(a)):

        catcher.append(b)

    else:

        c = b[:]

        b.append(a[idx])

        subsets(a,b,idx + 1,catcher)

        subsets(a,c,idx + 1,catcher)

    return catcher

def do_boxes_nest(a): #checks to see if the boxes of a combination nest all inside of one and other

    for i in range(len(a) - 1):

        if (does_box_fit(a[i],a[i + 1])) == False:

            return False

    return True

def find_largest_set(a): #finds the length of the largest set for narrowing down our searhces

    largest = 1

    for i in range(len(a)):

        if (do_boxes_nest(a[i]) == True):

            if (len(a[i]) >= largest):

                largest = len(a[i])

    return largest

def box_removal(a,max,new): #returns all boxes that are of the largest length that nest and that do nest

    for i in range(len(a)):

        if((len(a[i]) == max) and (do_boxes_nest(a[i]) == True)):

            new.append(a[i])

    return new

def main():

    #open the file for reading

    inf = open('boxes.txt','r')

    numBoxes = inf.readline()

    numBoxes.strip()

    numBoxes = int(numBoxes)

    boxList = []

    for i in range(numBoxes):

        box = list_line_intsSort(inf)

        boxList.append(box)

    boxList.sort()

    inf.close()

    idx = 0

    bask = []

    combins = []

    combos = subsets(boxList,bask,idx,combins)

    biggestNestLen = find_largest_set(combos)

    #example = [[14,27,62],[16,40,90],[53,56,91],[57,82,94]]

    catcher = []

    longestCombos = box_removal(combos,biggestNestLen,catcher)

    print('Largest Subset of Nesting Boxes')

    for i in range(len(longestCombos)):

        for j in range(len(longestCombos[i])):

            print(longestCombos[i][j])

        print('')

main()

    




