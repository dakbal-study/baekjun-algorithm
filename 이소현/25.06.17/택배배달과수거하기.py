def solution(cap, n, deliveries, pickups):
    answer = 0
    d = 0  # 배달 잔여 물량
    p = 0  # 수거 잔여 물량

    # 가장 멀리 있는 집부터 처리하기 위해 리스트를 역순으로 사용
    deliveries.reverse()
    pickups.reverse()

    for i in range(n):
        d += deliveries[i]
        p += pickups[i]
        # 배달이나 수거할 물량이 남아있다면
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (n - i) * 2

    return answer