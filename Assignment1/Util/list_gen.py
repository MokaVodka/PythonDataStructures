import random


# -- Get list of randomize int --
def get_random_list(size, width=10):
    result = []
    intRange = width * size
    for _ in range(0, size):
        result.append(random.randint(-intRange, intRange))
    return result
