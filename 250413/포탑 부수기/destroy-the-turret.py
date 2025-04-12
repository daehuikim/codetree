from collections import deque

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
last_attack = [[0 for _ in range(M)] for _ in range(N)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def set_attacker(last_attack):
    candidates = []
    for y in range(N):
        for x in range(M):
            if grid[y][x] > 0:
                candidates.append((grid[y][x], -last_attack[y][x], -(x + y), -x, x, y))
    candidates.sort()
    _, _, _, _, a_x, a_y = candidates[0]
    return a_x, a_y

def set_target(last_attack):
    candidates = []
    for y in range(N):
        for x in range(M):
            if grid[y][x] > 0:
                candidates.append((-grid[y][x], last_attack[y][x], (x + y), x, x, y))
    candidates.sort()
    _, _, _, _, t_x, t_y = candidates[0]
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
                nx = M-1
            if ny< 0:
                ny = N-1
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
    a_x, a_y = set_attacker(last_attack)
    last_attack[a_y][a_x] = t

    # set target
    t_x, t_y = set_target(last_attack)
    # BFS for laizer
    visited = [[False for _ in range(M)] for _ in range(N)]
    parent = [[(-1,-1) for _ in range(M)] for _ in range(N)]
    engaged = [[False for _ in range(M)] for _ in range(N)]
    engaged[a_y][a_x] = True
    engaged[t_y][t_x] = True
    grid[a_y][a_x] += (N + M)
    damage = grid[a_y][a_x]
    signal = bfs(a_x,a_y,t_x,t_y,visited,parent)

    if signal == 0:
        valid_path = extract_path(parent,a_x,a_y,t_x,t_y)
        for i in range(1,len(valid_path)):
            x,y=valid_path[i]
            engaged[y][x] = True
            if i == len(valid_path) - 1:
                grid[y][x] = max(0,grid[y][x]- damage)
                engaged[y][x]=True
            else:
                grid[y][x] = max(0,grid[y][x]- (damage//2))
                engaged[y][x] = True
    elif signal == -1:
        for i in range(-1,2):
            for j in range(-1,2):
                nx, ny = t_x + j, t_y + i
                if nx < 0:
                    nx = M-1
                if ny < 0:
                    ny = N-1
                nx %= M
                ny %= N
                if ny==t_y and nx==t_x and grid[ny][nx] != 0:
                    grid[ny][nx] = max(0,grid[ny][nx]-damage)
                    engaged[ny][nx] = True
                elif (ny!=t_y or nx!=t_x) and grid[ny][nx] != 0:
                    grid[ny][nx] = max(0,grid[ny][nx]-(damage//2))
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
