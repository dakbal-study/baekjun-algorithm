n = int(input())
lis = list(map(int, input().split(" ")))
dp = [0] * n

for i in range(n):
    for j in range(i):
        if lis[j] < lis[i] and dp[i] < dp[j]:
            dp[i] = dp[j]

    dp[i] += 1

print(max(dp))