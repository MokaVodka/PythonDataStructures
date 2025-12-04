# Sort wrapper
# Done because I'm tired of Flake8 screams

import os
import sys

# Path works when respo is the opened folder in VSCode
sys.path.append(os.path.abspath('./Assignment1/Lecture3/'))
sys.path.append(os.path.abspath('./Assignment2/Lecture5/src/'))
sys.path.append(os.path.abspath('./Util/'))

import sort_algorithms as sa
from list_gen import get_random_list
import Deque as deq


def gen_random_list(size):
    return get_random_list(size)


def sort_algorithms():
    return [sa.selection_sort, sa.bubble_sort, sa.insertion_sort,
            sa.merge_sort, sa.quick_sort, sa.improved_quick_sort]

# Can't use Deque as name because that's the same as Deque class
def create_Deque():
    return deq.Deque()
