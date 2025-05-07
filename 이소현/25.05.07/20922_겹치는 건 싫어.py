'''
20922_겹치는 건 싫어

문제
홍대병에 걸린 도현이는 겹치는 것을 매우 싫어한다. 특히 수열에서 같은 원소가 여러 개 들어 있는 수열을 싫어한다. 도현이를 위해 같은 원소가 
$K$개 이하로 들어 있는 최장 연속 부분 수열의 길이를 구하려고 한다.

 100,000 이하의 양의 정수로 이루어진 길이가 
N인 수열이 주어진다.  이 수열에서 같은 정수를 
K개 이하로 포함한 최장 연속 부분 수열의 길이를 구하는 프로그램을 작성해보자.

입력
첫째 줄에 정수 N(1<=N<=200000)과 K (1 <= K <= 100) 가 주어진다.


둘째 줄에는 a_1, a_2, ... a_n 이 주어진다 (1 <= a_i <= 100,000)

출력
조건을 만족하는 최장 연속 부분 수열의 길이를 출력한다.

예제 입력 1 
9 2
3 2 5 5 6 4 4 5 7
예제 출력 1 
7
예제 입력 2 
10 1
1 2 3 4 5 6 6 7 8 9
예제 출력 2 
6


<시간초과 풀이>
N, K = map(int, input().split())
A = list(map(int, input().split()))

start = 0
long_len = 0

for end in range(N):
    if A[start:end+1].count(A[end]) > K:
        while A[start] != A[end]:
            start += 1
        start += 1  

    long_len = max(long_len, end - start + 1)

print(long_len)
-> 딕셔너리 사용하도록 수정하여 통과


<깔끔한 풀이>
from collections import defaultdict

count = defaultdict(int)
start = 0

for end in range(N):
    count[A[end]] += 1
    while count[A[end]] > K:
        count[A[start]] -= 1
        start += 1

defaultdict는 Python 표준 라이브러리 collections에 있는 특별한 딕셔너리 타입
딕셔너리에 없는 key에 접근해도 자동으로 기본값을 넣어줌
매번 if num not in count: 같은 체크 없이
count[num] += 1 처럼 깔끔하고 안전하게 코드를 쓸 수 있음

'''
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 현재 슬라이딩 윈도우(start~end) 내에서 각 숫자의 등장 횟수를 저장하는 딕셔너리
count = {}

# start: 슬라이딩 윈도우의 시작 인덱스
start = 0

# max_len: 조건을 만족하는 가장 긴 부분 수열의 길이
max_len = 0

# end: 슬라이딩 윈도우의 끝 인덱스 (0부터 N-1까지 순회)
for end in range(N):
    num = A[end]  # 현재 새로 포함하려는 숫자

    # 딕셔너리에 해당 숫자가 없으면 0으로 초기화 (defaultdict 없이 처리)
    if num not in count:
        count[num] = 0
    count[num] += 1  # 현재 숫자의 등장 횟수 1 증가

    # 현재 숫자의 등장 횟수가 K를 초과한 경우 → 조건을 만족시키기 위해 start를 오른쪽으로 이동
    while count[num] > K:
        count[A[start]] -= 1  #윈도우에서 제거할 숫자, 제거되는 숫자의 등장 횟수 감소
        start += 1  # 윈도우의 시작 위치를 오른쪽으로 이동

    # 조건을 만족하는 현재 구간의 길이(end - start + 1)를 max_len과 비교하여 갱신
    max_len = max(max_len, end - start + 1)

# 최종 결과 출력: 조건을 만족하는 가장 긴 연속 부분 수열의 길이
print(max_len)