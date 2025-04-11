n = int(input())

# Please write your code here.
def choose(current, used):
    if len(current) == n:
        print(' '.join(map(str,current)).strip())
        return
    
    for i in range(1, n+1):
        if not used[i]:
            used[i] = True
            current.append(i)
            choose(current, used)
            current.pop()
            used[i] = False

used = [False] * (n + 1)
choose([],used)