# recursive, does subset sum of certain target exist
def existsSubsetSumNaive(numSet, target):
    if target == 0:
        return True 
    elif len(numSet) == 0 or target < 0:
        return False
    else:
        newTarget = target - numSet[0]
        return existsSubsetSumNaive(numSet[1:], newTarget) or existsSubsetSumNaive(numSet[1:], target)

# recursive, find list of lists of paths that correspond to a subset sum of certain target
def findSubsetSumNaive(numSet, target):
    total = []
    def sumAccum(numSet, target, path):
        if target == 0:
            total.append(path)
        elif len(numSet) != 0 and target > 0:
            newTarget = target - numSet[0]
            sumAccum(numSet[1:], newTarget, path + [numSet[0]])
            sumAccum(numSet[1:], target, path)
    sumAccum(numSet, target, [])
    return total

list1 = [1, 2, 3, 4]
print(str(list1) + " has subset-sum of 3: " + str(existsSubsetSumNaive(list1, 3)) \
    + " of " + str(findSubsetSumNaive(list1, 3)))
list2 = [-1, 2, 3, 5, 6, 7]
print(str(list2) + " has subset-sum of 4: " + str(existsSubsetSumNaive(list2, 4)) \
    + " of " + str(findSubsetSumNaive(list2, 4)))
print(str(list1) + " has subset-sum of 10: " + str(existsSubsetSumNaive(list1, 10)) \
    + " of " + str(findSubsetSumNaive(list1, 10)))
print(str(list1) + " has subset-sum of 11: " + str(existsSubsetSumNaive(list1, 11)) \
    + " of " + str(findSubsetSumNaive(list1, 11)))

# DP, does subset sum exist for certain target
def existsSubsetSumDP(numSet, target):
    existsMemo = ([False for i in range(target + 1)] for j in range(len(numSet) + 1)])

    for i in range(len(numSet + 1)):
        existsMemo[i][0] = True
    
    for tar in range(target + 1):
        for index in range(1, len(numSet)):
            if numSet[index - 1] == tar:
                existsMemo[index][tar] == True
            elif tar - numSet[index - 1] >= 0:
                existsMemo[index][tar] == (existsMemo[index - 1][tar] or existsMemo[index][tar - numSet[index - 1]])
            else:
                existsMemo[index][tar] == existsMemo[index - 1][tar]

    return existsMemo[len(numSet)][target]

# DP for find subset sum is sub-optimal in space?

