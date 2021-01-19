# 197p
# 실전문제
# 떡볶이 떡 만들기

# 입력
# 1 <= N <= 1,000,000
# 1 <= M <= 2,000,000,000
N, M = map(int, input().split())
list_N = list(map(int, input().split()))

# 가장 긴 떡의 길이
list_N.sort()
max_N = list_N[N - 1]

# 위에서부터 최대높이까지 자른다.
# H: 높이
for H in range(max_N - 1, 0, -1):
    # H 로 잘랐을 때 떡의 길이와 M 을 비교한다.
    # 같으면 출력
    length = 0
    for i in list_N:
        if i > H:
            length += (i - H)
    if length == M:
        print(H)
        break
