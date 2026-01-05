# 문제
# 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

# 입력
# 알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.

N = input()

if type(N)==str:
    print(ord(N))
else:
    print(chr(N))



# match type(N):
#     case string:
#         print(ord(N))

#     case int:
#         print(chr(N))
