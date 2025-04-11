from collections import deque

N = int(input())
seen = [False for _ in range(1000001)]


# Please write your code here.

def bfs():
    trial = 0
    q = deque()
    q.append((N, trial))
    seen[N] = True

    while q:
        x, trial = q.popleft()
        if x == 1:
            seen[x] = True
            break

        nx = x - 1
        if seen[nx] == False and 1 <= nx <= 1000000:
            q.append((nx, trial + 1))
            seen[nx] = True

        nx = x + 1
        if seen[nx] == False and 1 <= nx <= 1000000:
            q.append((nx, trial + 1))
            seen[nx] = True

        nx = x // 2
        if seen[nx] == False and 1 <= nx <= 1000000 and x % 2 == 0:
            q.append((nx, trial + 1))
            seen[nx] = True

        nx = x // 3
        if seen[nx] == False and 1 <= nx <= 1000000 and x % 3 == 0:
            q.append((nx, trial + 1))
            seen[nx] = True
    return trial


print(bfs())