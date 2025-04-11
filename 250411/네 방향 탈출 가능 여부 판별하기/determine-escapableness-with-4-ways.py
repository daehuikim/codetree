from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def can_go(x,y):
    if 0<=x<m and 0<=y<n and a[y][x]==1:
        return True
    return False

def bfs():
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    q = deque([(0,0)])
    while q:
        current = q.popleft()
        x,y = current[0],current[1]
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if can_go(nx,ny):
                a[ny][nx]=2
                q.append((nx,ny))

bfs()
if a[n-1][m-1]==2:
    print(1)
else:
    print(0)
