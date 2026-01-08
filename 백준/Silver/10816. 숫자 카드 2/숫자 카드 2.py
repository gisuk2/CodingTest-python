# 카드개수N, 정수값이 크다, 찾을 카드 개수M
# 계수 비교로 풀어야 할 듯 아닌가 수가큰데

# 그래그래 시간초과야
# set 집합 사용?
# count도 처음부터 찾는거아닌가


import sys
from collections import Counter

N = int(input())
card_vals = sys.stdin.readline().strip().split()

M = int(input())
find_num = sys.stdin.readline().strip().split()

# print(card_vals)
answer =[]
counts = Counter(card_vals)
for i in find_num:
    answer.append(counts[i])

# answer =[]
# for i in find_num:
#     cnt=0
#     for j in card_vals:
        
#         if i == j:
#             cnt += 1
#     answer.append(cnt)




print(*answer)
