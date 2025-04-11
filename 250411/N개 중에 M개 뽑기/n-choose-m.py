N, M = map(int, input().split())
ans=set()
# Please write your code here.
def choose(start,current):
    global ans

    if len(current)==M:
        ans.add(tuple(current))
        return
    
    for i in range(start,N+1):
        current.append(i)
        choose(i+1,current)
        current.pop()
    return

choose(1,[])
for item in sorted(ans):
     print(' '.join(map(str, item)))