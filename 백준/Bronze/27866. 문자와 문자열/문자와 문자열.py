val = input()
i_val = int(input())

answer=''
cnt=0
for i in val:
    answer = i
    cnt+=1
    if cnt == i_val:
        break
print(answer)

