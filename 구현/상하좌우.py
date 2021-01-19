# 110p
# 예제
# 상하좌우

# N 이 주어진다.
N = int(input())

# 이동할 계획이 주어진다.
plan = input().split()

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
# 이동한다.
nx, ny = 0, 0
for p in plan:
    # 이동 후 좌표를 구한다.
    for i in range(len(move_types)):
        if p == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어난 경우라면 무시한다.
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
        print("ignored")
    # 이동한다.
    x, y = nx, ny

# 답을 출력한다.
print(x, y)