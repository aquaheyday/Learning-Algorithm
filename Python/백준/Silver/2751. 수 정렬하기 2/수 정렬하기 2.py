import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    b = int(input())
    a.append(b)
    
a.sort()

print(*a, sep = '\n')
    