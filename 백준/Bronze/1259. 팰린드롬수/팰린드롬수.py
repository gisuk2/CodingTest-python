# 어떤 단어를 뒤에서부터 읽어도 똑같다면 그 단어를 팰린드롬이라고 한다. 'radar', 'sees'는 팰린드롬이다.

# 수도 팰린드롬으로 취급할 수 있다. 수의 숫자들을 뒤에서부터 읽어도 같다면 그 수는 팰린드롬수다. 121, 12421 등은 팰린드롬수다. 123, 1231은 뒤에서부터 읽으면 다르므로 팰린드롬수가 아니다. 또한 10도 팰린드롬수가 아닌데, 앞에 무의미한 0이 올 수 있다면 010이 되어 팰린드롬수로 취급할 수도 있지만, 특별히 이번 문제에서는 무의미한 0이 앞에 올 수 없다고 하자.

######################################
# 보자마자 이건 while 함수를 쓰는거다
# 문자열로 받아서 list로 만든다음 index로 번호찾아서 비교하는 로직?

# 홀/짝수 구분을 해야하나 range에 슬라이싱 써도 될거같은데

# while문도 제대로 못쓰네 돌겠네
# 입력값이 0을 받을때까지 계속해서 반복해야함.

# while True:
#     word = input()

#     if word == 0:
#         break

#     word_list = list[word]

#     for i in range(len(word_list)): # 0 1 2 
#         if word_list[i] == word_list[::-(i+1)]:
#             print('yes')
#         else:
#             print('no')


# 원본과 뒤집은 것([::-1])이 같은지 확인
# 아... 맞네 슬라이싱하면 숫자뒤집기가 가능하지...

while True:
    word = input()

    if word == '0':
        break

    word_list = list[word]

    if word == word[::-1]:
        print('yes')
    else:
        print('no')


        