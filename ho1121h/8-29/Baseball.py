### https://www.acmicpc.net/problem/10214


import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    y =0
    k =0
    
    for j in range(9):
        a, b = map(int,input().split())
        y +=a
        k +=b
    if y < k :
        print("Korea")
    elif y>k :
        print("Yonsei")
    else:
        print("Draw")