

N =int(input()) # 그냥 input 해도됨


sort_l = []
for i in str(N):
    sort_l.append(i)

M =(sorted(sort_l, reverse=True))
#print(M)
print(int(''.join(M)))