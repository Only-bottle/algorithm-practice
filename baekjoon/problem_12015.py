import sys

# Input
input = sys.stdin.readline
size = input().split()
init_sequence = list(map(int, input().split()))

# Binary Search
def binary_search(arr, value):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid
    return left

result = []
result.append(init_sequence.pop(0))

for value in init_sequence:
    if result[-1] < value:
        result.append(value)
    else:
        key = binary_search(result, value)
        result[key] = value
print(len(result))