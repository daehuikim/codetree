n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from collections import defaultdict

graph = defaultdict(list)
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

visited = [False for _ in range(n+1)]

def dfs(current):
    for neighbor in graph[current]:
        if not visited[neighbor]:
            visited[neighbor]=True
            dfs(neighbor)

dfs(1)
count=-1
for item in visited:
    if item==True:
        count+=1
print(count)