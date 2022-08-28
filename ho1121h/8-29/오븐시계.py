h, m = map(int,input().split())
t = int(input())

## 요리에 필요한 시간을 더하기
h += t //60
m += t % 60

if m >= 60:
    h +=1
    m-=60
if h >= 24:
    h -=24

print(h, m)
