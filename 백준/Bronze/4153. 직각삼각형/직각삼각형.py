# 무작위 n회의 예제 입력을 0 0 0 이 나올때까지 계속 반복
# input 받은 값들을 list로 묶은다음 오름차순 정렬
# [0]^2 = [1]^2 + [2]^2 계산으로 right wrong 출력
# 0 0 0 일 경우 while 문 탈출

while True:
    input_list = list(map(int, input().split()))

    if input_list[0] == 0 and input_list[1] == 0 and input_list[2] == 0:
        break

    new_list = sorted(input_list)
    # print(new_list)

    if (new_list[2])**2 == (new_list[1])**2 + (new_list[0])**2:
        print('right')
    
    else:
        print('wrong')
        