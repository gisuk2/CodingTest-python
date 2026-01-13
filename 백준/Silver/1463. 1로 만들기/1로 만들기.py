import sys

input = sys.stdin.readline

X = int(input().strip())

dp = [0]*(X+1)
dp[1]=0
for i in range(2, X + 1):
    # 1. 일단 1을 빼는 길을 기본으로 정함 (모든 숫자가 가능하니까)
    dp[i] = dp[i - 1] + 1
    
    # 2. 2로 나눌 수 있다면, 위에서 정한 값과 지름길을 비교함
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
        
    # 3. 3으로 나눌 수 있다면, 현재까지 찾은 최선과 또 다른 지름길을 비교함
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[X])


# 
