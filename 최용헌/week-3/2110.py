n, c = map(int, input().split(" "))
lis = []

# 공유기의 최소 거리가 최대한 크게 되어야함 (최소에 대한 최대값)
# 집, 공유기의 개수가 각각 20만개이므로 bfs는 불가할듯

# 이분탐색 사용 용도
# 1. 정렬된 배열에서의 특정값 찾기
# 2. 조건을 만족하는 최소 or 최대값 찾기
# 3. 정답이 범위 내에 존재하며 조건을 만족하는지 판단 가능할 때

# 즉, 해당 문제는 2번 유형에 해당함. (해당 거리 설치 가능인지 확인 후(최소값) 최대값 찾기)
# 거리 d를 이분탐색 (lis[0] <= d <= lis[-1])

for _ in range(n):
    lis.append(int(input()))

lis.sort()

start, end = 1, lis[-1] - lis[0]
res = 0

while start <= end:
    mid = (start + end) // 2
    prev, cnt = lis[0], 1

    for i in range(1, n):
        if lis[i] - prev >= mid:
            cnt += 1
            prev = lis[i]

    if cnt >= c:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)




