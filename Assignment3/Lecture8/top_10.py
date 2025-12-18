import HashMap as hm
import os


def program():
    hashMap = hm.HashMap(init_capacity=1000)
    totalLines = 1900380

    # Reading file
    print('Reading file...  ', end='')

    # This should work if opened directory is Assignment3
    filePath = os.path.normcase(os.getcwd() + '/lecture8/')
    fileName = '1900380_words.txt'
    with open(f'{filePath}{fileName}', 'r', encoding='utf-8') as file:

        # Factor of totalLines (Used a calculator for this)
        increment = 20004
        lineCount = 0
        progress, currProgress = -1, 0

        while lineCount < totalLines:

            # Print progress
            # Since it's kinda boring to wait for the reading to be done
            currProgress = int(lineCount / totalLines * 100)
            if currProgress != progress:
                print(f'{currProgress}%  ', end='')
                progress = currProgress

            # Read multi-lines
            lines = []
            for _ in range(0, increment):
                lines.append(file.readline().strip())

            # Get word count and update hashMap
            # Also this is super slow, but I can't be bothered to deal with it
            for word in lines:
                count = hashMap.get(word)
                if count is None:
                    count = 0

                hashMap.put(word, count + 1)

            lineCount += increment

    print('Done!')
    print()

    # Sort words by counts
    toSort = [(element[1], element[0]) for element in hashMap.as_list()]
    toSort.sort()
    wordList = toSort[-10:][::-1]
    toSort = None  # Free memory

    # Print to console
    print(f'File: {filePath}{fileName}')
    print(f'Word count: {totalLines}')
    print(f'Unique words: {hashMap.get_size()}')
    print()

    print('Top 10 Words')
    for i in range(0, 10):
        print(f'{wordList[i][1]:10} {wordList[i][0]}')
    print()

    print(f'Hash map capacity: {hashMap.get_capacity()}')


program()
