# https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline
N , K = map(int, input().split())

동전 = []
최소값  = 0 
for _ in range(N):
    
    A = int(input())
    # if A < K :
    #     동전.append(A) # 목표값 미만은 제외
    동전.append(A)
동전 = sorted( 동전, reverse=True) # 정렬 됨

for i in 동전 :
    if K == 0:
        break
    최소값 += K//i
    K %= i
print(최소값)