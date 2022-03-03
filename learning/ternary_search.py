import math, decimal

EPS = 1.0E-6
def distance(x,a,vp,vf):
    return math.sqrt(x*x + (1 - a)*(1 - a)) / vp + math.sqrt(a*a + (1 - x)*(1 - x)) / vf

vp, vf = map(int, input().split())
a = float(input())

left, right = 0, 1

while (right-left) >= EPS:
    f = left + (right - left) / 3
    g = right - (right - left) / 3
    if (distance(f, a, vp, vf) < distance(g, a, vp, vf)):
        right = g
    else:
        left = f
D = decimal.Decimal
print(D(left).quantize(D('1.0000007')))
#print(f'{round((left,7):.7f}')
