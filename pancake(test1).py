or i in range(len(stack)):

    maxIndex = stack.index(max(stack))

    if sorted(stack) == True:

        moves.append('0')

        break

    elif maxIndex == 0:

        stack = flip(maxIndex,stack)

        moves.append(str(len(sortedList) + 1))

        sortedList.insert(0,stack.pop(-1))

    else:

        moves.append(str(spot - maxIndex))

        stack = flip(maxIndex,stack)

        moves.append(str(len(sortedList) + 1))

        maxIndexTwo = stack.index(max(stack))

        stack = flip(maxIndexTwo,stack)

        sortedList.insert(0,stack.pop(-1))

print(sortedList)

print('moves: ',moves)

print('')
