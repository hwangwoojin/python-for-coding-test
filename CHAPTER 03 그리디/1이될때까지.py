# 99p
# 실전문제
# 1이 될 때까지

#  N 과 K 를 입력받는다.
N, K = map(int, input().split())

# N 이 1이 될 때까지 반복한다.
result = 0
while True:
    if N == 1:
        break
    # N 이 K 로 나누어지면 나눈다.
    if N % K == 0:
        N /= K
    # 그렇지 않다면 1 을 뺀다.
    else:
        N -= 1
    result += 1

# 답을 출력한다.
print(result)