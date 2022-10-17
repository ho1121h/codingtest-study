import heapq
import sys

n= int(input())
heap =[]
for i in range(n):
    m = int(sys.stdin.readline())
    #heap.sort(reverse=True) #시간초과
    if m == 0:
        if len(heap) ==0: # 힙이 비어있으면 0 출력
            print(0)
        else:
            print(-heapq.heappop(heap)) #제일 작은값 출력
    else:
        heapq.heappush(heap, -m) # 음수로 입력하면 가장 큰값이 가장 작은 값으로 입력됨