import sys

# Input
input = sys.stdin.readline
n = int(input())
k = int(input())

def binary_search(target):
    left, right = 1, k

    while left <= right:
        cnt = 0
        mid = (left + right) // 2

        for i in range(1, n+1):
            cnt += min(n, mid // i)

        if cnt >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left

print(binary_search(k))