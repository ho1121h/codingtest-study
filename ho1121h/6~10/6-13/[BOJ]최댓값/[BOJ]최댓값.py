입력 = [int(input()) for i in range(9)]


print(max(입력) , 입력.index(max(입력))+1,sep='\n')


#전통적인 방법

입력 = []
for i in range(9):
    입력.append(int(input()))

print(max(입력) , 입력.index(max(입력))+1,sep='\n')