def backtracking(idx, path):
    if len(path) == 6:
        print(*path)
        return

    for i in range(idx+1, len(lotto)):
        path.append(lotto[i])
        backtracking(i, path)
        path.pop()

while True:
    lis = list(map(int, input().split(" ")))
    lotto = lis[1:]

    if lis[0] == 0:     # 입력 종료 조건
        break

    for i in range(len(lotto) - 5):     # i가 맨 마지막 6개를 뽑는 경우의 수 까지 탐방
        backtracking(i, [lotto[i]])
    print()
