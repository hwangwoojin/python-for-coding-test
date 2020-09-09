# 118p
# 실전문제
# 게임 개발

# 맵 크기
N, M = map(int, input().split())
# 캐릭터 위치
x, y, d = map(int, input().split())
# 지도
map_data = []
for row in range(N):
    line = list(map(int, input().split()))
    map_data.append(line)

# 이동하는 위치 (0: 북, 1: 동, 2: 남, 3: 서)
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 지도에서 해당 위치를 방문했는지 여부
# 처음 위치는 방문한 것으로 표시
visit_data = [[0 for col in range(M)] for row in range(N)]
visit_data[x][y] = 1

# 이동한다.
result = 1
is_land = True
while is_land:
    has_target = False
    for i in range(4):
        # 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
        d = (d + 3) % 4
        target_direction = direction[d]
        # 왼쪽에 아직 가보지 않은 칸이 존재한다면 왼쪽으로 회전한 다음 한칸 전진한다.
        # 왼쪽 방향에 가보지 않은 칸이 없다면 왼쪽으로 회전만 한다.
        dx, dy = x + target_direction[0], y + target_direction[1]
        if map_data[dx][dy] == 0 and visit_data[dx][dy] == 0:
            x, y = dx, dy
            visit_data[x][y] = 1
            has_target = True
            result += 1
            break
    # 네 방향 모두 가본 칸이거나 바다이면 바라보는 방향을 유지한 채로 한칸 뒤로 간다.
    # 뒤쪽이 바다이면 움직임을 멈춘다.
    if not has_target:
        x, y = x - direction[d][0], y - direction[d][1]
        if map_data[x][y] == 1:
            is_land = False

# 답을 출력한다.
print(result)