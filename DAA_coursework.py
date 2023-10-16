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

import time
import matplotlib.pyplot as plt

def Selection_Sort(NumsList):
    n = len(NumsList)

    for i in range(n-1):
        minValueIndex = i

        for j in range(i+1, n):
            if NumsList[j] < NumsList[minValueIndex]:
                minValueIndex = j

        NumsList[i], NumsList[minValueIndex] = NumsList[minValueIndex], NumsList[i]

# Initialize lists of various lengths
list_lengths = list(range(1, 21))  # Lengths from 1 to 20
execution_times = []

for length in list_lengths:
    arr = list(range(length, 0, -1))  # Create a reversed list of given length
    start_time = time.time()
    Selection_Sort(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)

# Plot the results
plt.plot(list_lengths, execution_times, marker='o')
plt.xlabel('Length of List')
plt.ylabel('Execution Time (s)')
plt.title('Selection Sort Performance')
plt.grid(True)
plt.show()