from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# Please write your code here.
dx=[0,0,-1,1]
dy=[-1,1,0,0]

def can_go(x,y,visited):
    if 0<=x<n and 0<=y<n and grid[y][x]!=1 and not visited[y][x]:
        return True
    return False

def bfs(cur_x,cur_y,visited):
    q = deque()
    q.append((cur_x,cur_y,0))
    visited[cur_y][cur_x]=True
    while q:
        x,y,time = q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if can_go(nx,ny,visited):
                visited[ny][nx]=True
                if grid[ny][nx]==3:
                    return (cur_x,cur_y,time+1)
                q.append((nx,ny,time+1))
    return (cur_x,cur_y,-1)

candidates=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==2:
            visited = [[False for _ in range(n)] for _ in range(n)]
            candidate = bfs(j,i,visited)
            candidates.append(candidate)

results = [[0 for _ in range(n)] for _ in range(n)]
for item in candidates:
    results[item[1]][item[0]]=item[2]

for item in results:
    print(' '.join(map(str,item)).strip())


