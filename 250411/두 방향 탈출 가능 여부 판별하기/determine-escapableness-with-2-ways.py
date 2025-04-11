n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
# Please write your code here.
dx=[0,1]
dy=[1,0]
def can_go(x,y):
    if 0<=x<m and 0<=y<n and grid[y][x]==1:
        return True
    return False

def dfs(x,y):
    visited[y][x]=True
    for i in range(2):
        nx,ny = x+dx[i],y+dy[i]
        if can_go(nx,ny):
            dfs(nx,ny)

dfs(0,0)

if visited[n-1][m-1]:
    print(1)
else:
    print(0)
    

