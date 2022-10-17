import heapq
import sys

n= int(input())
heap =[]
for i in range(n):
    m = int(sys.stdin.readline())
    if m == 0:
        if len(heap) ==0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, m)