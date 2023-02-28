X = int(input())
x,P = map(int,input().split())
y,Q = map(int,input().split())

#an - (n-1)d = an - (n-1)d
#-(x-1)d + (y-1)d = ay - ax
#d = (ay-ax)/(y-x)

d = (Q-P)/(y-x)
a = P - (x-1)*d

for i in range(1,X+1):
    print(int(a + (i-1)*d))