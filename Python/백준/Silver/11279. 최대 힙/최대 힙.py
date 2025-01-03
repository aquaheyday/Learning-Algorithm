import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []

for i in range(n):
    x = int(input())
    
    if x == 0:
        if len(h) == 0:
            print(0)
        else:
            print(-h[0])
            heapq.heappop(h)
    else:
        heapq.heappush(h, -x)

