N = int(input())

# Please write your code here.
memo = [-1 for _ in range(N)]
memo[0]=1
memo[1]=1
for i in range(2,N):
    memo[i]=memo[i-1]+memo[i-2]


print(memo[N-1])