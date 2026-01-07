# 과연 조건문으로 푸는게 맞나..?

# alp 지우고 괄호 쌍 지우고 남으면 no 출력?
# 알파벳 어캐지우냐
# 차라리 괄호를 따로 뽑아내서 정리하고 지워서 체크?

import sys

while (True):
    string = input()
    if string=='.':
        break
    check=''
    for i in string:
        if i == '(' or i =='[' or i ==']' or i ==')':
            check += i
    
    while('[]' in check or '()' in check):
        check = check.replace('()','').replace('[]','')
    # print(check)
    if len(check)>0:
        print('no')
    else:
        print('yes')









    # cnt_a = 0
    # cnt_b = 0
    # cnt_c = 0
    # cnt_d = 0
    # check_cnt=0
    # string = input()

    # if string=='.':
    #     break
    # if '(' in string and ')' in string and string.find('(') < string.find(')'):
    #     print('yes')
    # elif '[' in string and ']' in string and string.find('[') < string.find(']'):
    #     print('yes')
    # else:
    #     print('no')


    # for i in string:
    #     if string.find('(')>string.find(')'):
    #         if i == '(':
    #             cnt_a += 1
    #         if i == ')':
    #             cnt_b += 1
    #     else:
    #         check_cnt +=1
        

    #     if string.find('[')>string.find(']'):
    #         if i == '[':
    #             cnt_c += 1
    #         if i == ']':
    #             cnt_d += 1
    #     else:
    #         check_cnt +=1
    # if cnt_a == cnt_b and cnt_c == cnt_d and check_cnt==0:
    #     print('yes')
    # else:
    #     print('no')