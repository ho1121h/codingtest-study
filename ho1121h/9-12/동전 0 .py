# https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline
N , K = map(int, input().split())

동전 = []
최소값  = 0 
for _ in range(N):
    
    A = int(input())
    if A < K :
        동전.append(A) # 목표값 미만은 제외

동전 = sorted( 동전, reverse=True) # 정렬 됨

for i in 동전 :
    while i <= K : # 뺄 수 있는 최대값 동전으로 빼기 시작해서 소거
            K -= i
            최소값 += 1
print(최소값)