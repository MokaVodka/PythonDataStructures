# Sort wrapper
# Done because I'm tired of Flake8 screams

import os
import sys

# Path works when 1DV505/respo is the opened folder in VSCode
sys.path.append(os.path.abspath('./Assignment2/Lecture6/src/'))

# Shaddup Flake8 >:(
import Heap as hp

# Wil run experiment during import
# When testing, comment out the experiment in heap_sort_experiments
from heap_sort_experiments import heap_sort
from util_fast_sort import fast_merge_sort
from util_sort import get_random_list


# Can't use Heap as name because that's the same as Heap file name
def create_Heap():
    return hp.Heap()


def run_heap_sort(lst):
    return heap_sort(lst)


def run_fast_merge_sort(lst):
    return fast_merge_sort(lst)


def gen_random_list(size):
    get_random_list(size)
