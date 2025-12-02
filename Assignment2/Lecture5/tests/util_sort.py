# Sort wrapper
# Done because I'm tired of Flake8 screams

import os
import sys

# Path works when respo is the opened folder in VSCode
sys.path.append(os.path.abspath('./Assignment1/Lecture3/'))

import sort_algorithms as sa
import util


def gen_random_list(size):
    return util.gen_random_list(size)


def sort_algorithms():
    return [sa.selection_sort, sa.bubble_sort, sa.insertion_sort,
            sa.merge_sort, sa.quick_sort, sa.improved_quick_sort]
