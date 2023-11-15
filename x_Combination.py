from itertools import combinations


def checker(mylist, tar):
    if sum(mylist) == tar:
        return True
    return False


def fourSum( nums, target):
    resultlist = []
    comb = list(set(combinations(nums, 4)))
    for i in range(len(comb)):
        comb[i] = sorted(comb[i])
    newcomb = []
    for element in comb:
        if element not in newcomb:
            newcomb.append(element)
    d = list(map(checker, newcomb, [target for i in range(len(newcomb))]))
    c = list(zip(newcomb, d))
    for i, j in c:
        if j == True:
            resultlist.append(i)
    return resultlist
print(fourSum([-5,5,4,-3,0,0,4,-2],4))

