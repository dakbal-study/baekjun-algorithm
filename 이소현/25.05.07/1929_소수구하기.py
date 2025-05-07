'''
1929-소수구하기
https://www.acmicpc.net/problem/1929

문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

예제 입력 1 
3 16
예제 출력 1 
3
5
7
11
13

<시간초과 풀이>
M,N = map(int, input().split())


for num in range(M,N+1):   
    prime_num = True
    for i in range(2, num): # 2부터 (x - 1)까지의 모든 수를 확인
        # x가 해당 수로 나누어떨어진다면
        if num % i == 0:
            prime_num = False
            break

    if(prime_num):        
        print(num)
'''

M,N = map(int, input().split())

array = [True for i in range(N + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화
array[0] = array[1] = False  # 0과 1은 소수가 아니므로 False 처리
# 에라토스테네스의 체 알고리즘 
for i in range(2, int(N ** 0.5) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인 (모든 합성수는 √n 이하의 소수를 약수로 가지기 때문에 소수 판별 시 √n까지만 검사)
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # 소수 i의 배수 중, 아직 안 지워진 i*i부터 N까지를 하나씩 지움
        for j in range(i * i, N + 1, i):
            array[j] = False

# 모든 소수 출력
for i in range(M, N + 1):
    if array[i]:
        print(i)