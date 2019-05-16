# Improvised Quick Sort

Implementation of MY_CHOICE_QSORT algorithm which is an improvisation of the traditional quicksort on the given two types of data sets. </br>
a. Set_1: Random Lists (1000, 10K, 50K, 100K and 500K) </br>
b. Set_2: Poisson distribution of data values </br>
</br>

Median of three technique:</br>
Median of three technique is an enhancement to the quicksort algorithm. In this method, before partitioning process of the data value begins, the left, middle and right element of the data values are sorted, and these values are placed back in sorted order in the same positions in the data. The pivot value is the median of these three elements. The rest of the process continues same as the traditional quicksort algorithm

Output:
Set 1 observations: </br>
ALGORITHM   N COMPARISONS  TIME </br>
Quick sort   1000 248502   0.06245112419128418 </br>
MY_CHOICE_QSORT  1000 62002   0.015660762786865234 </br>
Quick sort   10000 124749   0.03120279312133789 </br>
MY_CHOICE_QSORT  10000 124251   0.046866416931152344 </br>
Quick sort   50000 124749   0.03128933906555176 </br>
MY_CHOICE_QSORT  50000 124251   0.046814918518066406 </br>
Quick sort   100000 124749   0.031244277954101562 </br>
MY_CHOICE_QSORT  100000 124251   0.03124260902404785 </br>
Quick sort   500000 124749   0.04686307907104492 </br>
MY_CHOICE_QSORT  500000 124251   0.03124403953552246 
 
Set 2 observations: ALGORITHM   N COMPARISONS  TIME Quick sort   1000 124749   0.046863555908203125 MY_CHOICE_QSORT  1000 124251   0.03129076957702637 Quick sort   10000 124749   0.046816349029541016 MY_CHOICE_QSORT  10000 124251   0.03127264976501465 Quick sort   50000 124749   0.046880483627319336 MY_CHOICE_QSORT  50000 124251   0.03123021125793457 Quick sort   100000 124749   0.04686617851257324 MY_CHOICE_QSORT  100000 124251   0.031204700469970703 Quick sort   500000 124749   0.06248593330383301 MY_CHOICE_QSORT  500000 124251   0.04945945739746094 
Traditional quicksort with pivot value chosen as the last element of the data set turns out efficient when the data values are random, but it gives a bad runtime when the data set is nearly sorted or nearly reverse sorted. In this case, MY_CHOICE_QSORT algorithm(using median-of-three technique) gives equal or more efficient results in terms of runtime as well as comparisons thus enhancing quick sort.

