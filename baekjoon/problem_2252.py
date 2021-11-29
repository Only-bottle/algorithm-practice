import sys
import heapq
sys.setrecursionlimit(10**6)


def topological_sort(graph, indegree, heap):
    result = []
    while heap:
        node = heapq.heappop(heap)
        result.append(node)
        for adj_node in graph[node]:
            indegree[adj_node] -= 1
            if indegree[adj_node] == 0:
                heapq.heappush(heap, adj_node)
    return result

# Input
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
heap = []

# Graph Initialize
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# Queue Initialize
for idx in range(1, N+1):
    if indegree[idx] == 0:
        heapq.heappush(heap, idx)

# Topological Sort
sorted_result = topological_sort(graph, indegree, heap)

# Result
print(*sorted_result)
