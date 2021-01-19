# 197p
# 실전문제
# 떡볶이 떡 만들기

# 입력
# 1 <= N <= 1,000,000
# 1 <= M <= 2,000,000,000
N, M = map(int, input().split())
list_N = list(map(int, input().split()))

# 첫점과 끝점
start = 0
end = max(list_N)

# 이진 탐색 수행을 통해 구한다.
# 파라메트릭 서치
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in list_N:
        if i > mid:
            total += i - mid
    # 부족하면 왼쪽으로 이동 (더 자르기)
    if total < M:
        end = mid - 1
    # 충분하면 오른쪽으로 이동 (덜 자르기)
    else:
        # 최대한의 값을 구해야 하므로 result 에 기록만 하고 계속 수행
        result = mid
        start = mid + 1

# 정답 출력
print(result)
