import sys
input = sys.stdin.readline

N, K = map(int, input().split())

li = list(map(int, sys.stdin.read().split()))
li.sort(reverse=True)

# print(li)
cnt = 0
for i in li:
    cnt += K//i
    K = K%i

print(cnt)

