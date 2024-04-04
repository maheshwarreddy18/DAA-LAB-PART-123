import time
import random
import matplotlib.pyplot as plt

def selection(arr):
    size = len(arr)
    for i in range(size):
        min_idx = i
        for j in range(i+1, size):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bubble(arr):
    size = len(arr)
    for i in range(size):
        for j in range(0, size-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

random_numbers = [random.randint(1, 10000) for _ in range(1000)]
start_time = time.time()
selection(random_numbers.copy())
selection_sort_time = time.time() - start_time

start_time = time.time()
insertion(random_numbers.copy())
insertion_sort_time = time.time() - start_time

start_time = time.time()
bubble(random_numbers.copy())
bubble_sort_time = time.time() - start_time

labels = ['Selection Sort', 'Insertion Sort', 'Bubble Sort']
times = [selection_sort_time, insertion_sort_time, bubble_sort_time]

plt.bar(labels, times, color=['blue', 'green', 'orange'])
plt.xlabel('Sorting Algorithm')
plt.ylabel('Time (seconds)')
plt.title('Execution Time for Sorting Algorithms')
plt.show()

def merge_sorted_sets(sorted_sets):
    merged_set = set()
    for s in sorted_sets:
        merged_set.update(s)
    sorted_result = sorted(merged_set)

    return sorted_result

sorted_sets = [
    {3, 5, 7},
    {2, 4, 6},
    {1, 8, 9}
]

sorted_result = merge_sorted_sets(sorted_sets)
print("Sorted Result:", sorted_result)

def find_k_largest(arr, k):
    arr.sort(reverse=True)
    return arr[:k]

arr = [3, 10, 4, 7, 9, 1]
k = 4  
largest_elements = find_k_largest(arr, k)
print(f"The {k} largest elements in the array are: {largest_elements}")

def max_activities(acts):
    if not acts:
        return 0

    sorted_acts = sorted(acts, key=lambda x: x[1])
    max_count = 1
    end_time = sorted_acts[0][1]
    max_activities_set = {sorted_acts[0]}

    for act in sorted_acts[1:]:
        if act[0] >= end_time:
            max_count += 1
            end_time = act[1]
            max_activities_set.add(act)

    return max_count, max_activities_set

# Example usage:
acts = [(1, 3), (2, 5), (3, 6), (5, 7), (8, 10)]
result, max_activities_set = max_activities(acts)
print("Max activities:", result)
print("Activities set:", max_activities_set)

def merge(intervals):
    if not intervals:
        return []

    sorted_set = sorted(intervals, key=lambda x: x[0])
    merged_set = [sorted_set[0]]

    for interval in sorted_set[1:]:
        if interval[0] <= merged_set[-1][1]:
            merged_set[-1] = (merged_set[-1][0], max(merged_set[-1][1], interval[1]))
        else:
            merged_set.append(interval)

    return merged_set

input_intervals = [(1, 4), (2, 5), (7, 8), (6, 9)]
result = merge(input_intervals)
print("Merged intervals:", result)