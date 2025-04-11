n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
def goal_check(answer,m):
    count=0
    count_dict = {item[0]: 0 for item in answer}
    for a in answer:
        count_dict[a[0]]+=a[1]
    for val in count_dict.values():
        if val >= m-1:
            count += 1
    return count

def choose(depth,current,k,n,m):
    if depth==n:
        return goal_check(current,m)
    
    count_dict = {i: 0 for i in range(k)}
    for a in current:
        count_dict[a[0]] += a[1]

    remaining = sum(nums[depth:])  # 남은 명령 점수 총합
    possible = 0
    for i in range(k):
        if count_dict[i] + remaining >= m:  # m 도달 가능성 있는 agent 수
            possible += 1

    # pruning: 지금 가능한 최대값이 너무 작으면 의미 없음
    if possible <= 0:
        return 0

    count=0
    num = nums[depth]
    for i in range(k):
        current.append((i,num))
        count = max(count, choose(depth+1,current,k,n,m))
        current.pop()
    return count

print(choose(0,[],k,n,m))