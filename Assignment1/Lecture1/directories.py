import os


def is_hidden(name):
    return name.startswith('.') or name.startswith('_')


def print_files(dir_path):

    with os.scandir(dir_path) as dirIter:
        for dirEntry in dirIter:

            # Print non-hidden files in passed directory
            if dirEntry.is_file() and not is_hidden(dirEntry.name):
                print(f'File: {dirEntry.name}')

            # Print all sub-directories
            if dirEntry.is_dir():
                print(f'Dir: {dirEntry.name}')
                print_files(dirEntry.path)


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
    print_files(dirPath)


print_directory_contents()
