# 197p
# 실전문제
# 부품 찾기

import sys

# N, N 개의 정수, M, M 개의 정수 입력
N = int(input())
list_N = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
list_M = list(map(int, sys.stdin.readline().rstrip().split()))

# 계수 정렬을 위한 리스트 (1 <= M <= 100000)
array = [0] * 100001

# list_N 을 계수 정렬을 위한 리스트에 기록한다.
for i in list_N:
    array[i] = 1

# 계수 정렬 리스트에서 찾는다.
for i in list_M:
    if array[i] == 0:
        print('no')
    else:
        print('yes')