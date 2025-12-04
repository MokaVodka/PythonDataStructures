# -- Fast merge sort --
# My merge sort in assignment 1-3 is slow
# Because it is in-place merge sort (has insertion sort)
# So this is a faster implementation (hopefully)
def fast_merge(lst, start, end):
    sort = []

    middle = (start + end) // 2
    leftP = start
    rightP = middle + 1

    leftE = lst[leftP]
    rightE = lst[rightP]

    # Sort elements
    while leftP <= middle and rightP <= end:
        # Value is in correct place,
        # Add to sort and check next element
        if leftE <= rightE:
            sort.append(leftE)
            leftP += 1
            if leftP <= middle:
                leftE = lst[leftP]

        # Add right element instead
        # Then check current left to next right element
        else:
            sort.append(rightE)
            rightP += 1
            if rightP <= end:
                rightE = lst[rightP]

    # Add remaining elements
    # They are garanted to be sorted, no worries
    while leftP <= middle:
        sort.append(lst[leftP])
        leftP += 1

    while rightP <= end:
        sort.append(lst[rightP])
        rightP += 1

    # Replace sorted in list place
    # Copy the sorted elements from temp back into lst
    for i in range(0, len(sort)):
        lst[start + i] = sort[i]


def merge_sort_recursion(lst, start, end):
    middle = (start + end) // 2

    if start < end:
        merge_sort_recursion(lst, start, middle)
        merge_sort_recursion(lst, middle + 1, end)
        fast_merge(lst, start, end)


def fast_merge_sort(lst):
    lst = lst.copy()
    lstSize = len(lst)
    merge_sort_recursion(lst, 0, lstSize - 1)
    return lst
