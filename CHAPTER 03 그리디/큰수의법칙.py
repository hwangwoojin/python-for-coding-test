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

# 가장 큰 수가 더해지는 횟수를 구한다.
# 그 다음 큰 수가 더해지는 횟수를 구한다.
count_max2 = M // (K + 1)
count_max1 = M - count_max2

# 결과를 구한다.
result = max1 * count_max1 + max2 * count_max2

# 첫째 줄에 답을 출력한다.
print(result)