# n*n 격자 -> n^2 명
# 각 학생은 4명의 선호도가 나옴
# 인접 = 상하좌우

# 1. 인접한 칸에 선호 학생이 많아야함. -> 모든 칸을 탐색하며 선택된 학생과 선호학생이 몇명인지 카운트 ex. (count, blank, y, x)
# 2. 1번 선택지가 여러개면 인접칸이 가장 많이 비어있는 자리 선택 -> 위 리스트를 count로 정렬한 뒤 좌표 주변이 비어있는지 체크
# 3. 2번 선택지가 여러개면 행 > 열 번호가 작은 순으로 선택

# 출력 = 만족도 (좋아하는 인접 학생이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.)

mx = [1, -1, 0, 0]      # 동서남북
my = [0, 0, -1, 1]

n = int(input())
student = [[]]      # 입력받을 학생
res = 0     # 정답 점수
dic = {}        # 학생들의 좌표 저장 -> number:(x,y)
score = {0:0, 1:1, 2:10, 3:100, 4:1000}     # 만족도

for _ in range(n*n):
    student.append(list(map(int, input().split(" "))))

lis = [[0 for _ in range(n)] for _ in range(n)]     # 학생 배치도

for l in student[1:]:
    number, preferlist = l[0], l[1:]        # 학생번호, 선호하는 학생 리스트
    sortList = []

    # case 1. 모든 칸을 탐색하며 선택된 학생과 선호학생이 몇명인지 카운트
    for r in range(n):
        for c in range(n):
            prefer, blank = 0, 0      # 해당 좌표에서의 인접하는 선호 학생 수, 비어있는 칸 수

            if lis[r][c] != 0:      # 이미 배치된 곳은 건너뜀
                continue

            for i in range(4):      # 해당 좌표에서 4방향을 모두 체크
                dx = mx[i] + r
                dy = my[i] + c

                if 0 <= dx < n and 0 <= dy < n:
                    if lis[dx][dy] in preferlist:       # 4방향 안에 선호하는 학생이 있다면
                        prefer += 1
                    if lis[dx][dy] == 0:
                        blank += 1

            sortList.append((prefer, blank, r, c)) # 4방향 모두 체크한 뒤 좌표와 선호학생 수를 넣음

    # case 2. prefer, blank, row, col 순으로 정렬시킴 (좌표는 순서대로 정렬)
    sortList = sorted(sortList, key=lambda x:(x[0], x[1], -x[2], -x[3]), reverse=True)    # prefer 정렬
    lis[sortList[0][2]][sortList[0][3]] = number        # 선호하는 학생 순, 인접 빈칸 순으로 차례대로 정렬
    dic[number] = (sortList[0][2], sortList[0][3])

# 3. 점수 계산하기
for s in student[1:]:
    number, preferlist = s[0], s[1:]        # ex. 4번학생, 선호 = 2517
    c = 0       # 주변에 선호하는 학생 값
    xdic, ydic = dic[number][0], dic[number][1]     # 해당 학생의 좌표

    for i in range(4):
        dx = xdic + mx[i]
        dy = ydic + my[i]

        if 0 <= dx < n and 0 <= dy < n:
            for p in preferlist:
                if lis[dx][dy] == p:
                    c += 1

    res += score[c]

print(res)
