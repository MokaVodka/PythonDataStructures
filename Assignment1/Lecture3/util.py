# Util wrapper
# Done because I'm tired of Flake8 screams

import os
import sys

# Path works when Assignment1 is the opened folder in VSCode
# and Run -> Debug current script
sys.path.append(os.path.abspath('./Util/'))

# Shaddup Flake8 >:(
# You didn't accept my __init__.py !!!
from linear_regress import get_polinomial_ordo
from list_gen import get_random_list


def estimate_ordo(sizes, times):
    coefficient, bestFitLine = get_polinomial_ordo(sizes, times)
    return coefficient, bestFitLine


def gen_random_list(size):
    lst = get_random_list(size)
    return lst


# Use only valid data for plotting
def filter_plot_data(sizes, times):
    iterater = range(0, len(sizes))
    size, time = [], []

    for i in iterater:
        if times[i] > 0:
            size.append(sizes[i])
            time.append(times[i])

    return size, time
