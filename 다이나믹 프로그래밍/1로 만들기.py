# 217p
# 실전문제
# 1로 만들기

# 입력
X = int(input())


# 모든 경우를 사용해서 1을 만들고 최소 횟수를 구하는 재귀함수
def make_one(target, count):
    # 1이 만들어지면 종료
    if target == 1:
        return count
    # 5, 3, 2 로 나누거나 1을 뺸다.
    result = 30000
    if target % 5 == 0:
        result = min(result, make_one(target // 5, count + 1))
    if target % 3 == 0:
        result = min(result, make_one(target // 3, count + 1))
    if target % 2 == 0:
        result = min(result, make_one(target // 2, count + 1))
    result = min(result, make_one(target - 1, count + 1))
    # 가장 작은 값을 출력한다.
    return result


# 답을 구한다.
print(make_one(X, 0))
