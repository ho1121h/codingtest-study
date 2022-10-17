## https://www.acmicpc.net/problem/8958
## 브론즈 2

import sys 
input = sys.stdin.readline

Test = int(input()) # 테스트 케이스

for i in range(Test): 
    OX = input().strip() # OX 입력
    OX = OX.split("X")  # X 기준으로 나눔
    score = 0   # 점수
    # print(OX)
    for j in OX: 
        # print(j)
         for k in range(len(j)):
            A = j[k:] # ex ) OO -> 2 ,1 로 읽힘
            # print(A)
            score += A.count("O")
        
    print(score)
    