import HashMap as hm
import os


def program():
    hashMap = hm.HashMap(init_capacity=1000)
    lines = []

    # Reading file
    print('Reading file...  ', end='')

    # This should work if opened directory is Assignment3
    filePath = os.path.normcase(os.getcwd() + '/lecture8/')
    fileName = '1900380_words.txt'
    with open(f'{filePath}{fileName}', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]

    # Sort words for pointer-based counting
    lines.sort()
    totalWords = len(lines)
    pointer = 0

    while pointer < totalWords:

        # Get word count
        word = lines[pointer]
        count = 1

        while pointer + count < totalWords:
            if word != lines[pointer + count]:
                break
            else:
                count += 1

        # Update hashMap
        hashMap.put(word, count)
        pointer += count

    print('Done!')
    print()

    # Sort words by counts
    toSort = [(element[1], element[0]) for element in hashMap.as_list()]
    toSort.sort()
    wordList = toSort[-10:][::-1]
    toSort = None  # Free memory

    # Print to console
    print(f'File: {filePath}{fileName}')
    print(f'Word count: {totalWords}')
    print(f'Unique words: {hashMap.get_size()}')
    print()

    print('Top 10 Words')
    for i in range(0, 10):
        print(f'{wordList[i][1]:10} {wordList[i][0]}')
    print()

    print(f'Hash map capacity: {hashMap.get_capacity()}')


program()
