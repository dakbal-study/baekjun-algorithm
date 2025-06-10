#닫힐 때를 기준으로 열려있는 괄호의 갯수를 더해줌

s = input()
lis = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(':
        lis.append('(')
    else:
        lis.pop()
        if s[i - 1] == '(':
            cnt += len(lis)
        else:
            cnt += 1

print(cnt)
