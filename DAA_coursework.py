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

##########################################################################################################################

"""
INSERTION SORT

The time complexity of the insertion sort algorithm is O(n^2) in the worst case, where "n" is the number of elements in the list.
 This means that the time it takes to sort a list of "n" elements is roughly proportional to n^2.
For a list of 20 elements, the insertion sort would require approximately 20^2 = 400 time units in terms of computational steps.
 However, as with selection sort, the actual time it takes can vary depending on factors like the computer's processing speed, 
 the specific implementation, and the data distribution.
Here's a simplified example of how we can create a graph in Python to show the relationship between the length of the list and 
the time it takes for insertion sort.
In this code, we generate lists of various lengths, sort them using insertion sort, and measure the execution time.
 We then create a plot with list length on the x-axis and execution time on the y-axis. The resulting graph will show
   how the execution time increases as the length of the list grows.

"""

import time
import matplotlib.pyplot as plt

def Insertion_Sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Initialize lists of various lengths
list_lengths = list(range(1, 21))  # Lengths from 1 to 20
execution_times = []

for length in list_lengths:
    arr = list(range(length, 0, -1))  # Create a reversed list of given length
    start_time = time.time()
    Insertion_Sort(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)

# Plot the results
plt.plot(list_lengths, execution_times, marker='o')
plt.xlabel('Length of List')
plt.ylabel('Execution Time (s)')
plt.title('Insertion Sort Performance')
plt.grid(True)
plt.show()


#########################################################################################################################

"""
MERGE SORT

The time complexity of the merge sort algorithm is O(n log n) in the worst case, where "n" is the number of elements in the list. 
This means that the time it takes to sort a list of "n" elements is roughly proportional to n times the logarithm of n. Merge sort
 is more efficient than insertion and selection sort, especially for larger lists, and it offers a consistent and predictable time complexity.
For a list of 20 elements, the time complexity would be approximately 20 * log2(20), which is around 86.46 time units in terms of computational steps.
 Keep in mind that this is a simplification, as the actual time it takes can vary based on factors like the computer's processing speed, the specific
   implementation, and the data distribution.
To create a graph that shows the relationship between the length of the list and the time it takes for merge sort, we can use the following Python code.
In this code, we generate lists of various lengths, sort them using merge sort, and measure the execution time. We then create a plot with list length
 on the x-axis and execution time on the y-axis. The resulting graph will show how the execution time increases as the length of the list grows, 
 illustrating the efficiency of the merge sort algorithm for larger lists.

"""

import time
import matplotlib.pyplot as plt

def Merge_Sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        Merge_Sort(left_half)
        Merge_Sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Initialize lists of various lengths
list_lengths = list(range(1, 21))  # Lengths from 1 to 20
execution_times = []

for length in list_lengths:
    arr = list(range(length, 0, -1))  # Create a reversed list of a given length
    start_time = time.time()
    Merge_Sort(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)

# Plot the results
plt.plot(list_lengths, execution_times, marker='o')
plt.xlabel('Length of List')
plt.ylabel('Execution Time (s)')
plt.title('Merge Sort Performance')
plt.grid(True)
plt.show()




######################################################################################################################

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = {start}
        queue = deque([(start, 0)])  # (node, distance)
        while queue:
            node, distance = queue.popleft()
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
        return visited

    def mutual_friends(self, user1, user2):
        friends_of_user1 = self.bfs(user1)
        mutual_friends = [friend for friend in self.bfs(user2) if friend in friends_of_user1]
        return mutual_friends

# Example usage
social_graph = Graph()
social_graph.add_edge('Alice', 'Bob')
social_graph.add_edge('Bob', 'Charlie')
social_graph.add_edge('Alice', 'Charlie')
social_graph.add_edge('Charlie', 'David')
social_graph.add_edge('Eve', 'David')

user1 = 'Alice'
user2 = 'Charlie'

mutual_friends = social_graph.mutual_friends(user1, user2)
print(f"Mutual friends between {user1} and {user2}: {mutual_friends}")
