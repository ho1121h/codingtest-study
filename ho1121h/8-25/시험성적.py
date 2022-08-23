import sys
input = sys.stdin.readline

N = int(input())

if 101> N >=90 :
    print('A')
elif 90> N >= 80:
    print("B")
elif 80 > N >=70:
    print("C")
elif 70> N >=60:
    print("D")
else:
    print("F")