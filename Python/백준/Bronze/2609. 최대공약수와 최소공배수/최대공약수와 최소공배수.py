import sys
import math
input = sys.stdin.readline

a,b = map(int, input().split())

g = math.gcd(a,b)
l = a * b // g

print(g)
print(l)


