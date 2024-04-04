def find_pair_with_sum(arr, target_sum):
    seen = set()
    for num in arr:
        target_pair = target_sum - num
        if target_pair in seen:
            return target_pair, num
        seen.add(num)
    return None

arr = [1, 4, 7, 2, 5, 9]
target_sum = 11
pair = find_pair_with_sum(arr, target_sum)
if pair:
    print(f"Pair with sum {target_sum}: {pair}")
else:
    print("No pair found with the given sum.")

def max_pair(arr):
    if len(arr) < 2:
        return None

    arr.sort()
    return arr[-1], arr[-2]

arr = [1, 7, 4, 2, 8, 6, 3, 9, 5,-10,-91]
pair = max_pair(arr)
if pair:
    product = pair[0] * pair[1]
    print(f"Pair with maximum product: {pair}, Product: {product}")
else:
    print("Array is too small to find a pair with maximum product.")

def segregate_zeros_and_ones(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        while arr[left] == 0 and left < right:
            left += 1
        while arr[right] == 1 and left < right:
            right -= 1
            
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
segregate_zeros_and_ones(arr)
print("Segregated Array:", arr)

def inversion_count(arr):
    count = 0
    inversions = []

    n = len(arr)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
                inversions.append((arr[i], arr[j]))

    return count, inversions

arr = [10, 1, 2, 4, 13, 9, 5]
count, inversions = inversion_count(arr)
print("Count:", count)
print("Inversions:", inversions)