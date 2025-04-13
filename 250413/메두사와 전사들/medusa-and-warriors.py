from collections import deque

# Input part
N,M = map(int,input().split())
m_y, m_x, e_y, e_x = map(int,input().split())
warriors = list(map(int,input().split()))
candidates_x=[]
candidates_y=[]
for i in range(len(warriors)):
    if i%2==0:
        candidates_y.append(warriors[i])
    else:
        candidates_x.append(warriors[i])
grid = [list(map(int,input().split())) for _ in range(N)]

# Pre-defined variables
dx1=[0,0,-1,1]
dy1=[-1,1,0,0]
dx2=[-1,1,0,0]
dy2=[0,0,-1,1]

# Logic part
medusa_visited = [[N**2 for _ in range(N)] for _ in range(N)]

def bfs_medusa(cur_x,cur_y):
    q = deque()
    time=0
    q.append((cur_x,cur_y,time))
    path = [(cur_x,cur_y)]
    medusa_visited[cur_y][cur_x]=0
    while q:
        x,y,time = q.popleft()
        if x==e_x and y==e_y:
            break
        for i in range(4):
            nx,ny = x+dx1[i], y+dy1[i]
            if 0<=nx<N and 0<=ny<N and medusa_visited[ny][nx]>time+1 and grid[ny][nx]==0:
                q.append((nx,ny,time+1))
                medusa_visited[ny][nx]=time +1
                path.append((nx,ny))
    return path,time

for item in medusa_visited:
    print(item)
print(bfs_medusa(m_x,m_y))
