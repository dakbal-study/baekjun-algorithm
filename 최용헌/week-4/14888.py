# 연산자를 배치해서 만들 수 있는 최대, 최소값
# 백트래킹으로 모든 oper 경우의 수 생성

import sys
input = sys.stdin.readline

def backtracking(path, operList, visit):
    global op

    if len(path) == n-1:
        op.append(path[:])
        return

    for i in range(len(operList)):
        if not visit[i]:
            path.append(operList[i])
            visit[i] = 1
            backtracking(path, operList, visit)
            visit[i] = 0
            path.pop()


n = int(input())
number = list(map(int, input().split(" ")))
oper = list(map(int, input().split(" ")))
operList = []       # 연산자 나열하기
op = []     # 연산자 모든 경우의 수

maxVal, minVal = -sys.maxsize, sys.maxsize

s = ["+", "-", "*", "/"]

# oper를 통해 만들 수 있는 연산자의 모든 원소
for i in range(4):
    for j in range(oper[i]):
        operList.append(s[i])

visit = [0] * (len(operList))
backtracking([], operList, visit)

for o in op:        # o = +*, *+ ...
    r = number[0]

    for i in range(len(o)):
        if o[i] == "+":
            r += number[i+1]
        elif o[i] == "-":
            r -= number[i+1]
        elif o[i] == "*":
            r *= number[i+1]
        elif o[i] == "/":
            if r < 0:  # 음수를 양수로 나누는 경우 처리 (C++ 방식으로)
                r = -(-r // number[i + 1])
            else:
                r //= number[i + 1]

    maxVal = max(maxVal, r)
    minVal = min(minVal, r)

print(maxVal)
print(minVal)

