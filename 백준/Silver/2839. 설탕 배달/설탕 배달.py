# 5와 3의 배수로 이루어진 수인가?
# N => 5*a + 3*b
# 브루트포스로 하자
# 리스트에 모든 수를 담아?


N = int(input())
cnt = []
li = []

for i in range(5000) :
    for j in range(2000):
        if 5*i + 3*j == N:
            cnt.append(i+j)
if len(cnt)==0:
    print('-1')
else:
    print((min(cnt)))





# 애초에 5로 먼저 담고, 3으로 담으면 되잖아
# 근데 ^ㅣ바 11은 5로 2번담으면 안돼고 1번담고 3으로 2번담으면 담겨져

# 각 수마다 최소가 되는 값을 찾아?
#  

