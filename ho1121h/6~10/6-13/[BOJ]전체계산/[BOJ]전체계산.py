
n, m =map(int,input().split())
a =n #100
while n // m :# 나눔이 가능할때 까지 반복
    a  += n//m # 100+ 12 =112 /  112 + 1 = 113
    n //= m #12               /  1
print(a) #최종 a = 113