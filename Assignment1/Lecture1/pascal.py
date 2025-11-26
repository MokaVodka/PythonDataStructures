def pascal_rec(lst, n):

    # Build line based on previous line, starting from line 0: [1]
    t_lst = []
    listLength = len(lst)
    for i in range(-1, listLength):
        if i == -1 or i == listLength - 1:
            t_lst.append(1)
        else:
            t_lst.append(lst[i] + lst[i + 1])

    # Stop recursion when current line length is larger than n + 1
    if len(t_lst) > n + 1:
        return lst
    else:
        return pascal_rec(t_lst, n)


def pascal_line(n):

    # Base case
    if n == 0:
        return [1]

    # Recursive case
    else:
        return pascal_rec([1], n)


# -- Main Program --
def pascal_triangle():

    # Change input here
    lineIndex = 6

    pascalLine = pascal_line(lineIndex)
    print(f'Line {lineIndex} on the Pascal Triangle is {pascalLine}')


pascal_triangle()
