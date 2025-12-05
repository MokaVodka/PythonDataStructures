# Python Data Structures

This is a respository for programming assignments
done in **Linneaus University**'s *Programming and Data Structures* course


# Notes

## Slow/Delayed test runs (VSCode, not sure on command line)

When running Assignment 2 tests on VSCode, there might be a delay.

This is due to Lecture 6's *util_test_heap.py* importing **heap_sort** from *heap_sort_experiments.py*,
which runs **experiments()** (sorting lists and comparing algorithm performance).

To not be disturbed by **experiments()**, comment it out.
