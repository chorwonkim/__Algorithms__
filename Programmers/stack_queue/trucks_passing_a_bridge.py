# 리스트를 큐나 스택처럼 활용할려면
# 스택    LIFO, append(), pop()
# 큐      FIFO, append(), pop(0)

# pop()의 time complexity는 O(1)이지만, pop(0)는 O(N)
# 따라서 time complexity를 생각해 리스트를 큐로 사용하지 않음

# from collections import deque
#
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#
#     bridge = deque([0] * bridge_length)
#     trucks = deque(truck_weights)
#
#     while bridge:
#         answer += 1
#         bridge.popleft()
#
#         if trucks:
#             if sum(bridge) + trucks[0] <= weight:
#                 bridge.append(trucks.popleft())
#             else:
#                 bridge.append(0)
#
#     return answer


# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#
#     bridge = [0] * bridge_length
#     truck_weights.reverse()
#
#     while bridge:
#         answer += 1
#         bridge.pop(0)
#
#         if truck_weights:
#             # if sum(bridge) + truck_weights[0] <= weight:
#             if weight -
#                 bridge.append(truck_weights.pop())
#             else:
#                 bridge.append(0)
#
#     return answer


# sum이 O(N)이므로, 시간 초과 발생.
from collections import deque

def solution(bridge_length, weight, truck_weights):

    answer = 0

    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    bridge_weight = 0

    while bridge:
        answer += 1
        bridge_weight -= bridge.popleft()

        if trucks:
            if bridge_weight + trucks[0] <= weight:
                bridge_weight += trucks[0]
                bridge.append(trucks.popleft())
            else:

                bridge.append(0)

    return answer

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))