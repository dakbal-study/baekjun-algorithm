# 단방향 그래프 // 6 -> 2 != 2 -> 6

def dfs(start, current, visit):
    for i in range(n):
        if lis[start][i] and not visit[i]:
            visit[i] = 1
            res[start][i] = 1
            dfs(start, i, visit)

n = int(input())
lis = []
res = [[0] * n] * n
visit = [0] * n 

for _ in range(n):
    lis.append(list(map(int, input().split(" "))))

for i in range(n):
    dfs(i, i, visit)

for r in res:
    print(*r)

