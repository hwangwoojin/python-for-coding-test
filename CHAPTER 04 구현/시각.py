# 113p
# 예제
# 시각

# N 이 입력된다.
N = int(input())

# 00시 00분 00초애서 0시 59분 59초 까지 시각 중
# 3이 하나라도 포함되는 경우의 수를 구한다.
count_3 = 6 * 10 * 6 * 10
count_not_3 = count_3 - 5 * 9 * 5 * 9

result = (N + 1) * count_not_3
# 3시가 포함되는 경우
if N >= 3:
    result += count_3 - count_not_3

# 답을 출력한다.
print(result)