n = int(input())
lis = [0] * 10001
dp = [0] * 10001

# dp[i] = k -> i까지 마실 수 있는 최대합 k
# 연속 세 잔이상 불가 -> i + i-1 + i-3 or i + i-2 or 현재 인덱스 선택 x

for _ in range(1, n+1):
    lis[_] = int(input())

dp[1] = lis[1]
dp[2] = lis[1] + lis[2]

for i in range(3, n+1):
    dp[i] = max(lis[i]+lis[i-1]+dp[i-3], lis[i]+dp[i-2], dp[i-1])

print(max(dp))