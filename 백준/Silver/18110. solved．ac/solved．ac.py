# import sys

# input = sys.stdin.read
# # 모든 입력을 한줄로 받기
# data = input().split()
# n = int(data[0])

# scores = sorted(map(int, (data[1:])))

# # print(scores)

# true_round = int(n*0.15+0.5)

# answer = (scores[true_round:n-true_round])
# answer = int(sum(answer)/len(answer)+0.5)
# print(answer)

import sys

# 1. 한 번에 모든 데이터를 읽어와서 리스트로 만듭니다.
data = sys.stdin.read().split()

# 입력 데이터가 아예 없는 경우 방지
if not data:
    exit()

n = int(data[0])

# 2. [중요] n이 0일 때의 예외 처리
if n == 0:
    print(0)
else:
    # 3. 데이터 정렬
    scores = sorted(map(int, data[1:]))

    # 4. 사사오입 계산 (0.5를 더해서 int로 형변환)
    # n * 0.15가 4.5라면 5.0이 되어 int로 5가 됨
    cut = int(n * 0.15 + 0.5)

    # 5. 슬라이싱으로 절삭
    # n=1, cut=0인 경우 scores[0:1]이 되어 안전함
    final_scores = scores[cut : n - cut]

    # 6. 평균 계산 및 최종 사사오입
    if not final_scores:
        print(0)
    else:
        # sum/len 결과에 0.5를 더해 반올림 효과
        avg = sum(final_scores) / len(final_scores)
        print(int(avg + 0.5))