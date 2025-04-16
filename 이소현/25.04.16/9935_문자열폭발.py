'''
문제
상근이는 문자열에 폭발 문자열을 심어 놓았다. 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다.

폭발은 다음과 같은 과정으로 진행된다.

문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다. 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.
상근이는 모든 폭발이 끝난 후에 어떤 문자열이 남는지 구해보려고 한다. 남아있는 문자가 없는 경우가 있다. 이때는 "FRULA"를 출력한다.

폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.

입력
첫째 줄에 문자열이 주어진다. 문자열의 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다.

둘째 줄에 폭발 문자열이 주어진다. 길이는 1보다 크거나 같고, 36보다 작거나 같다.

두 문자열은 모두 알파벳 소문자와 대문자, 숫자 0, 1, ..., 9로만 이루어져 있다.

출력
첫째 줄에 모든 폭발이 끝난 후 남은 문자열을 출력한다.


입력1
mirkovC4nizCC44
C4
출력1
mirkovniz

입력2
12ab112ab2ab
12ab
출력2
FRULA
'''
'''
<시간 초과 난 풀이>
stack = list(input())
bomb = input()
bomb_len = len(bomb)
temp=""

while(stack):
    temp = stack.pop()+temp
    if temp.startswith(bomb):
        temp = temp[bomb_len:]

        # if len(temp) < bomb_len:
        #     stack.extend(list(temp)[::-1])
        #     temp = ""
        # else:
        #     stack.extend(list(temp[:-bomb_len])[::-1])
        #     temp = temp[:-bomb_len] 

if temp:
    print(temp)
else:
    print("FRULA")

<시간 초과 풀이 시간 복잡도>

stack.pop() + temp는 문자열 앞에 삽입 → O(N)

temp.startswith(bomb) → 문자열 비교 → O(M)

매 루프마다 temp 문자열 전체가 재생성됨 → 복사 비용 큼

결국 전체 시간복잡도는 O(N²) 이상
____________________________________________________________

<통과 풀이 시간 복잡도>
stack.append(char) → O(1)

'stack[-bomb_len:] → 슬라이싱 → 최대 O(M)

''.join(...) → 문자열 비교 비용은 폭발 문자열 길이에 비례 (O(M))

전체 루프는 문자열 길이 N만큼만 순회

시간 복잡도는 O(N × M) 수준


<알게된 점>
- 파이썬 슬라이싱은 범위 넘어가도 에러 발생 안함
  ㄴ 범위 내 요소만 반환, 없으면 빈 시퀀스
  ㄴ인덱싱은 해당 인덱스가 없으면 IndexError 발생


'''

string = input()
bomb = input()
bomb_len = len(bomb)

stack = []

for char in string:
    stack.append(char)  # 한 글자씩 스택에 넣음

    # 스택 끝이 폭발 문자열과 같은지 확인
    if ''.join(stack[-bomb_len:]) == bomb:
        # 폭발! => bomb 길이만큼 pop
        for _ in range(bomb_len):
            stack.pop()

# 결과 출력
result = ''.join(stack)
print(result if result else "FRULA")


