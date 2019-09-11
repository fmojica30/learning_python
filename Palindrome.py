#  File: Palindrome.py

#  Description:

#  Student Name: Fernando Martinez Mojica

#  Student UT EID: fmm566

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 2/20/19

#  Date Last Modified: 2/20/19

def is_palindrome(s): #define if a string is a palindrome

    for i in range(len(s)//2):

        if s[i] != s[-i-1]:

            return False

    return True

def make_palindrome(s): #function for making a palindrome out of a word

    newWord = '' #initial counter for the new word to see where to do the
                 #palindrome
    if len(s) == 1: #single letter palindrome case

        return s

    elif len(s) == 2: #2 letter palindrome case easy solve

        if s[0] == s[1]:

            return s

        else: #append the last letter to the front

            newWord += s[1]

            newWord += s

            newPalindrome = newWord

            return newPalindrome

    else: #all other length cases

        if is_palindrome(s) == True: #if the word is already a palindrome

            return s

        else:

            for i in range(len(s)):

                newWord += s[i]

                #determine if the set of letters we are looking at is a palindrome

                if (is_palindrome(newWord)) and (len(newWord) > 3):

                    if i == len(s): #the whole word is a palindrome

                        return newPalindrome

                    else: #creating a palindrome shortest

                        appender = '' #define letters to append at the front

                        adders = s[i+1:] #all of the letters required to append

                        adders = list(adders)

                        order = list(reversed(adders)) #putting them in order

                        for j in order:

                            newLetter = j

                            appender += newLetter

                        newPalindrome = appender + s

                        return newPalindrome

                elif newWord == s: #case where the word does not include a
                                   #palindrome
                    adder = ''

                    for i in range(-1,(-len(s) - 1),-1):

                        adder += s[i] #adding letters to the front from the back
                                      #of the word until we get a palindrome

                        newPalindrome = adder + newWord

                        if is_palindrome(newPalindrome):

                            return newPalindrome

                        else:

                            continue

                else:

                    continue

def main():

    inf = open('palindrome.txt','r')

    line = inf.readline()

    line = line.strip()

    while line != '':

        print(make_palindrome(line))

        line = inf.readline()

        line = line.strip()



main()
