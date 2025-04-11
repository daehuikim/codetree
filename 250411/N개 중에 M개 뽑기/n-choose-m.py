N, M = map(int, input().split())
ans=set()
# Please write your code here.
def check_diff(answer):
    for i in range(len(answer)):
        for j in range(len(answer)):
            if i!=j and answer[i]==answer[j]:
                return False
    return True

def choose(current):
    global ans

    if len(current)==M:
        if check_diff(current):
            key = tuple(sorted(current))
            ans.add(key)
        return
    
    for i in range(1,N+1):
        current.append(i)
        choose(current)
        current.pop()
    return

choose([])
for item in sorted(ans):
     print(' '.join(map(str, item)))