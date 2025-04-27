# 해당 원소 i가 다른 원소 j 보다 클 때의 갯수
# 즉, 해당원소보다 작은 원소들의 갯수
# -10 -9 2 4 4 -> set 처리 -> -10 -9 2 4 -> list sort

n = int(input())
lis = list(map(int, input().split(" ")))
s = set(lis)

l = sorted(list(s))
dic = {}

for i in range(len(l)):
    dic[l[i]] = i

for i in lis:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")
