import sys
import heapq

# Input
input = sys.stdin.readline
n = int(input())
university = []

for _ in range(n):
    pay, day = map(int, input().split())
    university.append((pay, day))

# Sort by day
university.sort(key=lambda x: x[1])

queue = []

for pay, day in university:
    heapq.heappush(queue, pay)

    if day < len(queue):
        heapq.heappop(queue)

print(sum(queue))