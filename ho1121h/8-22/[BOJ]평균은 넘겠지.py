import sys
t = int(sys.stdin.readline())
for i in range(t):
     
    a = sys.stdin.readline().split()
    m= []
    for j in a:
        j =int(j)
        m.append(j)
    b = m.pop(0)
    avg = sum(m)/b
    avg_l= []
    for k in m:
        if k > avg:
            avg_l.append(k)
    평균비율 = (len(avg_l)/b)*100
    print(f'{평균비율:.03f}%')
    # print(f'{round(len(avg_l)/b)}%')