# 226p
# 실전문제
# 효율적인 화폐 구성

# 1 <= N <= 100
# 1 <= M <= 10000
N, M = map(int, input().split())
# 1 <= list_N <= 10000
list_N = []
for i in range(N):
    list_N.append(int(input()))

# DP 테이블
d = [10001] * (M + 1)
d[0] = 0

# bottom-up 으로 해결
for i in range(N):
    for j in range(list_N[i], M + 1):
        if d[j - list_N[i]] != 10001:
            d[j] = min(d[j], d[j - list_N[i]] + 1)

# 결과 출력
if d[M] == 10001:
    print(-1)
else:
    print(d[M])
