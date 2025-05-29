from collections import defaultdict

def dfs(start, path):
    path.add(start)
    visit[start] = 1

    for i in dic[start]:
        if i not in path:
            dfs(i, path.copy())
        else:
            result.extend(list(path))
            return

n = int(input())
dic = defaultdict(list)
result = []

for i in range(1,n+1):
    dic[int(input())].append(i)

visit = [0] * (n+1)

for i in range(1, n+1):
    if not visit[i]:
        dfs(i, set([]))

print(len(result))
result.sort()

for i in result:
    print(i)