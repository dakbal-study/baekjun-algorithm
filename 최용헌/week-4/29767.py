n, m = map(int, input().split(" "))
lis = list(map(int, input().split(" ")))
dp = [0] * n
dp[0] = lis[0]

for i in range(1,n):
    dp[i] = dp[i-1] + lis[i]

dp.sort(reverse=True)
print(sum(dp[:m]))