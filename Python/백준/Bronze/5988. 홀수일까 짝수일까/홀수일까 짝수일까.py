import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    k = int(input())
    
    if k % 2 == 0:
        print('even')
    else:
        print('odd')