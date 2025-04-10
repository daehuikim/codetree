import copy

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
points = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            points.append((j, i))

# Please write your code here.
dx1 = [-1, 0, 1, 0]
dy1 = [0, -1, 0, 1]
dx2 = [-1, 1, 1, -1]
dy2 = [-1, -1, 1, 1]


def bomb_simulator(points, bombs):
    temp_grid = [[0] * n for _ in range(n)]

    # 1의 위치만 복사
    for y in range(n):
        for x in range(n):
            if grid[y][x] == 1:
                temp_grid[y][x] = 1
                
    count_bomb = 0
    for i in range(len(bombs)):
        x, y = points[i][0], points[i][1]
        if bombs[i] == 0:
            for j in range(-2, 3):
                ny = y + j
                if ny < 0 or ny >= n:
                    continue
                if temp_grid[ny][x] ==1:
                    continue
                temp_grid[ny][x] = 2
        elif bombs[i] == 1:
            for j in range(4):
                nx, ny = x + dx1[j], y + dy1[j]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if temp_grid[ny][nx] ==1:
                    continue
                temp_grid[ny][nx]= 2
        elif bombs[i] == 2:
            for j in range(4):
                nx, ny = x + dx2[j], y + dy2[j]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if temp_grid[ny][nx] ==1:
                    continue
                temp_grid[ny][nx] = 2

    count_bomb = sum(1 for row in temp_grid for val in row if val in (1, 2))

    return count_bomb


def get_fire(points, current):
    if len(points) == len(current):
        return bomb_simulator(points, current)
    count = 0
    for i in range(3):
        current.append(i)
        count = max(count, get_fire(points, current))
        current.pop()
    return count


print(get_fire(points, []))

