import sys

# 1. 모든 입력을 한 번에 읽어와서 단어 단위로 쪼개 리스트로 만듭니다.
# li[0] = N, li[1] = M, 그 뒤로는 이름들이 순서대로 들어옵니다.
li = sys.stdin.read().split()

N = int(li[0])
M = int(li[1])

# 2. 듣도 못한 사람 명단을 주머니(set)에 담습니다. (인덱스 2번부터 N개)
# set은 중복을 허용하지 않고 탐색 속도가 매우 빠릅니다.
heard = set(li[2 : 2 + N])

# 3. 보도 못한 사람 명단을 주머니(set)에 담습니다. (N+2번 인덱스부터 끝까지)
seen = set(li[2 + N : ])

# 4. 두 주머니에 공통으로 들어있는 이름(교집합)을 찾습니다.
# '&' 연산자를 사용하면 양쪽에 모두 있는 데이터만 골라냅니다.
result = heard & seen

# 5. 사전순으로 출력해야 하므로 리스트로 변환 후 정렬(sorted)합니다.
sorted_result = sorted(list(result))

# 6. 결과 출력 (겹치는 사람 수, 그리고 이름들)
print(len(sorted_result))
for name in sorted_result:
    print(name)