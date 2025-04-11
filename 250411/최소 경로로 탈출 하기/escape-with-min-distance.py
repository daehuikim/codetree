from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# Please write your code here.
def can_go(x, y):
    if 0 <= x < m and 0 <= y < n and a[y][x] == 1 and visited[y][x]==0:
        return True
    return False


def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = 0
    while q:
        x, y, distance = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if can_go(nx, ny):
                q.append((nx, ny, distance + 1))
                visited[ny][nx] = distance + 1

bfs()

if visited[n - 1][m - 1]!=0:
    print(visited[n - 1][m - 1])
else:
    print(-1)


