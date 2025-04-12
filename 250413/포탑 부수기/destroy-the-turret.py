from collections import deque
import sys
import math
input = sys.stdin.readline

# 입력 읽기
N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
last_attack = [[0 for _ in range(M)] for _ in range(N)]

# 네 방향 이동 (우, 하, 좌, 상)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def select_tower():
    """
    살아있는 포탑(체력이 0이 아닌 셀)들을 조건에 따라 정렬합니다.
    정렬 기준은
      1. 공격력(grid 값) 오름차순,
      2. 마지막 공격 턴(-last_attack) 역순,
      3. (행+열) 값 역순,
      4. 열 값 역순
    정렬된 리스트에서 0번째 원소를 attacker, 마지막 원소를 target으로 선택합니다.
    """
    candidates = []
    for y in range(N):
        for x in range(M):
            if grid[y][x] != 0:
                # 튜플 순서: (공격력, -last_attack, -(y+x), -x, y, x)
                candidates.append((grid[y][x], -last_attack[y][x], -(y+x), -x, y, x))
    if not candidates:
        return (-1, -1), (-1, -1)
    candidates.sort()
    # 0번째가 attacker, 마지막이 target
    # 튜플의 마지막 두 요소를 (y, x) 순서로 저장해두었으므로 반환시 순서를 (x, y)로 조정합니다.
    _, _, _, _, att_y, att_x = candidates[0]
    _, _, _, _, tgt_y, tgt_x = candidates[-1]
    return (att_x, att_y), (tgt_x, tgt_y)

def can_go(x, y, visited):
    # grid 값이 0이 아니고 아직 방문하지 않은 셀이면 이동 가능
    return grid[y][x] != 0 and not visited[y][x]

def bfs(source_x, source_y, target_x, target_y):
    """
    토로이달(격자 wrap-around) 이동을 적용하며, 현재 grid 상태에서 BFS를 진행해
    source에서 target으로 가는 최단 경로를 찾습니다.
    경로가 존재하면 (x,y) 좌표 리스트를 반환하고, 없으면 None을 반환합니다.
    """
    visited = [[False]*M for _ in range(N)]
    parent = [[(-1, -1)]*M for _ in range(N)]
    q = deque()
    q.append((source_x, source_y))
    visited[source_y][source_x] = True
    parent[source_y][source_x] = (source_x, source_y)
    
    found = False
    while q:
        x, y = q.popleft()
        if (x, y) == (target_x, target_y):
            found = True
            break
        for i in range(4):
            nx = (x + dx[i]) % M
            ny = (y + dy[i]) % N
            if can_go(nx, ny, visited):
                visited[ny][nx] = True
                parent[ny][nx] = (x, y)
                q.append((nx, ny))
    if not found:
        return None

    # 역추적하여 경로 복원
    path = []
    cx, cy = target_x, target_y
    while (cx, cy) != (source_x, source_y):
        path.append((cx, cy))
        cx, cy = parent[cy][cx]
    path.append((source_x, source_y))
    path.reverse()
    return path

def apply_attack(attacker, target, t):
    """
    공격자(attacker)가 target을 향해 공격합니다.
    BFS를 통해 경로가 있으면 해당 경로의 intermediate 셀에는 (damage//2)만큼,
    target 셀에는 full damage만큼 피해를 줍니다.
    만약 BFS 경로가 없으면, target 셀에 전액 데미지를 주고 target 주변 8칸에 (damage//2) 피해를 줍니다.
    공격 후, 공격하지 않은 (engaged되지 않은) 포탑은 체력이 1씩 증가합니다.
    """
    ax, ay = attacker
    tx, ty = target
    # 공격자의 최근 공격 턴 기록 갱신
    last_attack[ay][ax] = t
    # 보너스 만큼 공격자 체력 증가 (격자 크기 N+M)
    grid[ay][ax] += (N + M)
    damage = grid[ay][ax]
    
    # engaged: 이번 공격에서 피해를 준(또는 공격에 참여한) 셀 표시
    engaged = [[False]*M for _ in range(N)]
    engaged[ay][ax] = True
    
    path = bfs(ax, ay, tx, ty)
    if path is not None:
        # 경로가 있으면, attacker는 이미 bonus 반영됨.
        # intermediate 셀에는 damage의 절반, target에는 full damage 적용.
        for idx, (x, y) in enumerate(path):
            engaged[y][x] = True
            if idx == 0:
                continue  # attacker 셀은 이미 처리됨.
            elif (x, y) == (tx, ty):
                grid[y][x] = max(0, grid[y][x] - damage)
            else:
                grid[y][x] = max(0, grid[y][x] - (damage // 2))
    else:
        # 경로가 없으면, target에 full damage,
        # target 주변 8칸에 (damage // 2) 피해 적용 (토로이달 처리)
        grid[ty][tx] = max(0, grid[ty][tx] - damage)
        engaged[ty][tx] = True
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx = (tx + j + M) % M
                ny = (ty + i + N) % N
                if (nx, ny) == (tx, ty):
                    continue
                # 조건: 살아있고, 공격자 셀이 아니며, 아직 이번 공격에 관여하지 않은 경우
                if grid[ny][nx] != 0 and (nx, ny) != (ax, ay) and not engaged[ny][nx]:
                    grid[ny][nx] = max(0, grid[ny][nx] - (damage // 2))
                    engaged[ny][nx] = True
    # 이번 공격에 관여하지 않은 모든 포탑은 체력 1 증가
    for y in range(N):
        for x in range(M):
            if not engaged[y][x] and grid[y][x] != 0:
                grid[y][x] += 1

# 시뮬레이션 진행
for t in range(1, K + 1):
    alive = sum(1 for y in range(N) for x in range(M) if grid[y][x] != 0)
    if alive <= 1:
        break
    attacker, target = select_tower()
    if attacker == (-1, -1) or target == (-1, -1):
        break
    apply_attack(attacker, target, t)

def get_max_value():
    ans = 0
    for y in range(N):
        for x in range(M):
            ans = max(ans, grid[y][x])
    return ans

print(get_max_value())
