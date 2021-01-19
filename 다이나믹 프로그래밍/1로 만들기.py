# 217p
# 실전문제
# 1로 만들기

# 입력
X = int(input())

# DP 테이블
d = [0] * 30001

# bottom-up 방식으로 구한다.
for i in range(2, X + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2, 3, 5로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

# 답을 구한다.
print(d[X])
