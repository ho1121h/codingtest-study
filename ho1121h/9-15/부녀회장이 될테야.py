
# https://www.acmicpc.net/problem/2775
import sys

input = sys.stdin.readline

T = int(input())


for i in range(T):
    k = int(input())    # 몇층
    n = int(input())    # 몇호
    p = [i for i in range(1, n+1)] # 리스트 생성
    # print(p) [1,2,3]
    #          [1,2,3]
    for x in range(k): # 층
        for y in range(1,n):# 각 호에
             p[y] += p[y-1]# 사람수 더함
    print(p[-1])