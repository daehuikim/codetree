import copy

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
max_value = max(max(row) for row in grid)
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
turn = 0
peak=False
for t in range(1, max_value):
    visited = [[False for _ in range(m)] for _ in range(n)]
    areas = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] > t:
                dfs(j,i,t,visited)
                areas += 1
    if max_area < areas:
        max_area = areas
    else:
        peak = True
        turn=t-1
        break

if peak:
    print(turn, max_area)
else:
    print(t, max_area)

