### https://www.acmicpc.net/problem/10214


import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    y =0
    k =0
    
    for j in range(9): # 기본 9회 진행되므로 
        a, b = map(int,input().split()) # 그냥 단순히 9번 입력받도록
        y +=a # 점수는 간단하게 더하는 식으로
        k +=b
    if y < k :
        print("Korea")
    elif y>k :
        print("Yonsei")
    else:
        print("Draw")