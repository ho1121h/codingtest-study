
# https://www.acmicpc.net/problem/2884

import sys
input = sys.stdin.readline

h, m = map(int, input().split())

if h == 0:
    h += 24

if m < 45:
    h -=1
    m += 60
m -= 45

if h == 24 : #  (0 ≤ H ≤ 23, 0 ≤ M ≤ 59)
    h = 0
    
print(abs(h), abs(m))