def count_pieces(arrangement):
    stack = []
    pieces = 0
    
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            stack.append('(')
        else:
            stack.pop()
            if arrangement[i - 1] == '(':
                # 레이저인 경우
                pieces += len(stack)
            else:
                # 쇠막대기 끝
                pieces += 1
                
    return pieces

# 입력 받기
arrangement = input().strip()
print(count_pieces(arrangement))