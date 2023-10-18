# DAA-Test1-S23B23091-B24780
WAVAMUNNO DANIEL L
S23B23/091
B24780

Question 1

2
(i) Describe the working principle of the insertion sort algorithm.

An insertion sort compares values in turn, starting with the second value in the list. If this value is greater than the value to the left of it, no changes are made. This value is repeatedly moved left until it meets a value that is less than it. The sort process then starts again with the next value. This continues until the end of the list is reached.

(ii) Discuss the best-case, average-case, and worst-case time complexities of insertion sort. Under what conditions does the best-case scenario occur?

The worst case and average case complexity of the insertion sort algorithm is O(n2). Meaning that, in the worst case, the time taken to sort a list is proportional to the square of the number of elements in the list.
The best-case time complexity of insertion sort algorithm is O(n) time complexity. This is the case when the list is already in the correct order. Meaning that the time taken to sort a list is proportional to the number of elements in the list. 

3
(i)	Create a list of unsorted integers.

The list is; lst = [99,1, 12, 25, 71, 100]

(iii) Verify and explain if the list was sorted correctly.
The list was sorted correctly because the output given is [1, 12, 25, 71, 99, 100]

4
How does insertion sort compare to other sorting algorithms, like bubble sort or merge sort, in terms of efficiency and use cases?

For bubble sort algorithm we check the neighbor element and swap them if required while for the insertion sort we transfer an element at one time to construct a sorted array while merge sort compares element of two halves to merge them into a final sorted array.


5
Imagine you have a nearly sorted list with just a few elements out of order. Wouldinsertion sort be a good choice for such a list? Justify your answer.

Insertion sort is for small lists especially if the list is nearly sorted, there won't be many elements that need to be moved to their correct positions. 
Therefore, sorting algorithms like quicksort or merge sort may not be justified.





Question 2
Define the following terms and explain their relationship to searching and sorting:
• Linear search
Linear search is a sequential searching algorithm where we start from one end and check every element of the list until the desired element is found.


• Binary search
Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half.

• Merge sort
Merge sort is a sorting algorithm that works by dividing an array into smaller subarrays and then merging the sorted subarrays back together to form the final sorted array.

• Quick sort
Quick sort is a sorting algorithm based on the divide and conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

Finding the maximum element in an Array
a) Algorithm:
a) Initialize a variable max to the first element of the array.
b) Iterate over the array, starting from the second element.
c) For each element in the array, compare it to the current value of max. If the element
is greater than max, update max to the value of the element.
d) After iterating over the entire array, return the value of max.
1. Write the a pseudocode and the actual code for the find_max() function in your preferred
programming language.


   
2. Test the find_max() function with a variety of different arrays, including empty arrays, arrays
with a single element, and arrays with multiple elements.
3. Analyze the time complexity and space complexity of the find_max() function.

ANSWER
The time Complexity is O(n) which is linear time complexity and the space complexity is O(1) which is constant space complexity.
