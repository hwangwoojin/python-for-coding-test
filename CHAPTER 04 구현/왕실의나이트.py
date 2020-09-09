# 115p
# 실전문제
# 왕실의 나이트

# 현재 나이트의 좌표가 입력된다.
location = input()
x = int(ord(location[0]) - int(ord('a'))) + 1
y = int(location[1])

# 나이트가 움직이는 거리
steps = [(2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2)]

result = 0
# 나이트가 이동할 수 있는 좌표를 구한다.
for step in steps:
    loc_x, loc_y = x + step[0], y + step[1]
    # 그 좌표가 여전히 체스판 안이라면, 결과에 1을 더한다.
    if 1 <= loc_x <= 8 and 1 <= loc_y <= 8:
        result += 1

print(result)