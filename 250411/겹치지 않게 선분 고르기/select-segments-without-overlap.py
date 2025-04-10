n = int(input())
segments = []

for _ in range(n):
    a, b = map(int, input().split())
    segments.append((a, b))

# 끝나는 시간 기준으로 정렬
segments.sort(key=lambda x: x[1])

def dfs(index, count, last_end):
    if index == n:
        return count
    # 현재 선분을 선택하지 않는 경우
    res = dfs(index + 1, count, last_end)

    # 현재 선분을 선택할 수 있는 경우
    if segments[index][0] > last_end:
        res = max(res, dfs(index + 1, count + 1, segments[index][1]))

    return res

print(dfs(0, 0, -float('inf')))
