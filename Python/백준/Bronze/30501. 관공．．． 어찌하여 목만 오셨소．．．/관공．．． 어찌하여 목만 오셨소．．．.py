import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a = input().rstrip()
    
    if 'S' in a:
        print(a)
        break