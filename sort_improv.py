__author__ = 'AISHWARYA SONTAKKE'

"""
Author: AISHWARYA SONTAKKE

This program compares two different quick sorting algorithms on the
given two types of data sets.
"""

import quick_sort_types
import random
import time
import numpy as np

def check_sorted(list):
    """
        Check if list is sorted
    :param list: list to check
    :return: true if sorted else false
    """
    # Runs through list from 0 to length - 2
    for list_index in range(len(list) - 1):
        # If current element is greater than next one, then the list is not sorted.
        if list[list_index] > list[list_index + 1]:
            return False
    # Reached only if complete loop executed without condition match
    return True

def generate_data(N):
    """
        Generate a random sequence of N integers.
    :param N : a non-negative integer
    :return: result : list of integers generated
    """
    # Initialize a list of N elements
    result = list(range(N))

    # Random shuffle of values in result
    random.shuffle(result)

    return result

def displayIfSorted(sorted_list):
    """
        Print true for sorted and false for not
    :param sorted_list: list to be checked
    """
    print("Sorted : " + str(check_sorted(sorted_list)))

def main():
    """
        Main function
        Prints observation table
    """
    print("Set 1 observations:")
    values=[1000,10000, 50000, 100000, 500000]
    print("ALGORITHM\t\t\tN\t\tCOMPARISONS\t\tTIME")

    for N in values:

        toSortlist = generate_data(N)
        start = time.time()
        sorted_list, num_comparisons = quick_sort_types.qsort(toSortlist)
        end = time.time()
        time_taken = end - start
        print("Quick sort\t\t\t" + str(N) + "\t" + str(num_comparisons) + "\t\t\t" + str(time_taken))

        start = time.time()
        sorted_list, num_comparisons = quick_sort_types.MY_CHOICE_QSORT(toSortlist)
        end = time.time()
        time_taken = end - start
        print("MY_CHOICE_QSORT\t\t" + str(N) + "\t" + str(num_comparisons) + "\t\t\t" + str(time_taken))

    print("")
    print("Set 2 observations:")
    print("ALGORITHM\t\t\tN\t\tCOMPARISONS\t\tTIME")

    for N in values:
        toSortlist = np.random.poisson(N/2,N)
        start = time.time()
        sorted_list, num_comparisons = quick_sort_types.qsort(toSortlist)
        end = time.time()
        time_taken = end - start
        print("Quick sort\t\t\t" + str(N) + "\t" + str(num_comparisons) + "\t\t" + str(time_taken))

        start = time.time()
        sorted_list, num_comparisons = quick_sort_types.MY_CHOICE_QSORT(toSortlist)
        end = time.time()
        time_taken = end - start
        print("MY_CHOICE_QSORT\t\t" + str(N) + "\t" + str(num_comparisons) + "\t\t" + str(time_taken))

if __name__ == '__main__':
    main()
