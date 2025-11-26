import os


def is_python(name):
    return name.endswith('.py')


def count_line(filePath):
    count = 0

    with open(filePath, 'r') as file:
        for line in file:
            t_line = line.replace('\n', '')
            if len(t_line) > 0:
                count += 1

    return count


def count_lines(path, depth):
    lineCount = 0

    with os.scandir(path) as dirIter:
        for dirEntry in dirIter:

            # Count python file lines
            if dirEntry.is_file() and is_python(dirEntry.name):
                lineCount += count_line(dirEntry.path)

            # Print sub-directories with indent
            if dirEntry.is_dir():
                indent = '  ' * depth
                print(f'{indent}Dir: {dirEntry.name}')
                lineCount += count_lines(dirEntry.path, depth + 1)

    return lineCount


# -- Main Program --
def print_directory_contents():

    # Change input here
    dirPath = '.'
    isValidDir = os.path.exists(dirPath) and os.path.isdir(dirPath)
    if not isValidDir:
        print(f'Path "{dirPath}" is invalid')
        return

    # Base directory
    currDir = os.path.basename(os.getcwd() if dirPath == '.' else dirPath)
    print(f'Dir: {currDir}')

    # Print content and recursion case
    lineCount = count_lines(dirPath, 1)
    print(f'Total non-empty lines in all found .py files: {lineCount}')


print_directory_contents()
