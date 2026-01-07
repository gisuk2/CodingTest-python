# 아니 시간초과 ;;;
# 규칙을 찾아서 처리해야하나? 리스트에 저장하는거말고?
# 아님 그냥 set? 순서가 없어서 못하지않나

# dequeue 쓰는 문제였구나...

# N = int(input())
# li = [x for x in range(1,N+1)]

# while(len(li)>1):
#     li.remove(li[0])
#     li.append(li[0])
#     li.remove(li[0])

# print(*li)


import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

dq = deque(range(1, N+1))

while len(dq)>1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])