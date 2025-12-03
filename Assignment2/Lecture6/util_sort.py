# Sort wrapper
# Done because I'm tired of Flake8 screams

import os
import sys

# Path works when 1DV505/respo is the opened folder in VSCode
sys.path.append(os.path.abspath('./Assignment1/Lecture3/'))
sys.path.append(os.path.abspath('./Util/'))

# Shaddup Flake8 >:(
import sort_algorithms as sa
from list_gen import get_random_list
from util import filter_plot_data


def gen_random_list(size):
    return get_random_list(size)


def sort_algorithms():
    return [sa.merge_sort, sa.quick_sort]


def sort_run(sortAlgo, sizeRange, repeat=1, printAvgTime=False):
    return sa.sort_run(sortAlgo, sizeRange, repeat, printAvgTime)


def filter_data(sizes, times):
    return filter_plot_data(sizes, times)
