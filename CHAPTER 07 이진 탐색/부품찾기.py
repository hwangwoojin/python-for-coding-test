# 197p
# 실전문제
# 부품 찾기

import sys

# N, N 개의 정수, M, M 개의 정수 입력
N = int(input())
list_N = set(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
list_M = list(map(int, sys.stdin.readline().rstrip().split()))

# 집합에서 찾는다.
for i in list_M:
    if i in list_N:
        print('yes')
    else:
        print('no')