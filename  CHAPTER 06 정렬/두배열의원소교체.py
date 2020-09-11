# 182p
# 실전문제
# 두 배열의 원소 교체

# N, K 가 입력된다.
N, K = map(int, input().split())

# A 의 원소들이 입력된다.
A = list(map(int, input().split()))

# B 의 원소들이 입력된다.
B = list(map(int, input().split()))

# A 가 최대가 되도록 A 의 원소와 B 의 원소를 K 만큼 바꿔치기 한다.
# 이 때 바꿔치기 기준은 Greedy 로 접근했을때
# A 를 오름차순으로 정렬하고 B 를 내림차순으로 정렬했을 때 앞에서 K 개의 원소들이다.
A, B = sorted(A), sorted(B, reverse=True)
for i in range(K):
    # A 의 원소가 B 의 원소보다 크게 되면 종료한다.
    if A[i] >= B[i]:
        break
    A[i], B[i] = B[i], A[i]

# 답을 출력한다.
print(sum(A))
