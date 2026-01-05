# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)


# 반복 횟수를 모름. 10 이하의 랜덤 횟수 반복
# 그냥 입력이 없다면 break 으로 해야하는데
# 마지막 입력받고 다음줄 입력값이 없는데 받는다는 코드를 쓰면 에러아닌가


# for i in range(10):
#     a,b = map(int, input().split())
#     print(a+b)


while True:
    try:
        # 1. 일단 입력을 받는다
        line = input()
        
        # 2. 공백을 기준으로 A와 B를 분리 (언패킹)
        A, B = map(int, line.split())
        
        # 3. 결과 출력
        print(A + B)
        
    except EOFError:
        # 더 이상 입력받을 데이터가 없으면 루프 탈출
        break