K, N = map(int, input().split())

# Please write your code here.
def cons_three(answer):
    i=0
    while i<len(answer):
        j=i
        while j < len(answer) and answer[i]==answer[j]:
            j+=1
        length = j-i
        if length>=3:
            return False
        i=j
    return True

def choose(current,n,k,total):
    if len(current)==n:
        if cons_three(current):
            total.append(current[:])
        return
    for i in range(1,k+1):
        current.append(i)
        choose(current,n,k,total)
        current.pop()
    return total

results = choose([],N,K,[])
for result in results:
    print(' '.join(map(str,result)))