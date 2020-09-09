# 110p
# 예제
# 상하좌우

# N 이 주어진다.
N = int(input())

# 이동할 계획이 주어진다.
plan = list(input().split())

# 이동한다.
x, y = 1, 1
for p in plan:
    # 공간을 벗어나는 움직임은 무시한다.
    # 그게 아니라면 움직인다.
    if p == 'L' and y != 1:
        y -= 1
    elif p == 'U' and x != 1:
        x -= 1
    elif p == 'R' and y != N:
        y += 1
    elif p == 'D' and x != N:
        x += 1

# 답을 출력한다.
print(x, y)