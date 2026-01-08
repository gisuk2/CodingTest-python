import sys
from collections import deque

# 필수: 입력을 받는 속도를 비약적으로 높여줍니다.
input = sys.stdin.readline

queue = deque()
n_str = input().strip()
if not n_str: exit() # 입력이 비어있을 경우 대비
n = int(n_str)

for _ in range(n):
    # split()을 통해 명령(cmd)과 값(value)을 분리
    order = input().split()
    cmd = order[0]

    match cmd:
        case 'push':
            queue.append(order[1])
        case 'pop':
            print(queue.popleft() if queue else -1)
        case 'size':
            print(len(queue))
        case 'empty':
            print(1 if not queue else 0)
        case 'front':
            print(queue[0] if queue else -1)
        case 'back':
            print(queue[-1] if queue else -1)