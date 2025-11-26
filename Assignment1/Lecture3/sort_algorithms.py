import time

# If script doesn't run, check path in util.py
from util import gen_random_list


# -- Catch-all run call --
# sortAlgo: sort algorithm to use
# sizeRange: range for three-sum lst sizes
# repeat: repeat run x times to calculate average time
# printAvgTime: print average time of three-sum with lst size to console
# lst: pass a preexisting list
# returns lstSizes and lstTimes
def sort_run(sortAlgo, sizeRange, repeat=1, printAvgTime=False, lst=None):
    sizes = [size for size in sizeRange]
    times = []

    for size in sizes:
        # Feedback console print
        if printAvgTime:
            print(f'List size: {size}', end='')

        totalTime = 0

        # Repeat runs to get average time
        for _ in range(0, repeat):
            if lst is None:
                lst = gen_random_list(size)

            timeStart = time.time()

            try:
                sortAlgo(lst)
            except RecursionError:
                print(f'Exceeded max recursion depth at list size {size}')
                print('Stopping process')
                while len(times) < len(sizes):
                    times.append(-1)
                return times

            timeElapsed = time.time() - timeStart

            totalTime += timeElapsed

        avgTime = totalTime/repeat
        times.append(avgTime)

        # Feedback console print
        if printAvgTime:
            print(f' | Average time ({repeat} runs): {round(avgTime, 3)}')

    return sizes, times


def sort_single_run(sortAlgo, lst):
    timeStart = time.time()
    sortAlgo(lst)
    timeElapsed = time.time() - timeStart
    return timeElapsed


# -- O(n^2) sorts --

def selection_sort(lst):
    lst = lst.copy()
    lstSize = len(lst)

    for i in range(0, lstSize - 1):

        # Update swapP when smaller number found
        swapP = i
        for j in range(i + 1, lstSize):
            if lst[j] < lst[swapP]:
                swapP = j

        # swapP is now pointing to the smallest element
        # Swap elements, don't bother if no swap occured
        if swapP != i:
            lst[i], lst[swapP] = lst[swapP], lst[i]

    return lst


def bubble_sort(lst):
    lst = lst.copy()
    lstSize = len(lst)

    # Swap unordered pairs until there is no changes
    changes = 1
    while changes > 0:
        changes = 0
        for i in range(0, lstSize - 1):
            if lst[i] > lst[i + 1]:
                changes += 1
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

    return lst


def insertion_sort(lst):
    lst = lst.copy()
    lstSize = len(lst)

    for i in range(1, lstSize):
        # Element to insert
        iElement = lst[i]
        insertP = i

        # Move backwards in list
        for backwardP in range(i - 1, -1, -1):

            # Override (shift) current element to later element
            # Update insertion point
            if lst[backwardP] > iElement:
                lst[backwardP + 1] = lst[backwardP]
                insertP = backwardP

            # ...Until current element is smaller than insertion element
            else:
                break

        # Override (insert) iElement to insertion point
        lst[insertP] = iElement

    return lst


# -- O(n*log(n))  sorts --

# -- Merge sort
def merge(lst, start, end):
    middle = (start + end) // 2
    leftP = start
    rightP = middle + 1

    while leftP <= middle and rightP <= end:

        # Value is in correct place, check next element
        if lst[leftP] <= lst[rightP]:
            leftP += 1

        # Insertion sort, but insert point is leftP
        else:
            # Element to insert
            iElement = lst[rightP]

            # Move backwards in list
            # Override (shift) current element to later element
            for i in range(rightP, leftP, -1):
                lst[i] = lst[i - 1]

            # Override (insert) iElement to leftP
            lst[leftP] = iElement

            # Because we inserted iElement into left half,
            # middle is shifted right by 1
            leftP += 1
            middle += 1
            rightP += 1


def merge_sort_recursion(lst, start, end):
    middle = (start + end) // 2

    if start < end:
        merge_sort_recursion(lst, start, middle)
        merge_sort_recursion(lst, middle + 1, end)
        merge(lst, start, end)


def merge_sort(lst):
    lst = lst.copy()
    lstSize = len(lst)
    merge_sort_recursion(lst, 0, lstSize - 1)
    return lst


# -- Quick sort

def pivot_swap(lst, start, end, pivot):
    # Pointer to swap lower elements to start of list
    swapP = start

    # Swap list elements to lower and higher
    for i in range(start, end):
        if lst[i] <= pivot:

            # Swap if i != swapP
            if i != swapP:
                lst[swapP], lst[i] = lst[i], lst[swapP]

            # Prevent index out of range
            swapP += 1

    # Higher starts at swapP, clamped for invalid index
    higherStartP = swapP
    if higherStartP >= end:
        higherStartP = end - 1
    return higherStartP


def quick_sort_recursion(lst, start, end, pivot):
    if end - start > 1:
        higherStartP = pivot_swap(lst, start, end, pivot)

        pivot = lst[higherStartP - 1]
        quick_sort_recursion(lst, start, higherStartP, pivot)

        pivot = lst[end - 1]
        quick_sort_recursion(lst, higherStartP, end, pivot)


def quick_sort(lst):
    lst = lst.copy()
    lstSize = len(lst)
    if lstSize <= 0:
        return lst

    pivot = lst[lstSize - 1]
    quick_sort_recursion(lst, 0, lstSize, pivot)
    return lst


# -- Improved quick sort

def get_median(lst, start, end):
    middle = (start + end) // 2
    median = (lst[start] + lst[end - 1] + lst[middle]) // 3
    return median


def improved_quick_sort_recursion(lst, start, end, pivot):
    if end - start > 1:
        higherStartP = pivot_swap(lst, start, end, pivot)

        median = get_median(lst, start, higherStartP)
        improved_quick_sort_recursion(lst, start, higherStartP, median)

        median = get_median(lst, higherStartP, end)
        improved_quick_sort_recursion(lst, higherStartP, end, median)


def improved_quick_sort(lst):
    lst = lst.copy()
    lstSize = len(lst)
    if lstSize <= 0:
        return lst

    median = get_median(lst, 0, lstSize)
    improved_quick_sort_recursion(lst, 0, lstSize, median)
    return lst
