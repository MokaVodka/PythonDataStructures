import nsum as ns

# If script doesn't run, check path in util.py
from util import gen_random_list


# -- Test for algorithm correctness --
# nsumAlgo: nsum algorithm to use
def nsum_correct_test(nsumAlgo):
    label = ''
    if nsumAlgo == ns.threesum_brute:
        label = 'threesum_brute'
    if nsumAlgo == ns.threesum_pointers:
        label = 'threesum_pointers'
    if nsumAlgo == ns.threesum_caching:
        label = 'threesum_caching'

    print(f'{label}() correctness test')
    for _ in range(0, 3):
        lst = gen_random_list(15)
        sum = nsumAlgo(lst)
        print(f'Input: {lst}')
        print(f'Output: {sum}')

    print('')


# -- Test runs --
# Commented out so they don't run during import
# nsum_correct_test(ns.threesum_brute)
# nsum_correct_test(ns.threesum_pointers)
# nsum_correct_test(ns.threesum_caching)
