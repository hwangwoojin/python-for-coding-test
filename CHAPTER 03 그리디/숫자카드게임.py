# 96p
# 실전문제
# 숫자 카드 게임

# N, M 이 주어진다.
N, M = map(int, input().split())

# N 개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다.
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

# 각 행에서 가장 작은 숫자를 뽑는다.
num_list = []
for i in range(N):
    matrix[i].sort()
    num_list.append(matrix[i][0])
# 그 중에서 가장 큰 숫자를 선택한다.
num_list.sort()
result = num_list[N-1]

# 답을 출력한다.
print(result)