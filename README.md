# Improvised Quick Sort

Implementation of MY_CHOICE_QSORT algorithm which is an improvisation of the traditional quicksort on the given two types of data sets. </br>
a. Set_1: Random Lists (1000, 10K, 50K, 100K and 500K) </br>
b. Set_2: Poisson distribution of data values </br>

Median of three technique for MY_CHOICE_QSORT:</br>
- Before partitioning process of the data value begins, the left, middle and right element of the data values are sorted, and these values are placed back in sorted order in the same positions in the data. 
- The pivot value is median of these three elements.
- The rest of the process continues same as the traditional quicksort algorithm.</br>

Traditional quicksort with pivot value chosen as the last element of the data set turns out efficient when the data values </br> are random, but it gives a bad runtime when the data set is nearly sorted or nearly reverse sorted. In such cases, MY_CHOICE_QSORT algorithm gives equal or more efficient results in terms of runtime as well as comparisons thus enhancing quick sort.</br>

## Instructions:

Code includes 2 python files: sort_improv.py and quick_sort_types.py. </br>
Run sort_improv.py for execution of both quick sort types. There is no commandline argument required. </br>
The random data is generated within the file sort_improv.py for 1000, 10K, 50K, 100K and 500K data sizes. 
