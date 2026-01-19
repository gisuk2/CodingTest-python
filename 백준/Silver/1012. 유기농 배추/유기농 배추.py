import sys
from collections import deque
input = sys.stdin.readline



# 상하좌우 이동벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, m, n, field): # 1을 찾으면 주변 다 0으로 만들기
   queue = deque([(x,y)]) # 탐색 첫 시작을 체크큐에 넣고
   field[x][y]=0 # 넣은 위치에 0으로 초기화

   while queue:
      cx, cy = queue.popleft()

      for i in range(4): # 상하좌우 탐색시작
         nx = cx + dx[i]
         ny = cy + dy[i]

         if 0 <= nx < m and 0 <= ny < n: # 움직인 곳의 범위와 1 체크
            if field[nx][ny] == 1:
               field[nx][ny] = 0  # 방문 처리
               queue.append((nx, ny))
      
T = int(input().strip())

for i in range(T):

   m, n, k = map(int, input().split())
   field = [[0]*m for i in range(n)]
   # check_li = []

    # 배추 위치 입력받아 심기
   for _ in range(k):
      x, y = map(int, input().split())
      field[y][x] = 1  # x가 가로(열), y가 세로(행)이므로 field[y][x]
   
   # print(field)
   count = 0  # 지렁이 마리수

       # 전체 밭을 순회
   for i in range(n):
      for j in range(m):
         # 배추를 발견하면 지렁이 한 마리 추가하고 인접 배추들 모두 제거(BFS)
         if field[i][j] == 1:
            bfs(i, j, n, m, field)
            count += 1
                
   print(count)