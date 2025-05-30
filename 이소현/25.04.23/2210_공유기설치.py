"""
공유기 설치


공유기 설치 다국어
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	88523	32706	22497	37.356%
문제
도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 
한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

입력
첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

출력
첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

예제 입력 1 
5 3
1
2
8
4
9
예제 출력 1 
3
힌트
공유기를 1, 4, 8 또는 1, 4, 9에 설치하면 가장 인접한 두 공유기 사이의 거리는 3이고, 이 거리보다 크게 공유기를 3개 설치할 수 없다.


"""
#GPT 풀이

# 공유기를 거리 dist로 설치 가능한지 확인하는 함수,집들 사이의 거리를 dist 이상으로 유지하면서 공유기 c개를 설치할 수 있는지 확인
#c: 설치해야 하는 공유기의 목표 개수
#count: 지금까지 설치한 공유기의 개수
def can_install(houses, dist, c):
    count = 1
    last_installed = houses[0]

    for i in range(1, len(houses)):
        if houses[i] - last_installed >= dist:
            count += 1
            last_installed = houses[i]
        if count >= c:
            return True
    return False


# 입력 처리
n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

# 탐색하는 값 : 공유기 사이의 거리 값, 모든 공유기를 설치 가능한 최댓값 
# 이진 탐색 범위: 최소 거리, 최대 거리 = 가장 먼 두 집 차이
# 그 중 중간 값을 시작으로 이진 탐색 시도
start = 1
end = houses[-1] - houses[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    if can_install(houses, mid, c):
        result = mid         # 설치 가능하면 거리 늘려보기
        start = mid + 1
    else:
        end = mid - 1        # 설치 불가 → 거리 줄이기

print(result)
