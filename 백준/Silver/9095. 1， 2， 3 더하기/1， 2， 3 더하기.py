# DP Dynamic Programing인가?
# 쇼ㅗ발 규칙성을 못찾았는데...
# 점화식 찾는게 첫 번째
# 단순히 1,2,3 을 붙이는게 정답이라 -1 -2- 3 이 규칙
# 그럼 1 2 3 4 는 dp[i-4]인가? 맞다네
import sys

input = sys.stdin.read().split()

T = int(input[0])
nums = list(map(int,input[1:]))

dp = [0]*12
dp[1]=1
dp[2]=2
dp[3]=4

for i in range(4,11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for n in nums:
    print(dp[n])
