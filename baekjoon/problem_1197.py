import sys

input = sys.stdin.readline
v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]

def kruskal(edges):
    def make_set():
        parent = [0] * (v+1)
        for i in range(1, v+1):
            parent[i] = i
        return parent

    def collapsing_find(parent, x):
        if parent[x] != x:
            parent[x] = collapsing_find(parent, parent[x])
        return parent[x]

    def weighted_union(parent, i, j):
        i_root = collapsing_find(parent, i)
        j_root = collapsing_find(parent, j)
        if i_root < j_root:
            parent[j_root] = i_root
        else:
            parent[i_root] = j_root
    
    total_cost = 0
    parent = make_set()
    edges.sort(key=lambda x: x[2])

    for i in range(e):
        a, b, cost = edges[i]
        if collapsing_find(parent, a) != collapsing_find(parent, b):
            weighted_union(parent, a, b)
            total_cost += cost    

    return total_cost

print(kruskal(edges))

def prim(edges):
    pass

print(prim(edges))