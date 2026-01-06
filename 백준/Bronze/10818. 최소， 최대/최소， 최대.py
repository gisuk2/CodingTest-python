# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 입력값을 리스트로 만들어서 그냥 함수쓰면...

N = int(input())

li = list(map(int, input().split()))


print(f"{min(li)} {max(li)}")