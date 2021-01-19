# 99p
# 실전문제
# 1이 될 때까지

#  N 과 K 를 입력받는다.
N, K = map(int, input().split())

# N 이 1이 될 때까지 반복한다.
result = 0
while N > 1:
    # N 이 K 로 나누어질 때 까지 1을 뺀다.
    target = (N // K) * K

    # 나눌 수 없다면 1까지 뺀다.
    if target == 0:
        result += N - 1
        N = 1
    # 나눌 수 있다면 나눈다.
    else:
        result += N - target + 1
        N = target // K

# 답을 출력한다.
print(result)