# 113p
# 예제
# 시각

# N 이 입력된다.
N = int(input())

# 최대 경우가 86400 밖에 되지 않으므로
# 반복문을 사용하는 것이 더 직관적이다.
result = 0
for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            # 3이 포함되면 카운트를 늘린다.
            if '3' in str(i) + str(j) + str(k):
                result += 1

# 답을 출력한다.
print(result)