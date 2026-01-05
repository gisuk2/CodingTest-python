
arr = [[0]*14 for x in range(15)]

for i in range(0,14):
    arr[0][i] = i+1

# print(arr)

for i in range(1,15):
    for j in range(14):
        for k in range(j+1):
            arr[i][j] += arr[i-1][k]

# print(arr)

T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    print(arr[k][n-1])