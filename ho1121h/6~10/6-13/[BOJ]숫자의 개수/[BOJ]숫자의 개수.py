A = int(input())
B = int(input())
C = int(input())

ABC = str(A * B * C)

for i in range(10):
    print(ABC.count(str(i)))