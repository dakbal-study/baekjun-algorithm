from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    trucks = deque(truck_weights)
    answer = 0
    
    tmp = 0
    while bridge:
        tmp -= bridge.popleft() # 지나간 트럭 무게 제외
        
        if trucks:
            if trucks[0] + tmp <= weight: # 다음 트럭 올릴 수 있으면 올리기
                t = trucks.popleft() 
                bridge.append(t)
                tmp += t
            else: # 못올리면 시간만 + 1
                bridge.append(0)
        answer += 1
    
    return answer