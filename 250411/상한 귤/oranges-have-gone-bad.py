from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
temp_grid=[[10001 for _ in range(n)] for _ in range(n)]

# Please write your code here.
dx=[0,0,-1,1]
dy=[-1,1,0,0]

candidates=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==2:
            candidates.append((j,i))
        elif grid[i][j]==0:
            temp_grid[i][j]=-1

def can_go(x,y):
    if 0<=x<n and 0<=y<n and grid[y][x]==1 and not visited[y][x]:
        return True
    return False

def bfs(cur_x,cur_y,visited):
    q = deque()
    q.append((cur_x,cur_y,0))
    visited[cur_y][cur_x]=True
    temp_grid[cur_y][cur_x]=0
    
    while q:
        x,y,time = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if can_go(nx,ny):
                q.append((nx,ny,time+1))
                visited[ny][nx]=True
                temp_grid[ny][nx]=min(temp_grid[ny][nx],time+1)

for candidate in candidates:
    visited = [[False for _ in range(n)] for _ in range(n)]
    bfs(candidate[0],candidate[1],visited)

for i in range(n):
    for j in range(n):
        if temp_grid[i][j]==10001:
            temp_grid[i][j]=-2

for item in temp_grid:
    print(' '.join(map(str,item)).strip())

