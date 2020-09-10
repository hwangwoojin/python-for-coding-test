# 149p
# 실전문제
# 음료수 얼려 먹기

# N 과 M 이 주어진다.
N, M = map(int, input().split())

# 아이스크림 틀의 형태가 주어진다.
ice = []
for row in range(N):
    col = list(map(int, input().split()))
    ice.append(col)

# 방문 여부
visited = [[False] * M for _ in range(N)]

# dfs 를 위한 스택
stack = []

# 인근 방향
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# dfs 함수
# 칸막이가 아닌, 방문하지 않은 모든 구멍을 방문한다.
def dfs(x, y):
    # 범위를 벗어나면 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    # 칸막이인 경우 즉시 종료
    if ice[x][y] == 1:
        return False
    # 현재 노드를 방문하지 않은 경우 방문 처리한다.
    if not visited[x][y]:
        visited[x][y] = True
        # 현재 노드 주변의 다른 노드를 재귀적으로 방문
        for d in direction:
            dfs(x + d[0], y + d[1])
        return True
    # 현재 노드를 이미 방문한 경우
    return False


# 틀의 모든 부분을 탐색한다.
result = 0
for i in range(N):
    for j in range(M):
        # 그래프 탑색으로 방문하자
        if dfs(i, j):
            result += 1

# 답을 출력한다.
print(result)
