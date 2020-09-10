# 152p
# 실전문제
# 미로 탈출

from collections import deque

# N, M 이 주어진다.
N, M = map(int, input().split())

# 미로의 정보가 주어진다.
maze = []
for row in range(N):
    maze.append(list(map(int, input().split())))

# bfs 를 위한 큐
queue = deque()

# 이동할 방향
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# 최소 이동칸의 갯수를 찾는 bfs
def bfs(x, y):
    # 현재 위치를 큐에 넣는다.
    queue.append((x, y))
    # 큐가 빌 때까지 반복한다.
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치를 확인한다.
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            # 공간을 벗어난 경우 무시한다.
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 벽인 경우 무시한다.
            if maze[nx][ny] == 0:
                continue
            # 처음 방문하는 경우에만 기록한다.
            # 그게 최단 거리이기 때문이다.
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    # 최단 거리를 반환한다.
    return maze[N - 1][M - 1]


# 최소 이동칸의 갯수를 찾는다.
result = bfs(0, 0)

# 최소 이동칸의 갯수를 출력한다.
print(result)
