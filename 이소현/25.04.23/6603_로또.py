import sys
from itertools import combinations

while(1):
    nums = list(map(int,sys.stdin.readline().split()))
    if nums[0] == 0 and len(nums) ==1:
        break
    nums.pop(0)
    lotto_nums = list(combinations(nums, 6))
    for lotto in lotto_nums:
        print(*sorted(lotto)) # * : 언패킹 연산자 리스트나 튜플 등을 하나씩 풀어서 전달하는 역할 , 공백을 기준으로 나열된 값 출력
    print("")
