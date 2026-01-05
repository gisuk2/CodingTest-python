# 문제


# ISBN(International Standard Book Number)은 전 세계 모든 도서에 부여된 고유번호로, 국제 표준 도서번호이다. ISBN에는 국가명, 발행자 등의 정보가 담겨 있으며 13자리의 숫자로 표시된다. 그중 마지막 숫자는 체크기호로 ISBN의 정확성 여부를 점검할 수 있는 숫자이다. 이 체크기호는 일련번호의 앞에서부터 각 자리마다 가중치 1, 3, 1, 3…. 를 곱한 것을 모두 더하고, 그 값을 10으로 나눈 나머지가 0이 되도록 만드는 숫자 m을 사용한다. 수학적으로는 다음과 같다.

# ISBN이 abcdefghijklm 일 때, a+3b+c+3d+e+3f+g+3h+i+3j+k+3l+m ≡ 0 (mod 10)

# 즉, 체크기호 m = 10 - (a+3b+c+3d+e+3f+g+3h+i+3j+k+3l) mod 10 이다.

# 단, 10으로 나눈 나머지 값이 0일 경우 체크기호는 0이다.

# 전북대학교 중앙도서관에서 사서로 일하고 있는 영훈이는 책 정리를 하다가 개구쟁이 광현이에 의해서 ISBN이 훼손된 도서들을 발견했다. 광현이때문에 야근해야 하는 불쌍한 영훈이를 위해서 손상된 자리의 숫자를 찾아내는 프로그램을 작성해주자.


# a+3b+c+3d+e+3f+g+3h+i+3j+k+3l+m ≡ 0 (mod 10)
# 처음 든 생각은 dict 정리 다음 일차함수 계산인가?
# 다음은 * 표시를 어떻게 처리해둬야할까
# 조건문에 '*'를 제외하고.. 이런식으로?

# find로 찾기 replace로 바꾸기
# * 자리를 마지막에 짝홀수로 나눠서 곱3인지 체크해서 출력할까

# import sys
# input = sys.stdin.readline

# input_val = input()
# index_num = input_val.index('*')
# new_input = input_val.replace('*','0')

# # '*'를 0으로 채운 숫자 리스트 만들기
# val_list = [int(x) if x != '*' else 0 for x in isbn_str]
# # val_list = int,input_val()


# dict = {'a':val_list[0],'b':val_list[1],'c':val_list[2],
#         'd':val_list[3],'e':val_list[4],'f':val_list[5],
#          'g':val_list[6],'h':val_list[7],'i':val_list[8],
#           'j':val_list[9],'k':val_list[10],'l':val_list[11],
#            'm':val_list[12], }

# answer = 10 - (dict['a']+3*dict['b']+dict['c']
#       +3*dict['d']+dict['e']+3*dict['f']
#       +dict['g']+3*dict['h']+dict['i']
#       +3*dict['j']+dict['k']+3*dict['l']
#       +dict['m'])%10 

# if index_num %2==0:
#     print(answer)
# else:
#     print(answer//3)


#######################################

# import sys
# input = sys.stdin.readline

# # 1. 입력 및 리스트 변환
# isbn_str = input().strip()
# star_idx = isbn_str.index('*')
# # '*'를 0으로 채운 숫자 리스트 만들기
# val_list = [int(x) if x != '*' else 0 for x in isbn_str]

# # 2. '*'를 0이라 치환하고 현재 합계 구하기
# total = 0
# for i in range(13):
#     weight = 3 if i % 2 == 1 else 1
#     total += val_list[i] * weight

# # 3. 10의 배수가 되기 위해 '추가로 필요한 값' (사용자님의 answer)
# needed = (10 - (total % 10)) % 10

# # 4. '*'의 가중치에 따라 실제 숫자 x 찾기
# star_weight = 3 if star_idx % 2 == 1 else 1

# for x in range(10):
#     # (가중치 * x)를 10으로 나눈 나머지가 우리가 필요한 값(needed)과 같은지 확인
#     if (star_weight * x) % 10 == needed:
#         print(x)
#         break


#######################################

# import sys
# input = sys.stdin.readline

# S = input().strip()
# star_idx = S.find('*')

# # 가로로 길게 쓰는 대신 슬라이싱 활용
# # [::2]는 0, 2, 4... 인덱스 (가중치 1)
# # [1::2]는 1, 3, 5... 인덱스 (가중치 3)

# s_list = [int(c) if c != '*' else 0 for c in S]

# # 홀수/짝수 인덱스별로 합계를 한 번에 구함
# total = sum(s_list[0::2]) + sum(s_list[1::2]) * 3

# # '*' 위치의 가중치 결정 후 결과 도출
# w = 3 if star_idx % 2 ==1 else 1
# for x in range(10):
#     if (total + x * w) % 10 == 0:
#         print(x)
#         break

#######################################
# 안보고 풀어보기
# 슬라이싱 활용하기

import sys
input = sys.stdin.readline

val = input().strip()
star_idx = val.find('*')+1
total = 0


# '*'를 0으로 치환한 리스트 만들기 val 맞나?
val_list = [int(val) if val !='*' else 0 for val in val]
total = sum(val_list[::2]) + sum(val_list[1::2])*3

for i in range(10):
    if (total + i * (1 if star_idx%2 else 3))%10 == 0:
        print(i)
        break

# 시ㅣㅣㅣㅣㅣㅣㅣㅂㅂㅂㅂㅂval 리스트컴프리헨션 for val이 맞나?
# 런타임에러ㅓㅓㅓㅓㅓㅓㅗㅗㅗㅗㅗ
# 뭐였지 index 범위가 문제였지 않았나???
# t비ㅏㄹ break가 아니네 맞을텐데 분명
