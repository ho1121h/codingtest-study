## https://www.acmicpc.net/problem/1546
## 평균
import sys

input = sys.stdin.readline

N = int(input())

N_list = list(map(int,input().split()))

M = max(N_list)


# for i in N_list:
#     if i != M:
        
#         N_list2.append(int(i)) 

New_list = [] 

for i in N_list:
    
    New_list.append((i/M)*100) # 각 점수를 최대 점수로 나눈뒤 X100 해서 새로 리스트에 추가

avg = sum(New_list)/N # 평균
print(avg)

