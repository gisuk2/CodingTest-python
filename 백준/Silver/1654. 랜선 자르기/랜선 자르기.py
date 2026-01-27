# 11 개를 만들려면 가장 작은 수를 찾고 나누고
# 수를 줄여가면서 n개까지 몫을 키우려고
# 

import sys
input = sys.stdin.read

data = list(map(int, input().split()))

k, n = data[0], data[1]

li = data[2:]

start = 1
end = max(li)
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for x in li:
        cnt += x // mid

    if cnt >=n:
        result = mid
        start = mid + 1

    else:
        # n개를 못 만든다면, 길이를 줄여야 함
        end = mid - 1
        
print(result)
