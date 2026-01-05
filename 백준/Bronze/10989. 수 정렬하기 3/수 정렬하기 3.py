# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# N = int(input())
# arr = []

# for i in range(N):
#     temp = int(input())
#     arr.append(temp)

# arr.sort()

# for i in range(len(arr)):
#     print(arr[i])

# 메모리 제한 발생
# arr에 N 10**7 만큼의 데이터가 들어가기에
# 저장없이 출력하는 계수 정렬이 필요

# 값이 입력되면 해당하는 숫자의 index 에 +1을 하는것

# N = int(input())

# # 리스트컴프리헨션 arr = [x for x in range(N)]
# # arr 리스트 10001번째까지 0을 만들고
# arr = [0 for _ in range(10001)]

# for i in range(N):
#     # if int(input()) == i:
#     arr[int(input())] += 1

# for i in range(10001):
#     if arr[i] == 0:
#         continue
#     print(arr[i])




# 계수 정렬로 풀어보자
# 수가 10000 보자 작거나 같으니까 0으로 초기화한 값 리스트를 만들고
# 입력된 수를 +1 하는식으로 하는 것

import sys
input = sys.stdin.readline

N = int(input())
arr = [0]*10001

for i in range(N):
    arr[int(input())] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
# 왜 안되지 븅신인가?
# 입력방식 바꿨고
# arr[]에 0넣은거 10001개 만들었고
# 아하! input에 괄호를 안넣었네 ㅄ