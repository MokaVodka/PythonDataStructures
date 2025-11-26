import time

# If script doesn't run, check path in util.py
from util import gen_random_list


# -- Catch-all run call --
# nsumAlgo: nsum algorithm to use
# sizeRange: range for three-sum lst sizes
# repeat: repeat run x times to calculate average time
# printAvgTime: print average time of three-sum with lst size to console
# returns lstSizes and lstTimes
def nsum_run(nsumAlgo, sizeRange, repeat=1, printAvgTime=False):
    sizes, times = [], []

    for size in sizeRange:
        # Feedback console print
        if printAvgTime:
            print(f'List size: {size}', end='')

        sizes.append(size)
        totalTime = 0

        # Repeat runs to get average time
        for _ in range(0, repeat):
            lst = gen_random_list(size)

            timeStart = time.time()
            nsumAlgo(lst)
            timeElapsed = time.time() - timeStart

            totalTime += timeElapsed

        avgTime = totalTime/repeat
        times.append(avgTime)

        # Feedback console print
        if printAvgTime:
            print(f' | Average time ({repeat} runs): {round(avgTime, 3)}')

    return sizes, times


# -- Sort triplet from smallest to largest --
# O(1)
def triplet_sort(tripletTuple):
    t1, t2, t3 = tripletTuple
    if t3 < t2:
        t2, t3 = t3, t2
    if t2 < t1:
        t1, t2 = t2, t1
    if t3 < t2:
        t2, t3 = t3, t2

    return t1, t2, t3


# -- Calculate three sum of lst and add valid triplets to result --

# Should be O(n^3)
def threesum_brute(lst, sum=0):
    lstSize = len(lst)
    result = set()

    # Check sum for each element-triplet
    for i in range(0, lstSize - 2):
        n1 = lst[i]

        for j in range(i + 1, lstSize - 1):
            n2 = lst[j]

            # n1, n2, n3 should be distinct, skip if same integers
            if n1 == n2:
                continue

            for k in range(i + 2, lstSize):
                n3 = lst[k]
                if n1 == n3 or n2 == n3:
                    continue

                if n1 + n2 + n3 == sum:
                    # Avoid dupes
                    result.add(triplet_sort((n1, n2, n3)))

    return list(result)


# Should be O(n^2)
def threesum_pointers(lst, sum=0):
    lst = sorted(lst)
    lstSize = len(lst)
    result = set()

    # Three pointers:
    # i, main one going through the loop
    # leftP, starting right after the main pointer
    # rightP, starting at the end of loop
    for i in range(0, lstSize - 2):
        leftP, rightP = i + 1, lstSize - 1

        while leftP < rightP:
            n1, n2, n3 = lst[i], lst[leftP], lst[rightP]
            remainder = n1 + n2 + n3 - sum

            # Move rightP left if sum is larger target sum
            # or if rightP is not distinct
            if remainder > 0 or n3 == n1 or n3 == n2:
                rightP -= 1

            # Move leftP right if sum is smaller target sum
            # or if leftP is not distinct
            elif remainder < 0 or n2 == n1:
                leftP += 1

            # Add triplet if sum is same as target sum
            # Move pointers
            elif remainder == 0:
                result.add((n1, n2, n3))
                leftP += 1
                rightP -= 1

    return list(result)


# Should be O(n^2)
def threesum_caching(lst, sum=0):
    result = set()
    lstSize = len(lst)

    # Store previously examined elements in found
    # Add triplet when 2/3-sum's compliment is part of found set
    for i in range(0, lstSize - 1):
        found = set()
        n1 = lst[i]

        for j in range(i + 1, lstSize):
            n2 = lst[j]
            n3 = sum - n1 - n2

            if n3 in found:
                # Avoid dupes
                result.add(triplet_sort((n1, n2, n3)))
            else:
                found.add(n2)

    return list(result)
