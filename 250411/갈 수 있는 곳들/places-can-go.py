from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]
visited = [[False for _ in range(n)] for _ in range(n)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]

# Please write your code here.
def can_go(x,y,value):
    if 0<=x<n and 0<=y<n and grid[y][x]==value and not visited[y][x]:
        return True
    return False

def bfs(item):
    q=deque([])
    q.append((item[0]-1,item[1]-1))
    value = grid[item[0]-1][item[1]-1]
    visited[item[0]-1][item[1]-1]=True
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if can_go(nx,ny,value):
                visited[ny][nx]=True
                q.append((ny,nx))

for point in points:
    bfs(point)

result=0
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            result+=1
print(result)
