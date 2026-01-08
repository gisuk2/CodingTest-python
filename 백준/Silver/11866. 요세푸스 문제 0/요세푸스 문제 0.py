import sys
from collections import deque

input = sys.stdin.readline

data = (input().split())
N = int(data[0])
K = int(data[1])
li = deque()
for i in range(1,N+1):
    li.append(i)
ans = ''
while (True) :
    if len(li)==1:
        ans += str(li.popleft())
        # print(li.popleft())
        break
    li.rotate(-K+1)
    ans += str(li.popleft()) + ', '
print(f"<{ans}>")

