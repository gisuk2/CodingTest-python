import sys

input = sys.stdin.readline

T = int(input().strip())


if T%10 !=0:
    print(-1)

else:
    cnt = 0
    li = []
    cnt += T//300
    li.append(cnt)
    cnt = 0
    cnt += (T%300)//60
    li.append(cnt)
    cnt = 0
    cnt += ((T%300)%60)//10
    li.append(cnt)
    print(*li)
