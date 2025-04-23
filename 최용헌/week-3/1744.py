# -, +, *을 통해 최대 합
# 두 수를 적절히 묶기
# 양수, 음수에 따라 달라짐
# 양수 => 0과 1은 + > * 이며, 나머지의 경우 * > + 이다
# 음수 => *이 -보다 큼(ex. -1*-2 = 2 / -1--2 = 1)

n = int(input())
plus, minus = [], []
res = 0

for _ in range(n):
    num = int(input())

    if num > 1:
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    else:
        res += num


plus.sort(reverse=True) # [9,8,6,2,1]
minus.sort()    # [-1,-3,-5,-7]

for i in range(0, len(plus), 2):
    if i+1 >= len(plus):
        res += plus[i]
    else:
        res += (plus[i] * plus[i+1])

for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        res += minus[i]
    else:
        res += (minus[i] * minus[i+1])

print(res)
