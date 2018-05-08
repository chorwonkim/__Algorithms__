# 음의 가중치가 있을 경우에는 벨만-포드 알고리즘(Bellman-Ford Algorithm) 사용 필요
# 그래프, 가격, 부모 노드라고 하는 세 가지의 Hash Table 필요

# 예를 들어 시작점-(6)->A, 시작점-(2)->B 인 경우에는 다음과 같다.
graph = {}
graph["start"] = {}
graph["start"]['a'] = 6
graph["start"]['b'] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}  # 도착점에는 이웃이 없다.

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []
