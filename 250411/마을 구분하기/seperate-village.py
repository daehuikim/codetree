import copy
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = copy.deepcopy(grid)
# Please write your code here.
dx=[0,0,-1,1]
dy=[-1,1,0,0]

def can_go(x,y):
    if 0<=x<n and 0<=y<n and visited[y][x]==1:
        return True
    return False

def dfs(x,y):
    visited[y][x] = 2
    count=1
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if can_go(nx,ny):
            visited[ny][nx]=2
            count+=dfs(nx,ny)
    return count

towns=[]
for i in range(n):
    for j in range(n):
        if visited[i][j]==1:
            size = dfs(j,i)
            towns.append(size)
towns.sort()
print(len(towns))
for item in towns:
    print(item)
