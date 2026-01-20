import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# ⭐ 핵심: 작은 번호부터 방문하기 위해 각 리스트 정렬
for i in range(1, n+1):
    graph[i].sort()

visited = [False]*(n+1)
def bfs(start):
   # 각 노드에 대한 방문 리스트 를 적어야함
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)

visited_dfs = [False] * (n+1)
def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)

dfs(v)
print()
bfs(v)
