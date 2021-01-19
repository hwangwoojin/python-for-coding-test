# 223p
# 실전문제
# 바닥 공사

# 1 <= N <= 1000
N = int(input())

# DP 테이블
d = [0] * 1001
d[1] = 1
d[2] = 3

# bottom-up 으로 해결한다.
for i in range(3, N + 1):
    d[i] = d[i - 1] + (2 * d[i - 2])

# 결과 출력
print(d[N])