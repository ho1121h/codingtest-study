# https://www.acmicpc.net/problem/1032

import sys
input = sys.stdin.readline

n = int(input()) 
a = list(input()) # 첫번째 문자열을 비교대상으로 선정
# print(a)
a_len = len(a) # 인덱싱을 위한것

for i in range(n - 1): 
    b = list(input()) # 나머지 문자열 입력
    for j in range(a_len): # 
        if a[j] != b[j]:
            a[j] = '?'
# print(b)
print(''.join(a))