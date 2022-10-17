import itertools
# Permutations 함수를 이용하기
# Permutations는 원하는 배열에서 모든 조합을 구하는 함수임

n, m = map(int, input().split()) # 주어진 자연수 n 과 m 이 주어짐
nums = [i for i in range(1, n+1)] # 자연수 n 만큼 빈공간 생성  ex :[1,2,3,4]

array = itertools.combinations(nums, m) # 모든 배열 조회됨 -> m 만큼 m 개 조합 조회

list = []
for i in array:
    list.append(i)

list.sort()

for i,j in list:

    print(i,j )
#### 런타임 에러


import itertools
# Permutations 함수를 이용하기
# Permutations는 원하는 배열에서 모든 조합을 구하는 함수임

n, m = map(int, input().split()) # 주어진 자연수 n 과 m 이 주어짐
nums = [i for i in range(1, n+1)] # 자연수 n 만큼 빈공간 생성  ex :[1,2,3,4]

array = itertools.combinations(nums, m) # 모든 배열 조회됨 -> m 만큼 m 개 조합 조회 (1,2) ()


for i in array:
    for j in i:
        print(j, end = ' ')
    print(sep='\n')