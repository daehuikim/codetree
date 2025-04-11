import sys
sys.setrecursionlimit(10**4)
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
candidates = sorted(set(num for row in grid for num in row))

# Please write your code here.
dx=[0,0,-1,1]
dy=[-1,1,0,0]

def can_go(x,y,target,visited):
    if 0<=x<n and 0<=y<n and grid[y][x]==target and not visited[y][x]:
        return True
    return False

def dfs(x,y,target,visited):
    visited[y][x]=True
    count=1
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if can_go(nx,ny,target,visited):
            count += dfs(nx,ny,target,visited)
    return count

max_blocks=0
bomb_count=0
for item in candidates:
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j]==item and not visited[i][j]:
                value = dfs(j,i,item,visited)
                if value>=4:
                    bomb_count+=1
                max_blocks = max(max_blocks,value)

print(bomb_count,max_blocks)






