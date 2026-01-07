# 튜플의 x, y 값 둘다 각각 비교해야함
# 전체 비교? 정렬은 아니지않나? 계수비교?
# N 이 2~50 이라 수가 적음-> 브루트포스?

# 1. 리스트에 전부 저장 후, 각 하나씩 전체비교로 등수측정

import sys
input = sys.stdin.readline
N = int(input())

# li_all = [int(input().split()) for _ in range(int(input()))] #외않돼
# split()은 문자열을 공백기준으로 나누어 리스트를 반환
# 2등이 3명이면 3,4등이 없네...? set? 중복수 만큼 마이너스?

li_all = [list(map(int, input().split())) for _ in range(N)]
li_rank = [1]*N

# for i in li_all:
#     for j in li_all:
#         if i[0] > j[0] and i[1] > j[1]:
#             li_rank[(i.index())] -= 1

for i in range(N):
    for j in range(N):
        if (li_all[i])[0] < (li_all[j])[0] and (li_all[i])[1] < (li_all[j])[1] :
            li_rank[i] += 1




print(*li_rank)