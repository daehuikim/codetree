n = int(input())
MOD=10007
# Please write your code here.
memo = [0 for _ in range(n+10)]
memo[0]=1
memo[1]=1

for i in range(2,n+1):
    memo[i]=(memo[i-1] + memo[i-2])%MOD

print(memo[n])