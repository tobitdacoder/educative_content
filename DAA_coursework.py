""" 1. SELECTION SORT

The time complexity of the selection sort algorithm is O(n^2), where "n" is the number of elements in the list. This means that the time it 
takes to sort a list of "n" elements is roughly proportional to n^2. For a list of 20 elements, the selection sort would require approximately 
20^2 = 400 time units in terms of computational steps. However, the actual time it takes can vary depending on factors like the computer's processing 
speed, the specific implementation, and the data distribution (whether the list is partially sorted or not).
Creating a graph to show the relationship between the length of the list and the time it takes for selection sort is a bit more involved.
 We would need to run the selection sort algorithm on lists of various lengths, measure the execution time, and then plot the results. 
 Here's a simplified example of how we can create such a graph in Python using the time module.
In this code bellow , we generate lists of various lengths, sort them using selection sort, and measure the execution time. 
We then create a plot with list length on the x-axis and execution time on the y-axis. The resulting graph will show how the 
execution time increases as the length of the list grows."""

