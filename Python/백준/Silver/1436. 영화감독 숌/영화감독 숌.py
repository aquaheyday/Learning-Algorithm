import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
i = 666

while True:
    
    if str(i).count('666') > 0:
        cnt += 1
        if cnt == n:
            break
    i += 1
    
print(i)