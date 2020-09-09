# 115p
# 실전문제
# 왕실의 나이트

# 현재 나이트의 좌표가 입력된다.
location = input()
x = location[0]
y = location[1]

# 체스판
nx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ny = ['1', '2', '3', '4', '5', '6', '7', '8']

# 나이트가 움직이는 거리
dx = [2, 2, 1, -1, -2, -2, -1, 1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

result = 0
# 나이트 좌표를 구한다.
for i in range(len(nx)):
    for j in range(len(ny)):
        if nx[i] == x and ny[j] == y:
            # 나이트가 이동할 수 있는 좌표를 구한다.
            for k in range(len(dx)):
                loc_x, loc_y = i + dx[k], j + dy[k]
                # 그 좌표가 여전히 체스판 안이라면, 결과에 1을 더한다.
                if 0 <= loc_x < 8 and 0 <= loc_y < 8:
                    result += 1

print(result)