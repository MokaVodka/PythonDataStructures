# Sort wrapper
# Done because I'm tired of Flake8 screams

import os
import sys

# Path works when respo is the opened folder in VSCode
sys.path.append(os.path.abspath('./Assignment1/Lecture3/'))
sys.path.append(os.path.abspath('./Assignment2/Lecture5/src/'))

import sort_algorithms as sa
from util import gen_random_list
import Deque as deq


def get_random_list(size):
    return gen_random_list(size)


def sort_algorithms():
    return [sa.selection_sort, sa.bubble_sort, sa.insertion_sort,
            sa.merge_sort, sa.quick_sort, sa.improved_quick_sort]


# Can't use Deque as name because that's the same as Deque file name
def create_Deque():
    return deq.Deque()
