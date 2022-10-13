# https://www.acmicpc.net/problem/2293
# 메모리 제한 4mb
# 0.5

import sys 

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0 for i in range(k+1)]
# 동전의 가취
coins =[int(input()) for i in range(n)]
# print(c) ex 1 2 5
dp[0] = 1 # 동전을 1개 쓸때 대비

for i in coins : # 동전 하나씩 탐색
    for j in range(i, len(dp)): # 동전의 종류를 순회함
        if j - i >= 0 : # 특
            dp[j] +=dp[j-i]

print(dp[k]) # 합이 k원이 되는 경우의 수를 출력