import sys
input = sys.stdin.readline

N,M = map(int, input().split())

dict = {}
for i in range(N):
    a, b = map(str, input().split())
    dict.update({a : b})
for i in range(M):
    print(dict.get(input().strip()))