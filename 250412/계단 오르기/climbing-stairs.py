n = int(input())
MOD=10007
# Please write your code here.
memo = [0 for _ in range(n+10)]
memo[0]=1
memo[1]=0
memo[2]=1
memo[3]=1

for i in range(4,n+1):
    memo[i]=(memo[i-2]+memo[i-3])%MOD

print(memo[n])