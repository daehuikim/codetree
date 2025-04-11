from collections import deque
import sys

sys.setrecursionlimit(10 ** 5)

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

walls = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            walls.append((j,i))

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1
count = -1
# Please write your code here.
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def can_go(x, y,visited):
    if 0 <= x < n and 0 <= y < n and grid[y][x] == 0 and not visited[y][x]:
        return True
    return False


def bfs(visited):
    if r1 == r2 and c1 == c2:
        return 0
    q = deque()
    time = 0
    q.append((c1, r1, time))
    visited[r1][c1] = True
    while q:
        x, y, time = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if can_go(nx, ny,visited):
                visited[ny][nx] = True
                if nx == c2 and ny == r2:
                    return time + 1
                q.append((nx, ny, time + 1))
    return -1


def backtrack(current,index):
    global count

    if len(current) == k:
        visited = [[False for _ in range(n)] for _ in range(n)]
        for item in current:
            grid[item[1]][item[0]] = 0
        count = max(count, bfs(visited))
        for item in current:
            grid[item[1]][item[0]] = 1
        return

    for index in range(len(walls)):
        current.append(walls[index])
        backtrack(current, index + 1)
        current.pop()


backtrack([],0)
print(count)