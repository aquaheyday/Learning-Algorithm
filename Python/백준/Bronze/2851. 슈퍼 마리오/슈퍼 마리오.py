import sys
input = sys.stdin.readline

res = 0

for i in range(10):
    x = int(input())
    now = res + x
    
    if now <= 100:
        res = now
        continue

    
    if now - 100 <= 100 - res:
        res = now
    break
print(res)
    
    