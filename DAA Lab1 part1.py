import time
import random
import matplotlib.pyplot as plt

# Function to calculate the sum of first N natural numbers iteratively
def iter_sum(N):
    total = 0
    for num in range(1, N + 1):
        total += num
    return total

# Function to calculate the sum of first N natural numbers recursively
def recur_sum(N):
    if N == 0:
        return 0
    else:
        return N + recur_sum(N - 1)

# Function to measure the execution time of a function
def measure_time(func, N):
    start_time = time.time()
    func(N)
    end_time = time.time()
    return end_time - start_time

# Generate a range of N values from 1 to 1000
N_values = range(1, 1001)

# Calculate execution times for both recursive and iterative approaches
recursive_times = [measure_time(recur_sum, n) for n in N_values]
iterative_times = [measure_time(iter_sum, n) for n in N_values]

# Plot the execution times
plt.plot(N_values, recursive_times, label='Recursive')
plt.plot(N_values, iterative_times, label='Iterative')
plt.xlabel('N')
plt.ylabel('Time ')
plt.title('Execution Time for Sum of First N Natural Numbers')
plt.legend()
plt.grid(True)
plt.show()

# Function to perform linear search
def linear_search(arr, target):
    start = time.time()
    for i, num in enumerate(arr):
        if num == target:
            return (time.time() - start) * 10**6  # Convert to microseconds
    return -1

# Function to perform binary search
def binary_search(arr, target):
    start = time.time()
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return (time.time() - start) * 10**6  # Convert to microseconds
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Generate an array and a search key
arr = [random.randint(1, 1000) for _ in range(10000)]
key = random.choice(arr)

# Perform search operations and measure execution times
linear_times = []
binary_times = []

for _ in range(5):
    linear_times.append(linear_search(arr, key))
    arr.sort()  # Binary search requires a sorted array
    binary_times.append(binary_search(arr, key))

# Print search times
print("Linear search times (microseconds):", linear_times)
print("Binary search times (microseconds):", binary_times)

# Plot search times
plt.plot(range(1, 6), linear_times, label='Linear Search')
plt.plot(range(1, 6), binary_times, label='Binary Search')
plt.xlabel('Trial')
plt.ylabel('Time (microseconds)')
plt.title('Execution Time for Linear and Binary Search')
plt.legend()
plt.grid(True)
plt.show()

# Function to convert a string of digits to an integer
def str_to_int(string1): 
    string = string1.replace(',', '')
    if not string:
        return 0
    digit = int(string[-1])
    integer_value = str_to_int(string[:-1])
    return integer_value * 10 + digit

# Take input from the user and convert it to an integer
input_str = input("Enter a string of digits: ")
result = str_to_int(input_str)
print("Integer representation:", result)

# Function to reverse a string recursively
def reverse_str(string2):
    if len(string2) <= 1:
        return string2
    else:
        return reverse_str(string2[1:]) + string2[0]

# Reverse a given string
input_str = "pots&pans"
rev_str = reverse_str(input_str)
print("Reversed string:", rev_str)

# Function to check if a string is palindrome recursively
def palindrome(string3):
    if len(string3) <= 1:
        return True
    if string3[0] != string3[-1]:
        return False
    return palindrome(string3[1:-1])

# Take input from the user and check if it is a palindrome
input_str = input("Enter a string: ")
if palindrome(input_str):
    print("Input is a palindrome.")
else:
    print("Input is not a palindrome.")