import sys
input = sys.stdin.readline

x = int(input())
n = int(input())

y = 0

for i in range(n):
    a, b = map(int, input().split())
    y += a * b
    
if x == y:
    print('Yes')
else:
    print('No')
    
