# https://www.hackerrank.com/challenges/30-nested-logic/problem

d2,m2,y2 = map(int,input().split())
d1,m1,y1 = map(int,input().split())

if((y2,m2,d2)<=(y1,m1,d1)): print(0)
elif((y2,m2)==(y1,m1)): print((d2-d1)*15)
elif((y2)==(y1)): print((m2-m1)*500)
else: print(10000)