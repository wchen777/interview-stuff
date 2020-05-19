# find all subsets of given set of numbers
def subsets(numSet):
    sets = [[]]
    for i, num in enumerate(numSet):
        if i == 0:
            sets.append([num])
        else:
            sets.extend(list(map(lambda x: x + [num], sets)))
    return sets

print(str(subsets([1, 2, 3])))
print(str(subsets([1, 2, 3, 4])))
print(str(subsets([1, 2, 3, 4, 5])))
