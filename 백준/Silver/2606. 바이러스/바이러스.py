# BFS 탐색
# 인접 리스트로 그래프 구현
# 방문 리스트 설정, 탐색queue 설정
# 탐색queue가 끝날때까지 리스트의 다음번의 방문여부를 체크

import sys
from collections import deque
input = sys.stdin.read
data = input().split()

n = int(data[0])
v = int(data[1])



graph = [[] for _ in range(n+1)] # 이게 뭔차이냐 [[]*(n+1)] 음 알것같기도
for i in range(v):
    a, b = int(data[2 + i*2]) , int(data[3 + i*2])
    graph[a].append(b)
    graph[b].append(a)


# queue = deque([])

def bfs(start):
    visited = [False]*(n+1)
    queue = deque([start])
    visited[start] = True
    cnt = 0

    while queue:
        curr = queue.popleft()

        for neighbor in graph[curr]:
        
            # if visited[neighbor] == False:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                cnt += 1
            
    return cnt

print(bfs(1))


            



