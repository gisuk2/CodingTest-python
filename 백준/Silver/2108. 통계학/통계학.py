# N은 홀수라고 가정하자.

import sys
from collections import Counter

input = sys.stdin.read
data = input().split()
li = list(map(int, data[1:]))
arr = [0]*8001
li_so = sorted(li)

# 산술평균 (소수점 이하 첫째자리에서 반올림)
print(int(sum(li)/len(li)+0.5)) if sum(li) >=0 else print(int(sum(li)/len(li)-0.5))


# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
print(li_so[len(li)//2])




# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# enumerate 써서 arr[i] == max(arr)인거?
# 계수정렬
for i in li:
    arr[4000+i] += 1

count_li = []
for i in range(len(arr)):
    if arr[i] == max(arr):
        count_li.append(i)

if len(count_li) == 1:
    print((count_li[0])-4000)

else:
    print((count_li[1])-4000)


# counts = Counter(arr)
# for i in range(len(arr)):
#     if counts[max(arr)] >= 2:
#         if arr[i] == max(arr):
#             print(i - 4000)
#     else:
#         if arr[i] == max(arr):
#             print(i - 4000)



        




# 넷째 줄에는 범위를 출력한다.
print(li_so[-1] - li_so[0])


