t = int(input())

for i in range(t):
    a = int(input())
    oh = []

    for j in range(a):

        b = input().split()
        c = b[0]
        d = b[1]
        oh.append([b,int(d)])
    oh.sort(key= lambda x: x[1])
    print(oh[-1][0][0])