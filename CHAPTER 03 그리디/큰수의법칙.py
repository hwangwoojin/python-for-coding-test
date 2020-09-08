# 92p
# 실전문제
# 큰 수의 법칙

# N, M, K 의 자연수가 주어진다.
N, M, K = map(int, input().split())

# N 개의 자연수가 주어진다.
num_list = list(map(int, input().split()))

# 가장 큰 수를 찾는다.
# 그 다음 큰 수를 찾는다.
num_list.sort()
max1 = num_list[N - 1]
max2 = num_list[N - 2]

# 가장 큰 수를 K 번 더한다.
# 그 다음 큰 수를 1 번 더한다.
# 이를 M 번 될때까지 반복한다.
result, count_k = 0, 0
for i in range(M):
    if count_k == K:
        result += max2
        count_k = 0
        continue
    else:
        result += max1
        count_k += 1

# 첫째 줄에 답을 출력한다.
print(result)