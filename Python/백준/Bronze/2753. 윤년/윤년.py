import sys
input = sys.stdin.readline

n = int(input())

if n % 4 != 0:
    print(0)
else:
    if n % 100 != 0 or n % 400 == 0:
        print(1)
    else:
        print(0)