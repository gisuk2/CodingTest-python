# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 두 수를 입력받고 각각 최대공약수, 최소공배수 출력하는 간단한거네

a_t, b_t = map(int, input().split())

if a_t >= b_t :
    a = a_t
    b = b_t
else:
    a = b_t
    b = a_t


i=1
max_g=0

for i in range(1,b+1):
    if a%i==0 and b%i==0:
        max_g = i

print(max_g)
print(max_g* a//max_g * b//max_g)
    