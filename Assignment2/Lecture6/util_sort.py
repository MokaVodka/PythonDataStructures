# Sort wrapper
# Done because I'm tired of Flake8 screams

from util_fast_sort import fast_merge_sort

import os
import sys

# Path works when respo is the opened folder in VSCode
sys.path.append(os.path.abspath('./Assignment1/Lecture3/'))
sys.path.append(os.path.abspath('./Util/'))

import sort_algorithms as sa
from list_gen import get_random_list
from util import filter_plot_data


def gen_random_list(size):
    return get_random_list(size)


def sort_algorithms(fastMergeSort=False):
    if fastMergeSort:
        return [fast_merge_sort, sa.quick_sort]
    return [sa.merge_sort, sa.quick_sort]


def sort_run(sortAlgo, sizeRange, repeat=1, printAvgTime=False):
    return sa.sort_run(sortAlgo, sizeRange, repeat, printAvgTime)


def filter_data(sizes, times):
    return filter_plot_data(sizes, times)
