firstList = '1 2 3 4 5 6 7 8'.split(' ')
secondList = '2 4 6 8 10 12'.split(' ')

firstSet, secondSet = set(firstList), set(secondList)

print(firstSet.symmetric_difference(secondSet))
