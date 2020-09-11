# 180p
# 실전문제
# 성적이 낮은 순서로 학생 출력하기

# N 이 입력된다.
N = int(input())

# 학생의 이름과 성적이 주어진다.
data = []
for i in range(N):
    line = list(input().split())
    name, grade = line[0], int(line[1])
    data.append((name, grade))


# 성적을 기준으로 정렬하는 함수
def setting(e):
    return e[1]


# 성적이 낮은 순서대로 정렬한다.
result = sorted(data, key=setting)

# 이름을 성적이 낮은 순서대로 출력한다
for i in result:
    print(i[0], end=' ')