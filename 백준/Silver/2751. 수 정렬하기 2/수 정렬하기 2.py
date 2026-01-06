import sys

# 1. 한꺼번에 다 읽어서 공백 기준으로 자르기
# [1:]을 하는 이유는 첫 번째 값 N(개수)을 제외하기 위함입니다.
data = sys.stdin.read().split()

# 2. 중복 제거가 필요하다면 set, 아니면 바로 정렬
# 문제 조건에 중복이 없다면 바로 sorted를 씁니다.
res = sorted(map(int, data[1:]))

# 3. 한 번에 출력
sys.stdout.write('\n'.join(map(str, res)) + '\n')