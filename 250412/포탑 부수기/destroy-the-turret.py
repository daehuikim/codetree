from collections import deque

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
last_attack = [[0 for _ in range(M)] for _ in range(N)]
last_target = [[0 for _ in range(M)] for _ in range(N)]
dx=[1,0,-1,0]
dy=[0,-1,0,1]

def set_attacker():
    candidate_value = 5001
    a_x, a_y = -1, -1
    for i in range(N):
        for j in range(M):
            if candidate_value > grid[i][j] and grid[i][j] != 0:
                candidate_value = min(candidate_value, grid[i][j])
                a_x, a_y = j, i

    turn = -1
    for i in range(N - 1, 0, -1):
        for j in range(M - 1, 0, -1):
            if candidate_value == grid[i][j]:
                if turn < last_attack[i][j]:
                    a_x, a_y = j, i
    return a_x, a_y

def set_target():
    candidate_value = -1
    t_x, t_y = -1, -1
    for i in range(N):
        for j in range(M):
            if candidate_value < grid[i][j] and grid[i][j] != 0:
                candidate_value = max(candidate_value, grid[i][j])
                t_x, t_y = j, i

    turn = 1001
    for i in range(N):
        for j in range(M):
            if candidate_value == grid[i][j]:
                if turn > last_attack[i][j]:
                    t_x, t_y = j, i
    return t_x, t_y

def can_go(x,y):
    if grid[y][x] != 0 and not visited[y][x]:
        return True
    return False

def bfs(cur_x,cur_y,target_x,target_y,visited,parent):
    q = deque()
    q.append((cur_x, cur_y))
    visited[cur_y][cur_x] = True
    parent[cur_y][cur_x] = (cur_x, cur_y)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx < 0:
                nx = M
            if ny< 0:
                ny = N
            nx%=M
            ny%=N
            if can_go(nx,ny):
                q.append((nx,ny))
                visited[ny][nx] = True
                parent[ny][nx] = (x,y)
            if nx==target_x and ny==target_y:
                return 0
    return -1

def extract_path(parent,source_x,source_y,target_x,target_y):
    indicator_x,indicator_y = target_x,target_y
    path=[(target_x,target_y)]
    while not(indicator_x == source_x and indicator_y == source_y):
        path.insert(0, parent[indicator_y][indicator_x])
        indicator_x, indicator_y = parent[indicator_y][indicator_x]
    return path

for t in range(1, K + 1):
    # set attacker
    a_x, a_y = set_attacker()
    last_attack[a_y][a_x] = t
    grid[a_y][a_x] += (N+M)
    damage = grid[a_y][a_x]
    # set target
    t_x, t_y = set_target()
    last_target[t_y][t_x] = t
    # BFS for laizer
    visited = [[False for _ in range(M)] for _ in range(N)]
    parent = [[(-1,-1) for _ in range(M)] for _ in range(N)]
    engaged = [[False for _ in range(M)] for _ in range(N)]
    engaged[a_y][a_x] = True
    engaged[t_y][t_x] = True
    signal = bfs(a_x,a_y,t_x,t_y,visited,parent)
    if signal == 0:
        valid_path = extract_path(parent,a_x,a_y,t_x,t_y)
        for i in range(len(valid_path)):
            x,y=valid_path[i]
            engaged[y][x] = True
            if i == len(valid_path) - 1:
                grid[y][x] = max(0,grid[y][x]- damage)
            else:
                grid[y][x] = max(0,grid[y][x]- (damage//2))
    elif signal == -1:
        for i in range(-1,2):
            for j in range(-1,2):
                nx, ny = t_x + j, t_y + i
                if nx < 0:
                    nx = M
                if ny < 0:
                    ny = N
                nx %= M
                ny %= N
                
                if i==t_y and j==t_x and grid[ny][nx] != 0:
                    grid[i][j] = max(0,grid[i][j]-damage)
                    engaged[ny][nx] = True
                elif (i!=t_y or j!=t_x) and grid[ny][nx] != 0:
                    grid[i][j] = max(0,grid[i][j]-(damage//2))
                    engaged[ny][nx] = True

    for i in range(N):
        for j in range(M):
            if not engaged[i][j] and grid[i][j] != 0:
                grid[i][j]+=1

def get_max_value(arr):
    max_value = -1
    for i in range(N):
        for j in range(M):
            max_value = max(max_value, arr[i][j])
    return max_value


print(get_max_value(grid))
