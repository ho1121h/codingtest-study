import sys
input = sys.stdin.readline
test_place = int(input())
test_human = list(map(int,input().split()))

B, C = map(int, input().split())

# 총감독관이 감시할 인원 B
# 부감독관이 감시할 인원 C
# 각시험장에 총감독관은 한명만
# 각시험장 인원은 모두 감시해야함
# for i in range(test_place):
#     test_human[i] -= B
    
#     # 감독관수 += math.ceil(test_human[i]/C)
감독관수=0
for i in test_human:
    if i > B: # 반 인원이 총감독관이 감시하는 인원이하라면
        i -= B
        감독관수 += 1

        감독관수 += i//C
        if  i % C > 0:
            감독관수 +=1
    

    else:
        감독관수 +=1
        
print(감독관수)