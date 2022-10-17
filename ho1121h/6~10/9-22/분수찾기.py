# 보기가 주어짐 => 지그재그로 움직임

#https://www.acmicpc.net/problem/1193

import sys

input = sys.stdin.readline

n = int(input())

# 리스트를 생성하기보단 분자 분모를 만드는 방식으로 접근
# 정수가 주어짐 => 대응하는 분수를 출력
L = 0
Max_n = 0

while n > Max_n : # ex) n = 3 
    L += 1        # L= 2
    Max_n += L    # Max_n = 3
# print(L, Max_n)

gap = Max_n - n   # gap = 0
# print(gap)

if L % 2 == 0:    # L =2 ->참
    분자 = L - gap # 분자 = 2
    분모 = gap + 1 # 분모 = 1
else:
    분자 = gap + 1
    분모 = L - gap 
print(f'{분자}/{분모}') # 1 분의 2 출력
