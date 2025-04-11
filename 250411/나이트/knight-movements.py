from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[False for _ in range(n)] for _ in range(n)]

# Please write your code here.
dx=[-2,-1,1,2,2,1,-1,-2]
dy=[-1,-2,-2,-1,1,2,2,1]

def can_go(x,y):
    if 0<=x<n and 0<=y<n and not visited[y][x]:
        return True
    return False

def bfs():
    q = deque()
    q.append((c1-1,r1-1,0))
    visited[r1-1][c1-1]=True
    target_x,target_y = c2-1,r2-1
    while q:
        x,y,trial = q.popleft()
        for i in range(8):
            nx,ny = x+dx[i],y+dy[i]
            if can_go(nx,ny):
                if nx==target_x and ny==target_y:
                    return trial+1
                q.append((nx,ny,trial+1))
                visited[ny][nx]=True
    return -1
if n==1:
    print(0)
else:
    print(bfs())