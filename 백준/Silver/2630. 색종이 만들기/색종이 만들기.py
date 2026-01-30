import sys
input = sys.stdin.readline

N = int(input().strip())

paper = [list(map(int, input().split())) for _ in range(N)]
# print(paper)

white = 0
black = 0

def solution(x, y, n):
    global white
    global black

    color = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != color:
                solution(x, y, n//2)
                solution(x+n//2, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y+n//2, n//2)

                return
    if color == 0:
        white += 1
    else:
        black += 1
solution(0,0,N)
print(white)
print(black)