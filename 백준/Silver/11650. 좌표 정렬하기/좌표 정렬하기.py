import sys
input = sys.stdin.readline

N = int(input())
li = []

for _ in range(N):
    a,b = map(int, input().split())
    li.append((a,b))

li.sort(key= lambda x : (x[0], x[1]))

for a, b in li:
    print(f"{a} {b}")