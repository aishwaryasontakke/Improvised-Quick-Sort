__author__ = 'AISHWARYA SONTAKKE'

"""
Author: AISHWARYA SONTAKKE as4897
This program has two types of quick sorting algorithms implemented.
"""

def qsort(toSortlist):
    """
        Sort list using quick sort algorithm
    :param toSortlist: list to be sorted
    :return: currentList: list formed by tracing back up at the end of current recursion call
    :return: no_comparisons: number of comparisons calculated by end of this call
    """
    no_comparisons = 0

    # Initialize list for storing sorted list by end of this recursive call
    currentList = list(range(len(toSortlist)))

    if len(toSortlist) != 0:
        # Taking last element as pivot
        pivot = toSortlist[len(toSortlist) - 1]

    """
     Dividing the list around the pivot as left list < pivot and right list > pivot
    """

    if len(toSortlist) == 1:
        # For one element we add one element in list before it is returned
        # And no more division needed
        currentList[0] = pivot

    elif len(toSortlist) > 1:
        # Partition list into left_list and right_list
        left_list, right_list, comparisons = partitionList(toSortlist, pivot)

        # Add comparisons used to partition list
        no_comparisons += comparisons

        """
            Divide and call recursively for left and right lists
        """

        # Recursive call to left
        left_sorted_list, comparisons = qsort(left_list)

        no_comparisons += comparisons

        # Recursive call to right
        right_sorted_list, comparisons = qsort(right_list)

        no_comparisons += comparisons

        """
         Form list using left sorted list, pivot and right sorted list in order
        """
        curr_index = 0

        # Add left list
        while curr_index < len(left_sorted_list):
            currentList[curr_index] = left_sorted_list[curr_index]
            curr_index += 1

        # Add pivot
        currentList[curr_index] = pivot
        curr_index += 1

        # Add right list
        right_index = 0

        while curr_index < len(currentList):
            currentList[curr_index] = right_sorted_list[right_index]
            curr_index += 1
            right_index += 1

    # For length of list toSortList  = 0 there is no element to add to sorted list
    # Hence empty list returned

    return currentList, no_comparisons

def partitionList(toPartitionlist, pivot):
    """
        Partition list into left as smaller than pivot and right as greater than pivot
    :param toPartitionlist: list to partition
    :param pivot: pivot to compare elements to
    :return: left_list: left list i.e. all elements <= pivot
    :return: right_list: right list i.e. all elements > pivot
    :return: comparisons: number of comparisons to partition
    """
    """
     Start i from beginning and j from one before pivot (since pivot is last element)
     i moves right till a value greater than pivot is found and j moves left till a
     value < pivot found. If both these conditions satisfied then swap and continue till i >= j
    """
    comparisons = 0
    i = 0
    j = len(toPartitionlist) - 2

    while j > i:
        comparisons += 1
        if toPartitionlist[i] > pivot:
            # If left marker finds a value greater than pivot then we check right marker
            comparisons += 1
            if toPartitionlist[j] > pivot:
                # right marker found value at correct position so move to next
                j -= 1
            else:
                # Since both found values in wrong position, we swap
                toPartitionlist[i], toPartitionlist[j] = toPartitionlist[j], toPartitionlist[i]
                j -= 1
                i += 1
        else:
            # left marker found value at correct position so move to next
            i += 1

    # If left marker = right marker and value at that position is <= pivot
    # then we need to divide differently
    if i == j and toPartitionlist[i] <= pivot:
        left_list = toPartitionlist[0:i + 1]
        right_list = toPartitionlist[i + 1:-1]
    else:
        # Here left marker > right marker or left marker = right marker but value at that pos is > pivot
        # so we have left list till left marker - 1
        # and right list is left marker to second last element
        left_list = toPartitionlist[0:i]

        # -1 is last element so we get list till second last element
        right_list = toPartitionlist[i:-1]

    return left_list, right_list, comparisons

def get_median_pivot(a,b,c):
    """
        Find the median of the 3 parameters passed.
    :param a: First element of the list
    :param b: Middle element of the list
    :param c: Last element of the list
    :return: median of a, b and c
    """
    if ( a - b) * (c - a) >= 0:
        return a
    elif (b - a) * (c - b) >= 0:
        return b
    else:
        return c

def MY_CHOICE_QSORT(toSortlist):
    """
        Sorting the list using enhanced quick sort algorithm.
    :param toSortlist: list to be sorted
    :return: currentList: Sorted list by the end of the call to this method
    :return: no_comparisons: number of comparisons calculated by end of the call to this method
    """

    a = toSortlist[0]
    c = toSortlist[len(toSortlist) - 1]
    if len(toSortlist)%2==0:
        b = toSortlist[len(toSortlist)//2 -1]
    else:
        b= toSortlist[len(toSortlist)//2]

    pivot = get_median_pivot(a, b, c)

    vals=[a,b,c]
    vals.sort

    toSortlist[0]=vals[0]
    toSortlist[len(toSortlist) - 1]=vals[2]
    if len(toSortlist)%2==0:
        toSortlist[len(toSortlist)//2 -1]= vals[1]
    else:
        toSortlist[len(toSortlist)//2] = vals[1]

    no_comparisons = 0

    # Initialize list for storing sorted list by end of this recursive call
    currentList = list(range(len(toSortlist)))

    """
             Now we divide around the pivot as left list are < pivot and right > pivot
            """

    if len(toSortlist) == 1:
        # For one element we add one element in list before it is returned
        # And no more division needed
        currentList[0] = pivot

    elif len(toSortlist) > 1:
        # Partition list into left_list and right_list
        left_list, right_list, comparisons = partitionList(toSortlist, pivot)

        # Add comparisons used to partition list
        no_comparisons += comparisons

        """
            Divide and call recursively for left and right list
        """

        # Recursive call to left
        left_sorted_list, comparisons = qsort(left_list)

        no_comparisons += comparisons

        # Recursive call to right
        right_sorted_list, comparisons = qsort(right_list)

        no_comparisons += comparisons

        """
         Form list using left sorted list, pivot and right sorted list in order
        """
        curr_index = 0

        # Add left list
        while curr_index < len(left_sorted_list):
            currentList[curr_index] = left_sorted_list[curr_index]
            curr_index += 1

        # Add pivot
        currentList[curr_index] = pivot
        curr_index += 1

        # Add right list
        right_index = 0

        while curr_index < len(currentList):
            currentList[curr_index] = right_sorted_list[right_index]
            curr_index += 1
            right_index += 1

    # For length of list toSortList  = 0 there is no element to add to sorted list
    # Hence empty list returned

    return currentList, no_comparisons