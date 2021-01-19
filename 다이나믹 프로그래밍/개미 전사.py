# 220p
# 실전문제
# 개미 전사

# 3 <= N <= 100
# 0 <= K <= 1000
N = int(input())
K = list(map(int, input().split()))

# DP 테이블
d = [0] * 100
d[0] = K[0]
d[1] = max(K[0], K[1])

# bottom-up 으로 식량의 최댓값을 구한다.
for i in range(2, N):
    # 이전 창고를 선택한 경우, 이전 창고를 선택하지 않은 경우 중 최댓값을 구한다.
    d[i] = max(d[i - 1], d[i - 2] + K[i])

# 결과 출력
print(d[N - 1])