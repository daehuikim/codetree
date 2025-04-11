import copy
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
max_value = max(max(row) for row in grid)
min_value = min(min(row) for row in grid)
# Please write your code here.
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def can_go(x, y, k, visited):
    if 0 <= x < m and 0 <= y < n and grid[y][x] > k and not visited[y][x]:
        return True
    return False


def dfs(x, y, depth, visited):
    visited[y][x] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if can_go(nx, ny, depth, visited):
            dfs(nx, ny, depth, visited)

max_area = 0
best_turn = 1
for t in range(max(1,min_value-1), max_value):
    visited = [[False for _ in range(m)] for _ in range(n)]
    areas = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] > t:
                dfs(j,i,t,visited)
                areas += 1
    if areas > max_area:
        max_area = areas
        best_turn = t

print(best_turn, max_area)

