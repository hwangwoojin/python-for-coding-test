# 178p
# 실전문제
# 위에서 아래로

# N 이 주어진다.
N = int(input())

# N 개의 수가 입력된다.
numbers = []
for i in range(N):
    numbers.append(int(input()))

# 내립차순으로 정렬한다.
result = sorted(numbers, reverse=True)

# 답을 출력한다.
for i in result:
    print(i, end=' ')